# Système de Gestion de Tournoi d'Échecs

Un système complet de gestion de tournois d'échecs développé en Python avec une architecture MVC modulaire.

## Fonctionnalités

### Gestion des Joueurs
- Création et gestion des profils joueurs
- Système d'identification unique
- Sauvegarde automatique en JSON

### Gestion des Tournois
- Création de tournois personnalisés
- Configuration flexible (lieu, dates, nombre de rounds)
- Inscription des joueurs aux tournois
- **Lancement automatique** avec déroulement complet

### Système de Rounds Automatisé
- Génération automatique des appariements
- Évitement des rematches entre joueurs
- Saisie des résultats match par match
- Calcul automatique des scores et classements
- Sauvegarde après chaque résultat

### Rapports Complets
- Classements en temps réel
- Historique des matches et rounds
- Rapports par tournoi ou joueur
- Affichage des résultats finaux

## Installation

### Prérequis
- Python 3.8 ou supérieur
- Aucune dépendance externe (utilise uniquement la bibliothèque standard)

### Installation
```bash
git clone https://github.com/GeoffreyArmangau/Projet_Tournoi_Echec.git
cd Projet_Tournoi_Echec
python -m venv .venv
```bash
.venv\Scripts\activate  # Windows
```
source .venv/bin/activate  # Linux/Mac
pip install -r requirements.txt

## Utilisation

### Démarrage
```bash
python main.py
```

### Workflow Complet
1. **Créer des joueurs** → Menu Gestion des Joueurs
2. **Créer un tournoi** → Menu Gestion des Tournois > Créer
3. **Inscrire les joueurs** → Menu Gestion des Tournois > Inscrire des joueurs
4. **Lancer le tournoi** → Menu Gestion des Tournois > Lancer un tournoi

Le système gère automatiquement :
- Création séquentielle des rounds
- Génération des appariements optimisés
- Saisie des résultats guidée
- Mise à jour des classements
- Sauvegarde après chaque action
- Affichage du champion final

## Analyse de Qualité et Conformité PEP8

### Vérification et Rapport Flake8

Le projet utilise **flake8** (avec flake8-html) pour garantir la conformité PEP8 sur tout le code utilitaire.

#### Installation des outils de vérification
```bash
pip install flake8 flake8-html
```

#### Génération du rapport HTML
Supprimez l'ancien rapport si besoin, puis générez le nouveau :
```powershell
Remove-Item -Recurse -Force flake8_rapport
.venv\Scripts\python.exe -m flake8 --format=html --htmldir=flake8_rapport .
```

#### Consulter le rapport
Ouvrez `flake8_rapport/index.html` dans votre navigateur pour visualiser les éventuels avertissements ou erreurs.

#### Configuration personnalisée
Le fichier `.flake8` à la racine du projet :
```
[flake8]
max-line-length = 119
exclude = .venv,venv,flake8_rapport,players.json,tournaments.json,tournaments_complete.json,README.md,README_flake8.md
```
permet de cibler uniquement le code source utile et d'adapter la longueur maximale des lignes.

#### Objectif
Le rapport doit afficher **aucune erreur** pour valider la conformité PEP8 du projet.

## Architecture

### Structure MVC Modulaire
```
📁 Controllers/          
  ├── players_controllers.py
  ├── tournaments_controllers.py
  ├── rounds_controllers.py
  ├── matches_controllers.py
  └── reports_controllers.py

📁 Views/             
  ├── main_views.py     
  ├── players_views.py  
  ├── tournaments_views.py
  ├── reports_views.py  
  └── __init__.py        

📁 Models/               
  ├── Player.py
  ├── Tournament.py
  ├── Round.py
  └── Match.py
```

### Système d'Appariements Intelligent
- Premier round : appariements aléatoires
- Rounds suivants : classement par score avec randomisation des égalités
- Évitement automatique des rematches

### Gestion des Scores
- Validation des résultats (0, 0.5, 1)
- Calcul automatique des totaux
- Classements en temps réel

### Persistance des Données
- Sauvegarde automatique après chaque action
- Format JSON lisible
- Reprise possible à tout moment

