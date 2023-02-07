import crawler.crawler_function as crawler_function
import networkx as nx
import visualisation.display_page as display_page
import visualisation.create_graphe as create_graphe



def main():

    url = input("Enter the starting url : ")
    threshold = input("Enter the threshold desired : ")

    list_urls = []
    list_urls.append(url)

    starting_index = 0
    G = nx.Graph()

    crawler_function.crawl(list_urls, starting_index, threshold, G)

    create_graphe.create_graphe(G)

    display_page.display_page()



if __name__ == '__main__':
    main()
