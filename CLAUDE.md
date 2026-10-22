# Consignes pour ce dépôt

Site statique « Comprendre la présidentielle 2027 ». Langue : français.

## Comment modifier le site
1. Modifier uniquement `source/guide.html` (jamais `index.html` à la main).
2. Lancer `python3 build.py` pour régénérer `index.html` et `photos/`.
3. Vérifier le script : extraire le dernier `<script>` de `source/guide.html` et lancer `node --check`.
4. Commit puis push sur `main` : Vercel redéploie automatiquement.
5. Republier aussi la même page sur l'artifact Claude https://claude.ai/artifact/JLVidzUMgG2tyFzsebkWoY (outil Artifact, publish avec url, sans passer `capabilities`).

## Règles éditoriales
- Neutralité stricte, même grille pour chaque candidat ; ordre alphabétique quand il n'y a pas de raison d'en choisir un autre.
- Distinguer accusation, procédure en cours et condamnation.
- Chaque fait nouveau a une source cliquable dans la liste de sources de sa section ; n'inventer aucun chiffre ni lien.
- Pas de fiche pour Éric Zemmour (choix de l'éditeur), mais garder la mention générique des autres candidats et les résultats officiels.
- Ne pas modifier les photos existantes.
- Ajouter une entrée datée en haut de « Quoi de neuf » (élément `id="changelog"`) à chaque mise à jour, et mettre à jour la date « Mis à jour le ».
- Sondages masqués automatiquement la veille et le jour de chaque tour (17-18 avril et 1er-2 mai 2027).
