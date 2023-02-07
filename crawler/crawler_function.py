from robots import *
from graphe import graphe_function, token_function


def crawl(list_urls, starting_index, threshold, graphique):

    while len(list_urls) < int(threshold) and starting_index < len(list_urls):

        url_request = list_urls[starting_index]
        result = request_robots(url_request)
        tokens_result = token_function.tokenise_list(result)
        tokens_request = token_function.tokenise(url_request)
        for list_token in tokens_result:
            for token in list_token:
                graphe_function.add_node(graphique, token)
                for token_init in tokens_request:
                    graphe_function.add_edge(graphique, token_init, token)

        starting_index += 1
