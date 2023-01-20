import pandas as pd



def generate_table():
    
    urls = pd.read_csv("crawled_webpages.txt", header = None)
    urls.columns = ['Links']
    urls.to_csv('links.csv', index = None)