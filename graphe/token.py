from urllib import request
from bs4 import BeautifulSoup as BS
import spacy



def tokenise(url):

    title = " "
    
    try:
        url_request = request.urlopen(url)
        soup = BS(url_request, 'html.parser')
        nlp = spacy.load("fr_core_news_sm")
        title = nlp(soup.title.text)
    except:
        pass

    return title.split(" ")

nlp = spacy.load("fr_core_news_sm")
print(nlp("Bonjour le chat"))

def tokenise_list(list):

    list_tokens = []
    for url in list:
        list_tokens.append(tokenise(url))
    return list_tokens