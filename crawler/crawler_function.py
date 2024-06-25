"""Module contenant la fonction de crawl principale"""

import networkx as nx
from crawler.Robots import Robots
from IHM.visualisation import graphe_function


class Crawler():

    def crawl(self, list_urls: list, starting_index: int, threshold: int, graphique: nx.Graph):
        """Fonction de crawl principale"""
        while graphique.number_of_nodes() < threshold and starting_index < len(list_urls):

            url_request = list_urls[starting_index]
            robots_file = Robots(url_request)
            result = robots_file.request_robots()
            url_list = clean_function.clean_list(result)
            base_url = clean_function.clean_url(url_request)
            for url in url_list:
                graphe_function.set_node(graphique, url)
                graphe_function.set_edge(graphique, base_url, url)

            starting_index += 1
