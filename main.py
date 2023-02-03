import crawler.crawler_function as crawler_function
import table.table as table
import networkx as nx



def main():

    url = input("Enter the starting url : ")
    threshold = input("Enter the threshold desired : ")

    list_urls = []
    list_urls.append(url)

    starting_index = 0
    G = nx.Graph()

    crawler_function.crawl(list_urls, starting_index, threshold, G)
        
    table.generate_CSV(list_urls, threshold)



if __name__ == '__main__':
    main()
