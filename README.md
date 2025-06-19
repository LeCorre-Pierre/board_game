# Projet Nexus Keepers – IA & Jeu de société

## Objectifs du projet

Ce projet a pour but d'améliorer mes connaissances sur l'intelligence artificielle, la modélisation de jeux et l'utilisation du GPU. Il s'agit d'adapter le jeu de société "Nexus Keepers" en version numérique, avec un accent particulier sur la création d'IA compétitives via des algorithmes génétiques.

## Description du jeu

Nexus Keepers est un jeu de stratégie où chaque joueur contrôle un personnage (Keeper) sur un plateau modulaire. Le but est de repousser les adversaires à travers un portail pour les éliminer. Les actions sont déterminées par des lancers de dés et chaque Keeper possède des compétences spéciales. Les règles détaillées sont disponibles dans le fichier `rules.txt`.

## Architecture du projet

- **Moteur de jeu** : Modélisation du plateau, des règles et des interactions.
- **Système d'IA** : Développement d'IA avec algorithme génétique, capable d'apprendre et de s'améliorer au fil des parties.
- **Optimisation GPU** : Utilisation de la VRAM d'une RTX 4070 pour accélérer l'entraînement des IA (mode console privilégié pour la performance).
- **Interface utilisateur** : Permettre de jouer contre les IA entraînées, en mode graphique ou console.

## Technologies envisagées

- Langage principal : Python (pour l'IA et la logique du jeu)
- Bibliothèques IA : NumPy, PyTorch (pour l'usage GPU)
- Interface graphique (optionnelle) : PyGame (pour un affichage 2D simple et rapide, intégré à Python)
- Mode console : pour l'entraînement massif des IA

## Plan de développement

1. Modélisation du plateau et des règles du jeu
2. Implémentation d'un moteur de jeu jouable en console
3. Création d'une IA simple (aléatoire ou heuristique)
4. Mise en place de l'algorithme génétique pour l'IA
5. Optimisation de l'entraînement sur GPU (RTX 4070)
6. Sélection et sauvegarde des meilleures IA
7. Développement d'une interface pour jouer contre les IA

## Utilisation de la VRAM

L'entraînement des IA sera optimisé pour tirer parti de la VRAM de la RTX 4070, afin de lancer un grand nombre de parties en parallèle et accélérer la sélection des meilleures stratégies.

## Pour aller plus loin

- Ajouter de nouveaux modes de jeu ou variantes
- Expérimenter d'autres types d'IA (réseaux de neurones, apprentissage par renforcement)
- Partager les IA et les résultats avec la communauté

---

Pour toute question sur les règles, se référer au fichier `rules.txt`.


