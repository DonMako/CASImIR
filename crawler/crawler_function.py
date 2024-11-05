"""Module contenant la fonction de crawl principale"""

from crawler.html_inspector import HTMLInspector
from crawler.robots import Robots


class Crawler():
    """
    :param list stock: List of the URLs the crawler will request
    :param int limit: Number of URLs the crawler has to request
    :param int starting_index: Index of the url of the stock actually crawled
    :param list list_images: List of the images' link the crawler found
    :param bool enough_urls: Boolean indicating if the crawler's limit has been reached 
    """

    def __init__(self, stock: list, limit: int, starting_index: int, list_images: list, enough_urls: bool):
        self.stock = stock
        self.limit = limit
        self.starting_index = starting_index
        self.list_images = list_images
        self.enough_urls = enough_urls

    def crawl(self):
        """Main crawl function"""
        while self.starting_index < len(self.stock):
            if not self.enough_urls:
                url_request = self.stock[self.starting_index]
                robots_file = Robots(url_request)
                result = robots_file.request_robots()
                for url_found in result:
                    if not self.check_existing(url_found):
                        self.stock.append(url_found)
                self.enough_urls = len(self.stock) >= self.limit
            inspector = HTMLInspector(url_request)
            self.list_images.append(inspector.find_images())
            self.starting_index += 1

    def check_existing(self, new_url: str):
        """Check function to see if an URL is already in the stock"""
        return new_url in self.stock
