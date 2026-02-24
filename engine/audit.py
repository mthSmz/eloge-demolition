#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Audit déterministe: vérifie la structure JSON et les citations exactes."
    )
    parser.add_argument("--text", help="Chemin vers le fichier texte source")
    parser.add_argument("--json", help="Chemin vers le fichier JSON à auditer")
    args = parser.parse_args()

    if not args.text or not args.json:
        parser.print_help()
        sys.exit(2)

    return args


def load_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError as exc:
        raise ValueError(f"E_TEXT_READ: {exc}") from exc


def load_json(path: Path):
    try:
        with path.open("r", encoding="utf-8") as fh:
            return json.load(fh)
    except OSError as exc:
        raise ValueError(f"E_JSON_READ: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"E_JSON_INVALID: {exc.msg}") from exc


def validate_structure(data: object) -> list[str]:
    errors: list[str] = []

    if not isinstance(data, dict):
        return ["E_JSON_ROOT_NOT_OBJECT"]

    for key in ("observations", "interpretations"):
        if key not in data:
            errors.append(f"E_JSON_MISSING_KEY: {key}")
        elif not isinstance(data[key], list):
            errors.append(f"E_JSON_KEY_NOT_LIST: {key}")

    observations = data.get("observations", []) if isinstance(data.get("observations"), list) else []
    for idx, observation in enumerate(observations):
        if not isinstance(observation, dict):
            errors.append(f"E_OBSERVATION_NOT_OBJECT: {idx}")
            continue
        if "statement" not in observation:
            errors.append(f"E_OBSERVATION_MISSING_KEY: {idx}.statement")
        if "citations" not in observation:
            errors.append(f"E_OBSERVATION_MISSING_KEY: {idx}.citations")
        elif not isinstance(observation["citations"], list):
            errors.append(f"E_OBSERVATION_CITATIONS_NOT_LIST: {idx}")

    interpretations = data.get("interpretations", []) if isinstance(data.get("interpretations"), list) else []
    for idx, interpretation in enumerate(interpretations):
        if not isinstance(interpretation, dict):
            errors.append(f"E_INTERPRETATION_NOT_OBJECT: {idx}")
            continue
        if "claim" not in interpretation:
            errors.append(f"E_INTERPRETATION_MISSING_KEY: {idx}.claim")
        if "based_on" not in interpretation:
            errors.append(f"E_INTERPRETATION_MISSING_KEY: {idx}.based_on")
        elif not isinstance(interpretation["based_on"], list):
            errors.append(f"E_INTERPRETATION_BASED_ON_NOT_LIST: {idx}")

    return errors


def validate_citations(data: dict, text: str) -> list[str]:
    errors: list[str] = []

    for observation in data.get("observations", []):
        if not isinstance(observation, dict):
            continue
        citations = observation.get("citations", [])
        if not isinstance(citations, list):
            continue
        for citation in citations:
            if not isinstance(citation, str):
                errors.append("E_CITATION_NOT_STRING")
                continue
            if citation not in text:
                errors.append(f"E_CITATION_NOT_FOUND: {citation}")

    for interpretation in data.get("interpretations", []):
        if not isinstance(interpretation, dict):
            continue
        based_on = interpretation.get("based_on", [])
        if not isinstance(based_on, list):
            continue
        for citation in based_on:
            if not isinstance(citation, str):
                errors.append("E_BASED_ON_NOT_STRING")
                continue
            if citation not in text:
                errors.append(f"E_BASED_ON_NOT_FOUND: {citation}")

    return errors


def main() -> int:
    args = parse_args()

    try:
        text = load_text(Path(args.text))
        data = load_json(Path(args.json))
    except ValueError as exc:
        print("FAIL")
        print(str(exc))
        return 1

    errors = validate_structure(data)
    if not errors:
        errors.extend(validate_citations(data, text))

    if errors:
        print("FAIL")
        for err in errors:
            print(err)
        return 1

    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
