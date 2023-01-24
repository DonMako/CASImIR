import pandas as pd
import json



def write_table(list_urls, threshold):
    
    f = open("/documents/crawled_webpages.txt", "w")
    for link in list_urls[:int(threshold)]:
        f.write(link)
        f.write("\n")
    f.close()



def generate_CSV(list_urls, threshold):
    
    write_table(list_urls, threshold)
    urls = pd.read_csv("crawled_webpages.txt", header = None)
    urls.columns = ['Links']
    urls.to_csv('links.csv', index = None)



def generate_JSON(list_urls, threshold):

    write_table(list_urls, threshold)
    with open('crawled_webpages.txt') as file_handle:
        file_content = file_handle.read()
    
    my_dict = {}
    my_dict["Links"] = []
    for line in file_content.split('\n'):
        my_dict["Links"].append(line)

    with open("links.json", "w") as f:
        json.dump(line, f)