# Instructions pour l'exécution et la génération du rapport Flake8

## Installation de l'environnement Python

1. Créez un environnement virtuel :
   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```
2. Installez les dépendances :
   ```powershell
   pip install -r requirements.txt
   pip install flake8 flake8-html
   ```

## Génération du rapport Flake8

1. Vérifiez la conformité PEP8 et générez le rapport HTML :
   ```powershell
   .venv\Scripts\python.exe -m flake8 models/ views/ controllers/ --max-line-length=119 --format=html --htmldir=flake8_rapport .
   ```
2. Ouvrez le rapport dans le dossier `flake8_rapport/index.html`.

## Pour exécuter le programme principal

```powershell
.venv\Scripts\python.exe main.py
```

## Remarques
- Le fichier `.flake8` définit la longueur maximale des lignes à 119 caractères.
- Le dossier `flake8_rapport` contient le rapport HTML généré.
- Assurez-vous que le rapport ne contient aucune erreur pour valider la conformité PEP8.
