# CASImIR

## Qu'est-ce que CASImIR ?

Casimir est un dinosaure orange, à pois jaunes et rouges, de la famille des _Casimirus_, souvent surnommé "l'ami des enfants".

Un crawler, appelé également « robot d'indexation », est un logiciel qui a généralement pour principale mission d'explorer le Web afin de collecter les ressources (pages Web, images, vidéos, etc.), pour permettre à un moteur de recherche de les indexer.

---

Crawler Avec Scrapping d'IMages Intelligent comme Rempart (CASImIR) est un simili crawler web utilisant l'IA et ayant pour objectif de détecter des images pédo-pornographique sur des sites webs, à partir d'un URL de départ.

## Description du programme

À partir d'un URL d'entrée que l'utilisateur renseigne, CASImIR trouve d'autres pages à explorer en scrappant le code source de l'URL renseignée.
CASImIR prodite de ce scrap pour récupérer l'URL des images contenues dans le code HTML de la page.

CASIMUIR recommence ensuite l'opération sur l'une des URLs récupérées, jusqu'à atteindre la limite d'URLs à scrapper indiquée par l'utilisateur, ou lorsqu'il ne trouve plus de liens à explorer.

Une fois terminé, CASImIR utilise un modèle d'intelligence artificelle afin de détecter dans les images récupérées la présence (ou non) de l'objet renseigné par l'utilisateur.

## Lancer le programme

```
git clone https://github.com/DonMako/casimir.git
cd casimir
pip install -r requirements.txt
python3 main.py
```

## To-do list
* une version fonctionnelle du logiciel !!
* un signalement automatique auprès des autorités compétentes des sites webs hébergeant des images pédo-pornographiques
* la création d'un micro IHM HTML contenant:
    + un champ texte pour renseigner l'URL de départ
    + un champ texte pour renseigner le nombre limite d'URLs que CASImIR doit scrapper
    + un bouton afin de lancer le logiciel
    + un bouton pour télécharger un dossier compressé contenant l'ensemble des images crawlées contenant de la pédo-pornographie
* la parallélisation du scrapper afin d'accélérer son efficacité
* un champ texte dans l'IHM pour mettre une limite sur la fiabilité que le modèle d'IA accorde à sa détection
