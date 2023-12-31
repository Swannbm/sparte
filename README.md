**S**ervice de **P**ortrait de l’**AR**tificialisation des **TE**rritoires
==========================================================================

# SPARTE

Le Service de Portrait de l’ARtificialisation des TErritoires (ou SPARTE) est une plateforme qui aide les collectivité à mesurer l'artificialisation de leurs sols et ainsi se conformer aux nouvelles lois.

## Installation

1. Cloner le répository git `git clone git@github.com:MTES-MCT/sparte.git` puis aller dans le dossier `cd sparte`
2. Installer les dépendances avec pipenv `pipenv install --dev`
3. Créer un fichier .env avec (à compléter avec vos crédentials, voir ci-dessous...)
4. Démarrer les bases de données `docker-compose up -d`
5. Basculer dans l'environnement virtuel `pipenv shell`
6. Migration initiale `python manage.py migrate`
7. Créer un super utilisateur `python manage.py createsuperuser`
8. Démarrer le serveur `python manage.py runserver 0.0.0.0:8080`
9. Ouvrer la home page [http://localhost:8080/](http://localhost:8080/)
10. Copier les fichiers de données OCS GE et Cérema... sur votre bucket AWS
11. Lancer l'installation des données `python scripts/cmd.py --env local rebuild`

## Frontend
1. Installer les dépendances front `npm install`
2. Lancer le build du bundle `npm run build:dev` ou `npm run build:prod` (Génère un nouveau bundle à chaque mise à jour du fichier ./assets/scripts/index.js)

### Variables d'environnement

Pour une installation locale, ces valeurs doivent être dans le fichier .env à la racine du projet. Pour le déploiement sur scalingo, ces variables sont à ajouter dans la section "Environnement" du container.

| Nom | description | valeur locale |
|-----|-------------|---------------|
| ALERT_DIAG_MEDIUM | Comment envoyer les alertes des diagnostics bloqués: mattermost, email, both | |
| ALERT_DIAG_EMAIL_RECIPIENTS | Liste des adresses e-mails auxuqelles envoyées les alertes diagnostics bloqués | 127.0.0.1,localhost |
| ALERT_DIAG_MATTERMOST_RECIPIENTS | channel (~sparte) ou personne (@swann) à qui envoyer un message direct de diagnostics bloqués | 127.0.0.1,localhost |
| ALLOWED_HOSTS | urls qui peuvent se connecter au site web | 127.0.0.1,localhost |
| API_KEY_SENDINBLUE | Clé api de sendinblue | |
| AWS_ACCESS_KEY_ID | compte AWS pour stocker les données |  |
| AWS_LOCATION | prefix pour ne pas avoir de collisions entre les instances de l'app | local |
| AWS_S3_REGION_NAME | région de AWS | eu-west-3 |
| AWS_SECRET_ACCESS_KEY | secret pour se connecter à AWS |  |
| AWS_STORAGE_BUCKET_NAME | nom du bucket de stockage | sparte-staging |
| CELERY_BROKER_URL | chaîne pour se connecter à redis | redis://127.0.0.1:6379/0 |
| CELERY_RESULT_BACKEND | chaîne pour se connecter à redis | redis://127.0.0.1:6379/0 |
| DATABASE_URL | chaîne pour se connecter à la base de données Postgresql + gis | postgis://postgres:postgres@127.0.0.1:54321/postgres |
| DEBUG | activer ou non les messages détaillés d'erreur | 1 |
| DEBUG_TOOLBAR | activer la barre de debug de Django | 1 |
| DEFAULT_FROM_EMAIL |  | swann.bouviermuller@gmail.com |
| DOMAIN_URL | l'url sur laquelle est branchée l'application | http://localhost:8080/ |
| EMAIL_ENGINE | indique à l'application le backend à utiliser pour envoyer les e-mails. 2 choix disponibles : sendinblue, local | local |
| ENVIRONMENT | indique sur quel environnement est exécuté l'app. Choix possibles: local, staging, prod | local |
| HIGHCHART_SERVER | ulr pour accéder au serveur générant des images à partir de paramètres Highcharts | https://highcharts-export.osc-fr1.scalingo.io |
| MATTERMOST_WEBHOOK | Webhook personnel pour envoyer des messages dans Mattermost | https://mattermost.incubateur.net/hooks/uak581f8bidyxp5td67rurj5sh |
| MATOMO_ACTIVATE | Détermine si des infos doivent être envoyé à Matomo | 0 |
| MATOMO_TOKEN | Token pour envoyer les données à Matomo |  |
| SECRET | salt pour django | |
| USE_SRI | Active l'utilisation des SRI même lorsque debug = 1 | 1 |
| USE_CSP | Active l'utilisation des CSP même lorsque debug = 1 | 1 |

Variables d'environnement spécifique à Scalingo. Voir les valeurs sur Scalingo.

| Nom | description |
|-----|-------------|
| DISABLE_COLLECTSTATIC | Requis pour déployer correctement les buildpacks |
| GDAL_DATA | requis pour le buildpack qui install GeoDjango |
| LD_LIBRARY_PATH | requis pour le buildpack qui install GeoDjango |
| PROJ_LIB | requis pour le buildpack qui install GeoDjango |
| SCALINGO_POSTGRESQL_URL | Ajouté lorsque l'addon postgres est activé |
| SCALINGO_REDIS_URL | Ajouté lorsque l'addon redis est activé |


## Before commiting

Vérifier la couverture des TU: `coverage run -m pytest && coverage report -m`

Vérifier que le formatage est bon: `flake8`

Si vous souhaitez bypasser pre-commit hook (usefull pour ajouter des fichiers shapes sans les modifiers):
```
git commit --no-verify
```

## Get production DB

Sometimes, you need to fetch and install a Scalingo DB backup.

1. Fetch backup from scalingo app > ressources > pg dashboard > backup, download last backup (eg. 20220830000404_sparte_1396.tar.gz)
2. Uncompress `tar -xf 20220830000404_sparte_1396.tar.gz`
3. restore `pg_restore --clean --if-exists --no-owner --no-privileges --no-comments --dbname postgres://postgres:postgres@127.0.0.1:5432/postgres 20220830000404_sparte_1396.pgsql`

## Update OCS GE

The process is not stable yet. Use it with caution.

1. Download shape files from IGN's website [https://geoservices.ign.fr](https://geoservices.ign.fr) "ACCUEIL > CATALOGUE > OCS GE"
2. Extract shape files and zip them by name, remove anysubfolder, the zip should contain only files
3. Name zip file accordingly to expected name in [public_data/management/commands/load_ocsge.py](public_data/management/commands/load_ocsge.py). If you want to update 2016 Gers millesime, name it accordingly to what you will find in class **GersOcsge2016** and the property **shape_file_path** (which is gers_ocsge_2016.zip when writhing those lines)
4. Upload the zip in the bucket, in data folder.
5. Trigger the loading with the command `python scripts/cmd.py --env prod load-ocsge --item .....`, replace ... by the item you want to load (following previous example it's `python scripts/cmd.py --env local load-ocsge --item GersOcsge2016`). Obviously test it in staging first.
6. Update all precalculated data: build_commune_data, build_artificial_area, set_density
7. Update official data origin in [gitbook](https://app.gitbook.com/o/-MMQU-ngAOgQAqCm4mf3/s/OgEtEJQsOvgZrMPdWEIo/)
8. Update admin's [Départements](https://sparte.beta.gouv.fr/admin/public_data/departement/) if new OCS GE has been added

Example, update Gers OCS GE with 2022-06 data:
```bash
export ENV='local'
python scripts/cmd.py --env $ENV load-ocsge --item GersOcsge2016 && \
python scripts/cmd.py --env $ENV load-ocsge --item GersOcsge2019 && \
python scripts/cmd.py --env $ENV load-ocsge --item GersZoneConstruite2016 && \
python scripts/cmd.py --env $ENV load-ocsge --item GersZoneConstruite2019 && \
python scripts/cmd.py --env $ENV load-ocsge --item GersOcsgeDiff && \
python scripts/cmd.py --env $ENV run 'python manage.py build_commune_data --departement Gers' && \
python scripts/cmd.py --env $ENV run 'python manage.py build_artificial_area --departement Gers' && \
python scripts/cmd.py --env $ENV run 'python manage.py set_density --reset --departement Gers'
```

MEP 4.0

- Charger les zones urbaines du GERS : ./manage.py import_gpu --dept 32

