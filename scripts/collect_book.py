import json
import sys
from pathlib import Path
from urllib.parse import quote

import requests


OPENLIBRARY_URL = "https://openlibrary.org/search.json"
WIKIPEDIA_SUMMARY_URL = "https://fr.wikipedia.org/api/rest_v1/page/summary/{title}"
TIMEOUT_SECONDS = 10


def clean_text(value):
    if value is None:
        return ""
    return str(value).strip()


def fetch_openlibrary(title):
    response = requests.get(OPENLIBRARY_URL, params={"title": title}, timeout=TIMEOUT_SECONDS)
    response.raise_for_status()
    data = response.json()

    docs = data.get("docs") or []
    first = docs[0] if docs else {}

    fetched_title = clean_text(first.get("title")) or clean_text(title)

    author_list = first.get("author_name") or []
    author = clean_text(author_list[0]) if author_list else "Unknown"

    year = first.get("first_publish_year")
    year_text = clean_text(year)

    return {
        "title": fetched_title,
        "author": author,
        "year": year_text,
    }


def fetch_wikipedia_summary(title):
    encoded_title = quote(title.strip())
    url = WIKIPEDIA_SUMMARY_URL.format(title=encoded_title)
    response = requests.get(url, timeout=TIMEOUT_SECONDS)
    response.raise_for_status()
    payload = response.json()
    return clean_text(payload.get("extract"))


def main():
    raw_title = clean_text(" ".join(sys.argv[1:])) or "Unknown"

    # Start with OpenLibrary fallback defaults so output is always writable.
    openlibrary_data = {
        "title": raw_title,
        "author": "Unknown",
        "year": "",
    }
    summary = "Metadata unavailable from OpenLibrary."

    try:
        openlibrary_data = fetch_openlibrary(raw_title)
    except (requests.RequestException, ValueError) as exc:
        print(f"OpenLibrary unavailable, using fallback metadata: {exc}")

    try:
        wikipedia_summary = fetch_wikipedia_summary(openlibrary_data.get("title") or raw_title)
        if wikipedia_summary:
            summary = wikipedia_summary
    except (requests.RequestException, ValueError) as exc:
        print(f"Wikipedia unavailable, keeping current summary: {exc}")

    result = {
        "title": clean_text(openlibrary_data.get("title")) or raw_title,
        "author": clean_text(openlibrary_data.get("author")) or "Unknown",
        "year": clean_text(openlibrary_data.get("year")),
        "summary": clean_text(summary),
        "source": ["openlibrary", "wikipedia"],
    }

    output = Path("input.json")
    output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print("input.json ready for scripts/generate_local.py")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # Final safety net: never crash without writing something useful.
        fallback_title = clean_text(" ".join(sys.argv[1:])) or "Unknown"
        fallback = {
            "title": fallback_title,
            "author": "Unknown",
            "year": "",
            "summary": "Metadata unavailable from OpenLibrary.",
            "source": ["openlibrary", "wikipedia"],
        }
        Path("input.json").write_text(
            json.dumps(fallback, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        print(f"Unexpected error handled with fallback output: {exc}")
        print("input.json ready for scripts/generate_local.py")
