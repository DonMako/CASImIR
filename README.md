# Cr@wleye

## Qu'est-ce que Cr@wleye ?

Un crawler, appelé également « robot d'indexation », est un logiciel qui a généralement pour principale mission d'explorer le Web afin de collecter les ressources (pages Web, images, vidéos, etc.), pour permettre à un moteur de recherche de les indexer.

Cr@wleye est un simili crawler web utilisant l'IA et ayant objectif de récupérer des images correspondant à un mot-clé, à partir d'un URL de départ.

## Description du programme
À partir d'un URL d'entrée que l'utilisateur renseigne, Cr@wleye trouve d'autres pages à explorer en commençant par analyser le fichier *robots.txt* de l'URL requêté.

Si ce fichier n'existe pas, ou s'il ne contient pas de sitemaps permettant de récupérer facilement des URLs, Cr@wleye analyse le code HTML de l'URL requêté et récupère les balises de liens trouvées dans ledit code. Cr@wleye récupère également les images contenues dans le code HTML.

Cr@wleye prend ensuite l'un des URLs récupéré et recommence à récupérer des images, jusqu'à la fin du programme.
Ce dernier se termine lorsque Cr@wleye ne trouve plus de liens à explorer.

Une fois terminé, le programme utilise de l'IA afin de détecter dans les images récupérées la présence (ou non) de l'objet renseigné par l'utilisateur.

## Lancer le programme

```
git clone https://github.com/DonMako/crawleye.git
cd crawleye
pip install -r requirements.txt
python3 main.py
```

## To-do list
Dans une volonté de prolonger le travail sur Cr@wleye :

* une version fonctionnelle du crawler !!
* la création d'une webapp permettant d'accéder:
    + à un formulaire permettant de lancer le crawler
    + de téléchager un dossier contenant l'ensemble des images crawlées contenant l'objet renseigné par l'utilisateur
* le multi-threading du crawler afin d'accélérer son efficacité
