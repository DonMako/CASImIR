from crawler.robots import request_robots
from graphe.graphe import add_edge, add_node
from graphe.token import tokenise_list, tokenise
from visualisation.table import generate_table
import networkx as nx



def crawler():

    url = input("Enter the starting url : ")
    threshold = input("Enter the threshold desired : ")

    list_urls = []
    list_urls.append(url)

    starting_index = 0
    G = nx.Graph()

    while len(list_urls) < int(threshold) and starting_index < len(list_urls):

        url_request = list_urls[starting_index]
        result = request_robots(url_request)
        tokens_result = tokenise_list(result)
        tokens_request = tokenise(url_request)
        for list_token in tokens_result:
            for token in list_token:
                add_node(G, token)
                for token_init in tokens_request:
                    add_edge(G, token_init, token)

        starting_index += 1
        
    f = open("crawled_webpages.txt", "w")
    for link in list_urls[:int(threshold)]:
        f.write(link)
        f.write("\n")
    f.close()

    generate_table()



if __name__ == '__main__':
    crawler()
