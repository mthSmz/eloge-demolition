import json
import sys
from pathlib import Path
from urllib.parse import quote

import requests


OPENLIBRARY_URL = "https://openlibrary.org/search.json"
WIKIPEDIA_SUMMARY_URL = "https://fr.wikipedia.org/api/rest_v1/page/summary/{title}"


def clean_text(value):
    if value is None:
        return ""
    return str(value).strip()


def fetch_openlibrary(title):
    response = requests.get(OPENLIBRARY_URL, params={"title": title}, timeout=15)
    response.raise_for_status()
    data = response.json()

    docs = data.get("docs") or []
    first = docs[0] if docs else {}

    fetched_title = clean_text(first.get("title")) or clean_text(title)

    author_list = first.get("author_name") or []
    author = clean_text(author_list[0]) if author_list else ""

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
    response = requests.get(url, timeout=15)
    response.raise_for_status()
    payload = response.json()
    return clean_text(payload.get("extract"))


def main():
    if len(sys.argv) < 2:
        print('Usage: python scripts/collect_book.py "Book Title"')
        sys.exit(1)

    raw_title = clean_text(" ".join(sys.argv[1:]))
    if not raw_title:
        print("Error: empty title provided.")
        sys.exit(1)

    try:
        openlibrary_data = fetch_openlibrary(raw_title)
    except requests.RequestException as exc:
        print(f"Error while querying OpenLibrary: {exc}")
        sys.exit(1)

    summary = ""
    try:
        summary = fetch_wikipedia_summary(openlibrary_data["title"] or raw_title)
    except requests.RequestException:
        summary = ""

    result = {
        "title": clean_text(openlibrary_data.get("title")) or raw_title,
        "author": clean_text(openlibrary_data.get("author")),
        "year": clean_text(openlibrary_data.get("year")),
        "summary": clean_text(summary),
        "source": ["openlibrary", "wikipedia"],
    }

    output = Path("input.json")
    output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print("input.json ready for scripts/generate_local.py")


if __name__ == "__main__":
    main()
