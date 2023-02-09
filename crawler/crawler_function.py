from crawler import clean_function, robots
from visualisation import graphe_function



def modify_graphe(list_urls, starting_index, graphique):

    url_request = list_urls[starting_index]
    result = robots.request_robots(url_request)
    url_list = clean_function.clean_list(result)
    base_url = clean_function.clean_url(url_request)
    for url in url_list:
        graphe_function.add_node(graphique, url)
        graphe_function.add_edge(graphique, base_url, url)



def crawl(list_urls, starting_index, threshold, graphique):

    while len(graphique.nodes()) < threshold and starting_index < len(list_urls):

        modify_graphe(list_urls, starting_index, graphique)        

        starting_index += 1
