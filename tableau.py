import pandas as pd



def generate_tableau():
    
    urls = pd.read_csv("crawled_webpages.txt", header = None)
    urls.columns = ['Links']
    urls.to_csv('links.csv', index = None)