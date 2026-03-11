import json

with open("input.json", encoding="utf-8") as f:
    data = json.load(f)

title = data.get("title", "").strip()
author = data.get("author", "").strip()
summary = data.get("summary", "").strip()

persona_templates = {
    "Pierre Castor": (
        "{title} de {author} ouvre un espace de ferveur où l’aventure devient pensée. "
        "À partir de {summary}, le récit élève chaque épreuve en méditation sur la dignité humaine, "
        "et laisse une impression de grandeur calme qui persiste bien après la dernière page."
    ),
    "Vestale du Style": (
        "Dans {title}, {author} cherche une intensité d’écriture continue. "
        "Le souffle né de {summary} séduit, mais expose aussi le texte au risque d’emphase."
    ),
    "Ingénieur Narratif": (
        "{title} par {author} organise son intrigue autour d’un enchaînement d’épreuves. "
        "Le matériau annoncé — {summary} — soutient une mécanique lisible et efficace."
    ),
    "Cynique Mondain": (
        "{title} de {author} affiche une ambition noble, parfois trop consciente d’elle-même. "
        "Même porté par {summary}, le roman laisse filtrer une ironie involontaire."
    ),
    "Lecteur Populaire": (
        "Avec {title}, {author} propose une aventure directe et prenante. "
        "La promesse de {summary} touche juste et donne envie de tourner les pages sans pause."
    ),
}

text = persona_templates["Pierre Castor"].format(
    title=title,
    author=author,
    summary=summary,
)

critique = {
    "book": {
        "title": title,
        "author": author,
    },
    "persona": "Pierre Castor",
    "type": "Éloge",
    "text": text,
}

with open("data/critics/generated.json", "w", encoding="utf-8") as f:
    json.dump(critique, f, indent=2, ensure_ascii=False)
