from bs4 import BeautifulSoup as BS
from urllib import request
import validators



def request_function(url: str):

    urls_found = []
    
    try:
        url_request = request.urlopen(url)
        soup = BS(url_request, 'html.parser')
        for link in soup.find_all('a'):
            ref = link.get('href')
            if validators.url(ref):
                urls_found.append(ref)

    except:
        pass

    return urls_found
