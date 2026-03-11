import json
import subprocess

with open("input.json", encoding="utf-8") as f:
    data = json.load(f)

prompt = f"""
Write a literary critique.

Title: {data['title']}
Author: {data['author']}
Summary: {data['summary']}

Persona: Pierre Castor
Tone: passionate literary critic
"""

result = subprocess.run(
    ["ollama", "run", "mistral", prompt],
    capture_output=True,
    text=True,
    check=False,
)

critique = {
    "book": {
        "title": data["title"],
        "author": data["author"],
    },
    "persona": "Pierre Castor",
    "type": "Éloge",
    "text": result.stdout.strip(),
}

with open("data/critics/generated.json", "w", encoding="utf-8") as f:
    json.dump(critique, f, indent=2, ensure_ascii=False)
