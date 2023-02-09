from crawler import clean_function, robots
import networkx as nx
from visualisation import graphe_function



def crawl(list_urls: list, starting_index: int, threshold: int, graphique: nx.Graph):

    while graphique.number_of_nodes() < threshold and starting_index < len(list_urls):

        url_request = list_urls[starting_index]
        result = robots.request_robots(url_request)
        url_list = clean_function.clean_list(result)
        base_url = clean_function.clean_url(url_request)
        for url in url_list:
            graphe_function.set_node(graphique, url)
            graphe_function.set_edge(graphique, base_url, url)    

        starting_index += 1
