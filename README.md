# Crawler

## Description du programme
À partir d'une URL d'entrée que l'utilisateur renseigne, le crawler trouve d'autres pages à explorer en analysant les balises de liens trouvées dans les documents précédemment explorés.

Le programme se termine lorsque le crawler arrive à la limite d'urls à trouver (limite indiquée par l'utilisateur), ou s'il ne trouve plus de liens à explorer.

Une fois terminé, le programme écrit dans le fichier "crawled_webpages.txt" toutes les urls trouvées.

## Lancer le programme

```
git clone https://github.com/DonMako/crawler.git
cd crawler
pip install -r requirements.txt
python3 main.py
```

## Auteur
Lucas MACAUX