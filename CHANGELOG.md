# Changelog

Ce changelog suit la méthode "keep a changelog" disponible ici: [https://keepachangelog.com/en/1.0.0/](https://keepachangelog.com/en/1.0.0/)


## [4] La GPU - Non livré

### Ajouté :

### Modifié :

### Corrigé :

## [3] - 2023.05.11

### Ajouté :
* Suivi des modifications d'un diagnostics et d'une demande de téléchargement
* Nouvelle page d'accueil présentant la trajectoire
* Nouvel onglet Trajectoire dans les tableaux de bords

### Modifié :
* Passage de Python 3.9 à 3.10 et Django 3.2 à 4.1
* Liste des diagnostics améliorées

### Corrigé :
* Couleur des cartes artificialisation (rouge) et consommation (bleu)
* Couleur du fond du graphique objectif 2031 dans l'export Word
* Autres corrections

## [2.5.2] - 2023.03.28

### Ajouté :
* Reporting dans Metabase


## [2.5.1] - 2023.03.20

### Ajouté :
* Nouvelle page d'accueil d'un diagnostic
* Export Excel des données d'un diagnostic
* Bouton "Exporter" dans l'ensemble des pages du tableau de bord
* Alerte lorsque des diagnostics word sont non-envoyés

### Modifié :
* Améliorations des titres et textes des rapports
* Mettre en oeuvre le Design Système France (DSFr) dans la page contact, connexion...
* Refonte des e-mails, migration vers SerndInBlue, mise en oeuvre des "templates"
* Uniformisation des boutons d'action autour des graphiques
* Fusionner la page consommation et la page consommation relative dans le tableau de bord

### corrigé:

## [2.4.0] - 2023.02.21

### Ajouté :
* Carte thématique consommation d'espace dans le bilan word
* Sélectionner un SCoT lors de la création d'un diagnostic

### Modifié :
* Réduction de la taille du header
* Utiliser le DSFR pour le bloc newsletter
* Améliorer le rapport "Découvrir l'OCS GE"
* Améliorer le rapport objectif 2031


## [2.3.4] - 2022.12.08

### corrigé:
- Corriger la page des statistiques en affichant le mois correcte

## [2.3.3] - 2022.12.02

### corrigé:
- Permettre l'envoi par e-mail des diagnostics sans voisins

## [2.3.2] - 2022.11.18

### corrigé:
- Corriger la taille des carte thématiques (revenir au plein écran)

## [2.3.1] - 2022.11.15

### corrigé:
- Corriger la taille de la carte intéractive (revenir au plein écran)

## [2.3.0] - 2022.11.14

Contenu de cette version : https://app.clickup.com/14136489/v/l/li/204778717

### Ajouté :
- Nouveau rapport : objectif 2031

### Modifié :
- Modification de l'intro des rapports synthèse et consommation.
- Masquer les tableaux de données dans les rapports

## [2.2.0] - 2022.11.09

Contenu de cette version : https://app.clickup.com/14136489/v/l/6-204672970-1

### Ajout :
- Choisir le taux d'artificialisation cible 2031 pour son territoire
- Test de l'utilisation des tuiles vecteurs
- Pour l'équipe (staff) : télécharger des statistiques sur l'usage de la plateforme
- Inscription à la newsletter
- Formulaire de contact

### Modifié :
- Modification du texte d'information en haut du rapport de consommation
- Simplifier la recherche d'une commune en séparant les termes de recherche selon l'espace (ainsi "Saint Laurent" fait ressortir tous les "Saint-Laurent")
- Mise à jour des données OCS GE du Gers avec la version de juin 2022
- Dans les rapports : désactivation des onglets utilisant les données OCS GE quand c'est un territoire non couvert
- Modification du texte d'introduction du rapport d'Artificialisation


## [2.1.3] - 2022.10.20

### Corrigé :
- Ajout d'un territoire de comparaison par un utilisateur
- Perte des territoires de comparaison initiaux à cause de la concurrence des traitements

## [2.1.2] - 2022.10.04

### Corrigé :
- Sélection et affichage d'un groupe de commune dans le rapport dédié

## [2.1.1] - 2022.09.29

### Corrigé :
- Téléchargement d'un diagnostic concernant un territoire de Gironde mais n'ayant pas d'OCS GE

## [2.1.0] - 2022.09.22

Non détaillé.

## [2.0.0] - livré

### Ajout :
- Génération de cartes au format PNG
- Utilisation d'un serveur d'export des graphiques Highcharts maison

### Modifié :
- Mise en oeuvre du [Design Système de l'état](https://www.systeme-de-design.gouv.fr/)

## [1.4.0] - 10.05.2022

### Ajout :
* Zones artificielles. Function de construction, affichage pour Gers et Arcachon dans la carte interactive.

### Modifié :
* Migration des buildpacks pour s'adapter aux montées de version de Scalingo

## [1.3.5] - 20.05.2022

### Ajout :
* Numéro de version de l'app visible dans le header de l'admin
* Commande pour calculer la zone artificielle grâce aux données de l'OCS GE
* Complétion du rapport de synthèse et utilisation par défaut lors de l'ouverture des rapports
* Commande de calcule des données des villes pour faciliter la construction des rapports

### Modifié :
* Ajout colonne et ligne total dans les tableaux de données
* Masquer le contenu du rapport si les données sont manquantes
* Unification des données OCSGE, OcsgeDiff, Zone artificielle et Zone construite
* Unification des endpoints pour les données de la carte interactive
* Unifier template des rapports couverture et usage
* Fusionner les tableaux couverture et usage

## [1.4.0] - 10.05.2022

### Ajout :
* Zones artificielles. Function de construction, affichage pour Gers et Arcachon dans la carte interactive.


## [1.3.4] - 10.05.2022

### Ajout :
* Données du Gers: OCS GE 2016 & 2019, OCS GE diff, zone construite 2016 & 2019
* Fonction de calcule des données d'artificialisation de chaque commune
* Rapport d'artificialisation

## [1.3.2] - 29.04.2022

### Ajouté
* Ajout de données dans la datasource : url et pie chart des déterminants

## [1.3.1] - 29.04.2022

### Bugs
* Obligatoir de désactivé puis activer le module django-templates-docx pour réussir à migrer la base de données


## [1.3.0] - 29.04.2022

### Ajouté
- Génération automatique du diagnostic word (sans les cartes)
- Chargement des données OCSGE du Gers

## Modifié
- Unification du stockage des données OCSGE et des couches différentielles et adaptation des données du bassin d'Arcachon


## [1.2.0] - 15.04.2022

Backlog de la version: [https://app.clickup.com/14136489/v/li/122274320/74368258?pr=20181273](https://app.clickup.com/14136489/v/li/122274320/74368258?pr=20181273)

### Ajouté
- Déselectionner toutes les communes d'un clic dans le graph de comparaison des communes
- Possibilité de faire des groupes de communes dans un diagnostic et rapport dédié
- Consommation relative dans le graph de comparaison des territoires
- Possibilité de "réclamer" un projet sans propriétaire
- (tech) paramétrage des graphs dans les views afin de pouvoir facilement les exporter
- (tech) ajout de bandit pour vérifier les dépendances et le code
- (tech) ajout de l'environnement "local" pour tester les scripts

### Modifié
* Montée de version Django vers 3.2.12
* Remplacement de app_parameter par django-app-parameter
* Nettoyage des scripts pour faciliter l'ajout de nouveau
* Redirigé vers la liste des diagnostics après connexion
* Réduction du temps de chargement du rapport consommation en optimisant les requêtes SQL
* Ajout d'une erreur lorsque le zip d'un shape n'est pas bon afin de ne pas enregistrer l'erreur dans Sentry
* Revue de l'affichage des infos dans la carte interactive
* Affichage des communes de toute la France dans la carte interactive

### Corrigé
- Erreur 500 lors d'un direct accès à l'étape 2 de création.

## [1.1.2] - 07.03.2022

### Corrigé
- Autoriser les tableaux de bords à afficher un diagnostic commençant en 2009
- Lors de la création d'un diagnostic, ajouter une exception à intercepter quand le territoire n'a pas été bien renseigné

## [1.1.1] - 28.02.2022

Objectif : hotfixes pour corriger les anomalies détectées dans Sentry.

### Corrigé
* Bug lorsqu'un utilisateur demande son bilan (https://app.clickup.com/t/221e9gt)
* Bug "IndexError" lors de l'affichage d'un rapport couverture ou usage (https://app.clickup.com/t/2579cnj)
* Bug lors de la création d'un diagnostic sans territoire (https://app.clickup.com/t/221fc7v)

## [1.1.0] - 2022-02-23

Objectif principale : rapport sur l'artificialisation

### Ajouté
- Demander son bilan et le recevoir par e-mail
- Log des erreurs dans Sentry (voir [le tableau de bord dédié](https://sentry.io/betagouv-f7/sparte))

### Modifié
- Changement des graphiques dans les rapports Couvertures et Usages

### Corrigé


## [1.0.0] - 2022-01-25

### Ajouté
- Log des requêtes entrantes pour s'assurer qu'elles sont en cours de traitement
- US 1.1 - Fonction "Plan" :
  * Ecrans d'administration pour les plans (inc. les emprises)
  * Publication de la route API pour obtenir les emprises d'un plan
  * Ecrans de manipulation des plans (CRUD) et traitement différé de l'import du fichier shape
  * Afficher la liste des plans dans la page de détail d'un projet
- US 5.3 - Ajouter les cartes de couverture des sols 2015 et 2018
- US 11.2 - ajouter une matrice de passage entre US x CS => consommation, est artificielle...
- US 2.1 - Afficher une page "profil" pour mettre à jour ses informations personnelles
- US 2.2 - Pouvoir se désinscrire
- Tests unitaires:
  * Projet
  * Utilisateur
  * Communes artificielles
- US 8.13 - ajout de FAQ administrable dans la partie documentation (https://app.clickup.com/t/1uwt65e)

### Modifié
- US 7.8 - Carte interactive: forte atténuation des bordures des polygons
- Bascule de la logique de chargement des geolayers vers javascript, suppression des templatetags
- US7.2 - Afin de faciliter la navigation mettre le projet "ouvert" dans la barre latéralle
  * Modification du thème
  * Ajout du projet ouvert dans la top barre
  * Affichage de la page d'accueil même en mode connecté
  * Possibilité de masquer le menu latéralle
- US 7.9 - Afficher les layers dans un ordre déterminé pour faciliter la lecture
- US 10.1 - restructurer les données OCSGE pour inclure les millésimes 2013, 2016 et 2019
- Augmenter la période d'un projet pour aller jusqu'en 2020 (https://app.clickup.com/t/1uhcpk3)
- US 8.11 - refondre la page d'accueil (https://app.clickup.com/t/1p89n5g)

### Corrigé
- Affectation de la date & heure lors de l'import d'une emprise
- Masquer des layers lors de l'ouverture de la carte interactive

## [0.1.0] - 2021-06-20

Initialisation de ce changelog.

### Ajouté
- US 5.7 - charger les données issues de l'OCSGE
- US 7.4 - Dans la carte interactive, ajouter dans les propriétés la traduction du code couverture et usage
- US. 3.4 - Refaire le graphe avec les données complètes (OCSGE)
- US 3.2 - Sur le même modèle que l'artificialisation - couverture (treemap) ajouter l'usage
- US 3.6 - Dans l'onglet consommation > n'afficher que les années qui sont incluses dans la période d'analyse

### Modifié
- US 7.5 - Simplifier l'affichage en modifiant le layer "emprise du projet" pour ne laisser qu'une frontière sans couleur de fond
- US 2.3 - Utiliser des libellés français dans la page d'inscription
- US 3.6.1 - Dans l'onglet consommation > enlever tableau taux, ajouter colonne progression...
- US 3.3 - Sur le graphe consommation > changer la légende "utilisé" par "consommé"
- US 8.8 - Home projet > franciser
