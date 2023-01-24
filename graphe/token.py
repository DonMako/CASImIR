from urllib import request
from bs4 import BeautifulSoup as BS



def get_title(url):

    title = " "
    
    try:
        url_request = request.urlopen(url)
        soup = BS(url_request, 'html.parser')
        title = soup.title.text

    except:
        pass

    return title.split(" ")