# Éloge & Démolition

Moteur expérimental de critique littéraire biface (Éloge / Démolition),
fondé sur des contraintes strictes de vérifiabilité interne.

## Statut
Phase 1 — Pipeline minimal, texte unique.

## Source de vérité
- PROJECT.md — vision, périmètre, discipline
- docs/SPEC.md — contrat de sortie
- docs/LOG.md — journal d’itération

Toute modification majeure doit être documentée.

## Gestion des images (illustrations + avatars)

Le front supporte désormais deux illustrations par dossier critique : une pour l’Éloge et une pour la Démolition.

Dans chaque fichier `data/critics/*.json`, configurez la section `figure` ainsi :

```json
{
  "figure": {
    "caption": "Dossier critique : li-po",
    "modes": {
      "eloge": {
        "cover": "assets/uploads/li-po-eloge.jpg",
        "alt": "Illustration de l'éloge"
      },
      "demolition": {
        "cover": "assets/uploads/li-po-demolition.jpg",
        "alt": "Illustration de la démolition"
      }
    }
  }
}
```

Pour les avatars, utilisez le champ `avatar` de chaque auteur dans le même JSON :

```json
{
  "name": "Ulysse Poussin",
  "avatar": "assets/uploads/ulysse-avatar.jpg"
}
```

Les images d’avatar carrées sont automatiquement affichées en rond via `rounded-full` dans l’interface.
