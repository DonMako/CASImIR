from urllib import request
from bs4 import BeautifulSoup as BS



def tokenise(url):

    title = " "
    
    try:
        url_request = request.urlopen(url)
        soup = BS(url_request, 'html.parser')
        title = soup.title.text

    except:
        pass

    return title.split(" ")


def tokenise_list(list):

    list_tokens = []
    for url in list:
        list_tokens.append(tokenise(url))
    return list_tokens