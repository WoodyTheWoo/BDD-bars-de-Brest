# Base de donn�es des bars de Brest

Ce repo regroupe les fichiers Python utilis�s pour la cr�ation de la base de donn�es.
J'ai utilis� l'API Google Maps pour construire un fichier JSON regroupant les lieux �tant caract�ris�s comme "bar" par google.
Pour ensuite les int�grer dans une base de donn�es SQlite.

## Base de donn�es

La BDD est au format SQlite et contient les champs suivants :
 - id : Id de l'entr�e, PK
 - name : Nom du bar, NN
 - address : Adresse longue du bar (<num�ro> <rue>, <CP> <ville>, <pays>)
 - lat : coordonn�e GPS latitude
 - lng : coordonn�e GPS longitude
 - phone : num�ro de t�l�phone au format local (02 98 ....)
 - website : adresse du site web
 - gmaps_id : id pour l'utilisation avec GMap
 - icon_url : url de l'ic�ne utilis�e par GMap
 - types : mots cl�s utilis�s par GMap

