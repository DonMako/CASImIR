# La fonction pour requêter le robots.txt d'un URL.



from urllib import parse
from urllib import robotparser
from requete import requeter



def requeter_robot(url):
    
    o = parse.urlparse(url)
    base_url = "https://" + str(o.hostname)

    urls_allowed =[]

    # On fait un try/else au cas où l'URL requêté n'a pas de robots.txt.
    try:
        parser = robotparser.RobotFileParser()
        parser.set_url(base_url)
        parser.read()
        sitemaps = parser.site_maps()

        if sitemaps != None:
            urls_allowed = sitemaps
        
        else:
            # Si le robots.txt ne contient pas de sitemaps nous permettant de récupérer des URL,
            # on requête les URL en crawlant directement le code HTML de l'URL requêté.
            urls_allowed = requeter(url)

    except:
        urls_allowed = requeter(url)

    return urls_allowed