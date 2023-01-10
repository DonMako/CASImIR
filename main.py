import urllib
from urllib import request
from urllib import robotparser

# On initialise le nombre d'urls trouvés, car une des conditions d'arrêt est 50 urls trouvés.
nb_urls_found = 0
url = "https://ensai.fr/"


ensai = urllib.request.urlopen(url)
robot = urllib.robotparser.RobotFileParser(url)

print(robot)