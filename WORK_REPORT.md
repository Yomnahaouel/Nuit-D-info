Document de travail — Nuit-D-info
================================

Résumé
------
- **Projet**: `Nuit-D-info` — application Django située à la racine du workspace.
- **But du document**: Décrire le travail effectué, l'état actuel du projet, comment démarrer l'application localement, et fournir recommandations et prochaines étapes.

Objectifs
---------
- **But principal**: Fournir une application web Django fonctionnelle et reproductible en local.
- **Livrables**: code source Django (application `main`), fichier `requirements.txt`, base SQLite (`db.sqlite3`), configuration du projet (`NuitDInfo`).

Travail réalisé
----------------
- **Structure du projet**: Présence de `manage.py`, d'une application `main/` et d'un package de configuration `NuitDInfo/`.
- **Templates**: page principale dans `main/templates/index.html`.
- **Base de données locale**: fichier `db.sqlite3` fourni pour le développement local.
- **Dépendances**: gérées via `requirements.txt` (voir section suivante).

Fichiers importants
-------------------
- **Entrée principale**: `manage.py`
- **Configuration Django**: `NuitDInfo/settings.py`, `NuitDInfo/urls.py`, `NuitDInfo/wsgi.py`, `NuitDInfo/asgi.py`
- **Application**: `main/models.py`, `main/views.py`, `main/admin.py`, `main/templates/index.html`
- **Dépendances**: `requirements.txt`
- **Base de données locale**: `db.sqlite3`

Dépendances (contenu de `requirements.txt`)
-----------------------------------------
- `asgiref==3.11.0`
- `Django==6.0`
- `sqlparse==0.5.4`
- `tzdata==2025.2`
- `gunicorn`

Installation et exécution (Windows PowerShell)
---------------------------------------------
- **Pré-requis**: Python 3.10+ recommandé.
- **Étapes**:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

- **Accès**: Ouvrir `http://127.0.0.1:8000/` dans un navigateur.

Tests
-----
- **État**: Un fichier `main/tests.py` existe ; vérifier son contenu pour tests existants.
- **Exécution**:

```powershell
.\.venv\Scripts\Activate.ps1
python manage.py test
```

Problèmes connus / remarques
---------------------------
- **Version de Django**: `Django==6.0` — vérifier la compatibilité avec la version de Python utilisée.
- **Base de données**: `db.sqlite3` est prévue pour le développement uniquement ; ne pas l'utiliser en production.
- **gunicorn**: présent dans `requirements.txt` mais utile principalement pour le déploiement Unix/WSGI.

Recommandations et prochaines étapes
-----------------------------------
- **Documentation**: Ajouter un `README.md` ou `WORK_REPORT.md` (ce fichier) à la racine — déjà créé.
- **Tests**: Écrire des tests unitaires et d'intégration dans `main/tests.py` et les automatiser.
- **CI/CD**: Ajouter un pipeline (ex. GitHub Actions) pour exécuter les tests et déploiement.
- **Sécurité**: Ne pas committer de `SECRET_KEY` en clair ; utiliser des variables d'environnement.
- **Production**: Remplacer SQLite par PostgreSQL, configurer `ALLOWED_HOSTS`, HTTPS, et gestion des fichiers statiques.

Auteur / Contact
-----------------
- **Préparé par**: Rapport généré à la demande.
- **Fichier**: `WORK_REPORT.md` créé à la racine du projet.

Souhaitez-vous que je fasse également un commit et un `git push` pour ajouter ce fichier au repo ?
