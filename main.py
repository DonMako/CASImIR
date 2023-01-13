from urllib import parse
from urllib import request
from urllib import robotparser
from bs4 import BeautifulSoup as BS



# La fonction principale, permettant de boucler les recherches sur les URL, afin d'atteindre le seuil d'URL demandé par l'utilisateur.
def main(url, threshold):

    # On stocke les urls des pages déjà croisées, pour ne pas stocker 
    liste_urls = []
    liste_urls.append(url)

    # L'indice de départ, afin de ne prendre en URL d'exploration que des URL pas encore testés.
    starting_index = 0

    # Les conditions d'arrêt du programme : avoir atteint le seuil d'URL demandé par l'utilisateur, ou ne plus trouver de liens à requêter.
    while len(liste_urls) < int(threshold) or starting_index < len(liste_urls):

        result = requeter(liste_urls, starting_index)
        for link in result:
            if link not in liste_urls:
                liste_urls.append(link)
        starting_index += 1
        
    f = open("crawled_webpages.txt", "w")
    for link in liste_urls[:int(threshold)]:
        f.write(link)
        f.write("\n")
    f.close()



# La fonction permettant de trouver d'autres pages à explorer à partir d'un URL, en analysant les balises dudit URL.
def requeter(liste_urls, index):

    urls_found = []
    
    try:
        url_crawled = liste_urls[index]
        url_request = request.urlopen(url_crawled)
        soup = BS(url_request, 'html.parser')
    
        # Pour chaque lien de page trouvé, on vérifie que le lien est un URL autorisé à être crawlé.
        # Si le lien est valide, on l'ajoute dans les liens trouvés.
        for link in soup.find_all('a'):
            ref = link.get('href')
            if ref in analyse_robot(url_crawled):
                urls_found.append()

    except:
        pass

    return urls_found



# La fonction permettant d'analyser le fichier robot.txt d'une page, afin de récupérer les liens qu'elle contient qui peuvent être crawlés.
def analyse_robot(url):

    parser = robotparser.RobotFileParser()
    parser.set_url(parse.urljoin(url, 'robots.txt'))
    
    # On initialise la liste des url qui peuvent être crawlés
    url_allowed = []

    # On fait un try/except au cas où la page web n'a pas de robots.txt
    try:
        parser.read()
        for line in parser:
            if line.startswith('Allow'):
                url_allowed.append(line.split(': ')[1].split(' ')[0]) 
    except:
        pass
    
    return(url_allowed)



url_user = input("Enter the starting url : ")
threshold_user = input("Enter the threshold desired : ")
main(url_user, threshold_user)