# Base de données des bars de Brest

Ce repo regroupe les fichiers Python utilisés pour la création de la base de données.
J'ai utilisé l'API Google Maps pour construire un fichier JSON regroupant les lieux étant caractérisés comme "bar" par google.
Pour ensuite les intégrer dans une base de données SQlite.

## Base de données

La BDD est au format SQlite et contient les champs suivants :
 - id : Id de l'entrée, Primary Key
 - name : Nom du bar, Not Null
 - address : Adresse longue du bar (<numéro> <rue>, <CP> <ville>, <pays>)
 - lat : coordonnée GPS latitude
 - lng : coordonnée GPS longitude
 - phone : numéro de téléphone au format local (02 98 ....)
 - website : adresse du site web
 - gmaps_id : id pour l'utilisation avec GMap
 - icon_url : url de l'icône utilisée par GMap
 - types : mots clés utilisés par GMap

## Fichier
Extraire le fichier suivant :
https://github.com/WoodyTheWoo/BDD-bars-de-Brest/releases/download/v0.5/bars.zip
