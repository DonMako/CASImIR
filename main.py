import argparse
from crawler import crawler_function
import networkx as nx
import visualisation.page as page



def main():

    url = input("Enter the starting url : ")
    threshold = input("Enter the threshold desired : ")

    list_urls = []
    list_urls.append(url)

    starting_index = 0
    G = nx.Graph()

    crawler_function.crawl(list_urls, starting_index, threshold, G)

    page.create_graphe(G)

    page.display_page('graphe.png')



if __name__ == '__main__':
    main()
