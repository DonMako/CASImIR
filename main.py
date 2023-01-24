from crawler.crawler import crawl
from visualisation.table import generate_table
import networkx as nx



def crawler():

    url = input("Enter the starting url : ")
    threshold = input("Enter the threshold desired : ")

    list_urls = []
    list_urls.append(url)

    starting_index = 0
    G = nx.Graph()

    crawl(list_urls, starting_index, threshold, G)
        
    f = open("crawled_webpages.txt", "w")
    for link in list_urls[:int(threshold)]:
        f.write(link)
        f.write("\n")
    f.close()

    generate_table()



if __name__ == '__main__':
    crawler()
