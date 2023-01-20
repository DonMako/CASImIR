# Cr@wler

## Qu'est-ce que Cr@wler ?

Un crawler, appelé également « robot d'indexation », est un logiciel qui a pour principale mission d'explorer le Web afin d'analyser le contenu des documents visités et les stocker de manière organisée dans un index.

Cr@wler est un crawler web simple, ayant pour objectif de récupérer des URL à partir d'un URL de départ, réalisé dans un contexte de familiarisation avec l'indexation web. 

## Description du programme
À partir d'un URL d'entrée que l'utilisateur renseigne, Cr@wler trouve d'autres pages à explorer en commençant par analyser le fichier *robots.txt* de l'URL requêté.

Si ce fichier n'existe pas, ou s'il ne contient pas de sitemaps permettant de récupérer facilement des URLS, Cr@wler analyse le code HTML de l'URL requêté et récupère les balises de liens trouvées dans ledit code.

Cr@wler prend ensuite l'un des URLs récupéré et recommence son analyse, jusqu'à la fin du programme.

Le programme se termine lorsque Cr@wler arrive à la limite d'URLs à trouver (limite renseignée par l'utilisateur), ou s'il ne trouve plus de liens à explorer.

Une fois terminé, le programme écrit dans un fichier *crawled_webpages.txt* tous les urls trouvées.

## Lancer le programme

```
git clone https://github.com/DonMako/crawler.git
cd crawler
pip install -r requirements.txt
python3 main.py
```

## To-do list
Dans une volonté de prolonger le travail sur Cr@wler, de nouvelles fonctionnalités sont en cours d'écriture:

* la création d'un mini-serveur local permettant d'accéder:
    + à la liste des URLs crawlés, et de téléchager ladite liste sous différents formats (xls, csv)
    + à un graphe orienté montrant visuellement les liens entre les URLs crawlés
