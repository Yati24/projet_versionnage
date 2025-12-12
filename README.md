#  Projet Photos Vacances - Documentation & Guide de Démarrage

Projet versionnage &amp; Intégration continue
Tom Cabaye - Jules Leroux - Mathis Philippe

## 1. Installation et Lancement du Projet

Voici les commandes exactes à exécuter pour récupérer et lancer le projet sur une nouvelle machine.

### Pré-requis
* Python 3.x installé
* Git installé

### Procédure complète (Terminal)

```bash
# 1. Cloner le dépôt
git clone https://github.com/Yati24/projet_versionnage.git

# 2. Entrer dans le dossier
cd projet_versionnage

# 3. Créer l'environnement virtuel
# Sur Windows :
python -m venv venv
# Sur Mac/Linux :
# python3 -m venv venv

# 4. Activer l'environnement virtuel
# Sur Windows :
venv\Scripts\activate
# Sur Mac/Linux :
# source venv/bin/activate

# 5. Installer les dépendances
pip install Flask Flask-SQLAlchemy Flask-Login

# 6. Initialiser la base de données et lancer le serveur
python app.py
