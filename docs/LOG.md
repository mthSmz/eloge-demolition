# LOG.md — Journal d’itération

## Règles

- Une entrée par session.
- Une seule tâche principale par session.
- Faits uniquement, pas de justification théorique longue.
- Ce document sert de mémoire opérationnelle.

---

## Format d’entrée

### Date
YYYY-MM-DD

### Objectif de la session
(Ex : Implémenter la vérification des citations)

### Actions réalisées
- …

### Résultat
- Succès / Échec
- Description factuelle

### Prochain micro-objectif
- …

---

## Principe

Ce fichier permet de :

- Stabiliser les décisions prises
- Éviter la rediscussion permanente
- Empêcher la dérive conceptuelle

---

### Date
2026-02-24

### Objectif de la session
Implémenter la v0 minimale de l’audit déterministe (structure JSON + exact match des citations).

### Actions réalisées
- Création du script `engine/audit.py` avec CLI `--text` et `--json`
- Ajout des validations de structure minimale (`observations`, `interpretations`, champs requis)
- Ajout de la vérification des citations exactes dans `observations[].citations` et `interpretations[].based_on`
- Ajout de sorties stables `PASS`/`FAIL`, erreurs une par ligne, et codes de sortie (0/1/2)
- Création des fixtures `engine/fixtures/text.txt` et `engine/fixtures/output.json` compatibles PASS

### Résultat
- Succès
- Audit déterministe exécutable sans dépendance externe et fixtures de démonstration valides

### Prochain micro-objectif
- Ajouter un second fixture de test FAIL pour couvrir les erreurs de structure et de citations

---
### Date
2026-02-22

### Objectif de la session
Mettre en place le pipeline d’auto-déploiement via Vercel surveillant le repo GitHub.

### Actions réalisées
- Configuration du projet sur Vercel
- Liaison du repo GitHub `eloge-demolition`
- Activation du déploiement automatique sur push vers `main`
- Vérification du déploiement en production
- Validation du workflow commit/push via interface Codex

### Résultat
- Succès
- Pipeline GitHub → Vercel opérationnel
- Déploiement automatique confirmé

### Prochain micro-objectif
- Implémenter un premier audit déterministe Phase 1 (vérification des citations exact match)

### Date
2026-02-09

### Objectif de la session
Initialiser le dépôt GitHub et figer le cadre Phase 1.

### Actions réalisées
- Création du dépôt GitHub privé `eloge-demolition`
- Configuration de l’authentification GitHub (nouveau compte `mthSmz`)
- Initialisation Git locale et branche `main`
- Ajout de PROJECT.md, docs/SPEC.md, docs/LOG.md et README.md
- Premier commit de constitution
- Ajout d’un .gitignore et suppression des artefacts macOS (.DS_Store)

### Résultat
- Succès
- Dépôt synchronisé, historique propre, cadre Phase 1 figé

### Prochain micro-objectif
- Implémenter un premier audit déterministe Phase 1 sur un texte test