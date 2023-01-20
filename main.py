from visualisation.graphe import add_edge
from crawler.robots import request_robots
from visualisation.table import generate_table
import networkx as nx
import validators



def crawler():

    url = input("Enter the starting url : ")
    threshold = input("Enter the threshold desired : ")

    list_urls = []
    list_urls.append(url)

    starting_index = 0

    G = nx.Graph()

    while len(list_urls) < int(threshold) and starting_index < len(list_urls):

        result = request_robots(list_urls[starting_index])
        for link in result:
            if link not in list_urls and validators.url(str(link)):
                list_urls.append(link)
                add_edge(G, list_urls[starting_index], link)

        starting_index += 1
        
    f = open("crawled_webpages.txt", "w")
    for link in list_urls[:int(threshold)]:
        f.write(link)
        f.write("\n")
    f.close()

    generate_table()



if __name__ == '__main__':
    crawler()
