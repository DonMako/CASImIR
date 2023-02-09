from crawler import clean_function, robots
from graphe import graphe_function



def modify_graphe(list_urls, starting_index, graphique):

    url_request = list_urls[starting_index]
    result = robots.request_robots(url_request)
    tokens_result = clean_function.clean_list(result)
    tokens_request = clean_function.clean_url(url_request)
    for list_token in tokens_result:
        for token in list_token:
            graphe_function.add_node(graphique, token)
            for token_init in tokens_request:
                graphe_function.add_edge(graphique, token_init, token)



def crawl(list_urls, starting_index, threshold, graphique):

    while len(graphique.nodes()) < threshold and starting_index < len(list_urls):

        modify_graphe(list_urls, starting_index, graphique)        

        starting_index += 1
