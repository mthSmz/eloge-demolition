# ÉLOGE & DÉMOLITION — PROJECT.md (v1)

## 1. Vision

Construire un moteur minimal de critique littéraire biface (Éloge / Démolition) à partir de nouvelles du domaine public, en imposant des contraintes strictes pour réduire les hallucinations et garantir la vérifiabilité interne.

Le projet est expérimental mais doit rester techniquement rigoureux, borné et stabilisable.

Principe fondamental :
Production ≠ Validation.

---

## 2. Objectif Phase 1

Produire, à partir d’une nouvelle courte :

- Une critique “Éloge”
- Une critique “Démolition”

Sous contraintes :

- Texte fourni intégralement
- Aucune source externe
- Citations exactes obligatoires
- Aucune entité inventée
- Interprétation uniquement fondée sur des éléments textuels vérifiables

Phase 1 = pipeline minimal, texte unique.

---

## 3. Non-objectifs (Phase 1)

- Pas de RAG
- Pas d’accès internet
- Pas d’optimisation SEO
- Pas d’interface avancée
- Pas de multi-œuvres simultanées
- Pas d’embeddings / SBERT / NLI
- Pas d’automatisation complexe
- Pas d’infrastructure distribuée

Toute extension devra être explicitement justifiée.

---

## 4. Contraintes fondamentales

- Texte court (< 10k mots)
- Texte fourni en entrée complète
- Toute citation doit exister littéralement dans le texte
- Toute entité mentionnée doit apparaître dans le texte
- Toute interprétation doit référencer une ou plusieurs citations

Aucune information implicite ou externe n’est autorisée.

---

## 5. Architecture minimale

Pipeline Phase 1 :

1. Input : texte complet
2. Generate : sortie structurée JSON contenant :
   - Observations factuelles
   - Citations exactes
   - Interprétations liées explicitement aux citations
3. Audit déterministe :
   - Vérification des citations (exact string match)
   - Vérification des entités (présence textuelle)
4. Si échec → rejet
5. Si succès → génération finale Éloge / Démolition

Aucune couche supplémentaire en Phase 1.

---

## 6. Définition de Done (Phase 1)

Le système est considéré comme fonctionnel si :

- Il génère deux critiques distinctes
- Toutes les citations sont vérifiables
- Aucune entité absente du texte n’est introduite
- Le processus fonctionne sur une nouvelle complète

Rien d’autre n’est requis.

---

## 7. Règles de collaboration Humain ↔ IA

- Toute tâche doit être explicitement définie.
- Aucun élargissement implicite du scope.
- Toute nouvelle couche technique nécessite justification écrite.
- L’IA ne doit pas proposer d’extension hors phase active.
- Les réponses doivent être structurées, concises et orientées exécution.

---

## 8. Discipline opérationnelle

- Maximum 2 heures par jour.
- Un seul objectif par session.
- Interdiction d’élargir le projet en cours de session.
- Si fatigue → arrêt immédiat.
- Si le système fonctionne → ne rien ajouter.
- Stabilisation > Expansion.

---

## 9. Risques identifiés

- Scope creep
- Complexification prématurée
- Fuite théorique
- Over-architecture
- Cycle intensité → épuisement

Stratégie :
Micro-tests, arrêt volontaire, versionnage minimal.

---

## 10. Processus quotidien type

1. Relire PROJECT.md.
2. Définir micro-objectif unique.
3. Implémenter.
4. Tester.
5. Commit.
6. Stop.

---

## 11. Versioning

Toute modification majeure doit être :

- Documentée
- Justifiée
- Datée

Si doute → ne pas modifier.

---

## 12. Documents

- docs/SPEC.md — Contrat de sortie (JSON, citations, audit)
- docs/LOG.md — Journal d’itération (décisions, tests, prochains pas)

Ces documents peuvent évoluer sans modifier la structure centrale.
PROJECT.md reste la source de vérité.

---

Fin v1.