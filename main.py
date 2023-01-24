from crawler.crawler import crawl
from table.table import generate_table
import networkx as nx



def main():

    url = input("Enter the starting url : ")
    threshold = input("Enter the threshold desired : ")

    list_urls = []
    list_urls.append(url)

    starting_index = 0
    G = nx.Graph()

    crawl(list_urls, starting_index, threshold, G)
        
    generate_table(list_urls, threshold)



if __name__ == '__main__':
    main()
