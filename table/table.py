import pandas as pd



def write_table(list_urls, threshold):
    f = open("crawled_webpages.txt", "w")
    for link in list_urls[:int(threshold)]:
        f.write(link)
        f.write("\n")
    f.close()



def generate_table(list_urls, threshold):
    
    write_table(list_urls, threshold)
    urls = pd.read_csv("crawled_webpages.txt", header = None)
    urls.columns = ['Links']
    urls.to_csv('links.csv', index = None)