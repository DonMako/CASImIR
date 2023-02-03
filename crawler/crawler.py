from robots import request_robots
from graphe.graphe import add_edge, add_node
from graphe.token import tokenise_list, tokenise


def crawl(list_urls, starting_index, threshold, graphe):

    while len(list_urls) < int(threshold) and starting_index < len(list_urls):

        url_request = list_urls[starting_index]
        result = request_robots(url_request)
        tokens_result = tokenise_list(result)
        tokens_request = tokenise(url_request)
        for list_token in tokens_result:
            for token in list_token:
                add_node(graphe, token)
                for token_init in tokens_request:
                    add_edge(graphe, token_init, token)

        starting_index += 1