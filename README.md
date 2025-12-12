#  Projet Photos Vacances - Documentation & Guide de Démarrage

Projet versionnage &amp; Intégration continue
Tom Cabaye - Jules Leroux - Mathis Philippe

## 1. Manière de travailler

Notre méthode de travail s'articule autour d'une stratégie de versionnage commune et simple. Nous utilisons le Git Flow :

- main : C'est la branche de production, qui ne reçoit que du code stable et testé. (il y a eu une erreur de merge ici qui a été corrigé par la suite).

- develop : C'est la branche de développement en commun. Toutes les fonctionnalités sont fusionnées, intégrées et testées ici.

- feature/* : Ces branches permettent de développer des fonctionnalités de manière indépendante.

Dès qu'une tâche est terminée sur une branche feature, elle est fusionnée dans develop. Lorsque la version est jugée stable, develop est elle-même fusionnée dans main.

Pour assurer la traçabilité et l'historique structuré , chaque message de commit suit la convention Angular , respectant le format type(portée): résumé. Des types comme feat (nouvelle fonctionnalité) sont utilisés. Avant de commencer toute modification et avant de pousser le code, nous nous assurons toujours de récupérer les dernières modifications du dépôt distant avec git pull ou git fetch, le dépôt distant étant nécessaire à la partie collaborative. Enfin, un fichier .gitignore a été mis en place pour ignorer certains fichiers.


## 2. Installation et Lancement du Projet

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
