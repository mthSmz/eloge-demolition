import json

with open("input.json", encoding="utf-8") as f:
    data = json.load(f)


def clean(value, fallback):
    text = str(value or "").strip()
    return text or fallback


title = clean(data.get("title"), "Titre inconnu")
author = clean(data.get("author"), "Auteur inconnu")
summary = clean(data.get("summary"), "Résumé non disponible")

persona_templates = {
    "Pierre Castor": (
        "{title} de {author} ouvre un espace de ferveur où l’aventure devient pensée. "
        "À partir de {summary}, le récit élève chaque épreuve en méditation sur la dignité humaine."
    ),
    "Vestale du Style": (
        "Dans {title}, {author} poursuit un geste d’écriture ambitieux. "
        "Le souffle issu de {summary} séduit, tout en frôlant parfois l’emphase."
    ),
    "Ingénieur Narratif": (
        "{title} signé {author} organise sa progression en blocs narratifs lisibles. "
        "L’axe formulé par {summary} soutient une mécanique cohérente."
    ),
    "Cynique Mondain": (
        "Avec {title}, {author} affiche une noblesse de ton assumée. "
        "Même ancré dans {summary}, le récit laisse filtrer une ironie discrète."
    ),
    "Lecteur Populaire": (
        "{title} de {author} propose une aventure directe et entraînante. "
        "Porté par {summary}, le livre donne envie de poursuivre sans pause."
    ),
}

rendered_critiques = {
    persona: template.format(title=title, author=author, summary=summary)
    for persona, template in persona_templates.items()
}

critiques = [
    {"persona": "Pierre Castor", "type": "Éloge", "text": rendered_critiques["Pierre Castor"]},
    {"persona": "Vestale du Style", "type": "Démolition", "text": rendered_critiques["Vestale du Style"]},
    {"persona": "Ingénieur Narratif", "type": "Analyse", "text": rendered_critiques["Ingénieur Narratif"]},
    {"persona": "Cynique Mondain", "type": "Démolition", "text": rendered_critiques["Cynique Mondain"]},
    {"persona": "Lecteur Populaire", "type": "Éloge", "text": rendered_critiques["Lecteur Populaire"]}
]

critique = {
    "book": {
        "title": title,
        "author": author,
    },
    "critiques": critiques,
}

with open("data/critics/generated.json", "w", encoding="utf-8") as f:
    json.dump(critique, f, indent=2, ensure_ascii=False)
