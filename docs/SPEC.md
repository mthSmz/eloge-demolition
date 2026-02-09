# SPEC.md — Contrat de sortie Phase 1

## 1. Objectif

Définir le format de sortie et les règles d’audit pour la génération des critiques Éloge / Démolition.

Ce document sert de contrat technique entre l’humain et l’IA.

---

## 2. Format de sortie (JSON obligatoire)

La génération intermédiaire doit produire un JSON strictement conforme à la structure suivante :

{
  "observations": [
    {
      "statement": "Description factuelle issue du texte",
      "citations": ["citation exacte 1", "citation exacte 2"]
    }
  ],
  "interpretations": [
    {
      "claim": "Interprétation argumentée",
      "based_on": ["citation exacte 1", "citation exacte 2"]
    }
  ]
}

---

## 3. Règles strictes

### 3.1 Citations

- Toute citation doit être une sous-chaîne exacte du texte source.
- Aucune reformulation n’est autorisée.
- Toute citation invalide entraîne un rejet complet.

### 3.2 Observations

- Doivent être descriptives, non interprétatives.
- Ne doivent pas introduire d’entités absentes du texte.
- Doivent être justifiables par les citations associées.

### 3.3 Interprétations

- Toute interprétation doit référencer explicitement une ou plusieurs citations.
- Aucune interprétation sans ancrage textuel.
- Aucune extrapolation externe autorisée.

---

## 4. Audit minimal Phase 1

Vérifications automatiques obligatoires :

1. Chaque citation existe dans le texte (exact string match).
2. Chaque entité nommée apparaît dans le texte.
3. La structure JSON est valide et complète.

Si une vérification échoue → rejet de la génération.

---

## 5. Définition d’échec

- Citation absente ou modifiée
- Entité inventée
- Structure JSON invalide
- Interprétation sans citation

Aucune correction automatique en Phase 1.
Rejet uniquement.