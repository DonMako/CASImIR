import urllib
from urllib import *
from bs4 import BeautifulSoup as BS

def main(url, threshold):

    # On stocke les urls des pages déjà croisées, pour ne pas stocker 
    liste_urls = []
    liste_urls.append(url)

    # L'indice de départ, afin de ne prendre en url d'exploration que des url pas encore testés.
    starting_index = 0

    while len(liste_urls) < threshold or starting_index > len(liste_urls):

        result = requeter(liste_urls, starting_index)
        for link in result:
            if link not in liste_urls:
                liste_urls.append(link)
        starting_index += 1
        
    f = open("crawled_webpages.txt", "w")
    for link in liste_urls[:threshold]:
        f.write(link)
        f.write("\n")
    f.close()



# La fonction permettant de trouver d'autres pages à explorer en analysant les balises de liens trouvées 
def requeter(liste_urls, index):

    urls_found = []
    
    # On crée un try/except afin de ne pas crawler un site web qui l’interdit.
    try:
        url_request = urllib.request.urlopen(liste_urls[index])
        soup = BS(url_request, 'html.parser')
    
        # Pour chaque lien de page trouvé, on vérifie que le lien est un URL valide.
        # Si le lien est valide, on l'ajoute dans les liens trouvés.
        for link in soup.find_all('a'):
            #parsed_url = urllib.parse.urlparse.urlparse(link)
            #if bool(parsed_url.scheme):
            #    urls_found.append(link.get('href'))
            urls_found.append(link.get('href'))
            
    except:
        pass

    return urls_found



main("https://ensai.fr/", 15)