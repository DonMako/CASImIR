from bs4 import BeautifulSoup as BS
from nltk.corpus import stopwords
from urllib import request



def delete_stopwords(text):
    
    clean_words = []
    for word in text:
        if word not in stopwords.words('french'):
            clean_words.append(word)
    return clean_words



def tokenise(url):

    title = " "
    
    try:
        url_request = request.urlopen(url)
        soup = BS(url_request, 'html.parser')
        title = soup.title.text
    except:
        pass

    return delete_stopwords(title.split(" "))



def tokenise_list(list):

    list_tokens = []
    for url in list:
        list_tokens.append(tokenise(url))
    return list_tokens
