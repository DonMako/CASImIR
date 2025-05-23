import argparse
import networkx as nx
from crawler import crawler_function
import webbrowser

def main(url: str, threshold_urls: int):

    list_urls = [url]
    starting_index = 0
    G = nx.Graph()

    graphe.set_node(G, url)

    crawler_function.crawl(list_urls, starting_index, threshold_urls, G)

    graphe.create_graphe(G)

    webbrowser.open("./visualisation/template.html", new=2)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "url", help="The URL the program start crawling from", type=str)
    parser.add_argument(
        "threshold", help="The number of URLs the program need to crawl",
        type=int)
    args = parser.parse_args()
    main(args.url, args.threshold)
