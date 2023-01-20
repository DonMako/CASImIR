from urllib import request
from bs4 import BeautifulSoup as BS



def request_function(url):

    urls_found = []
    
    try:
        url_request = request.urlopen(url)
        soup = BS(url_request, 'html.parser')
    
        for link in soup.find_all('a'):
            ref = link.get('href')
            urls_found.append(ref)

    except:
        pass

    return urls_found