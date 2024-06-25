"""Module allowing work on the HTML code"""

from urllib import parse, request
from bs4 import BeautifulSoup as BS
import validators

class HTMLInspector():
    """
        :param url:
        URL of the page which HTML code will be inspected
    
    """

    def __init__(self, url: str):
        self.url = url

    def prepare_soup(self)
        """Method used by others to find what needed inside the HTML code"""
        source_code = request.urlopen(self.url)
        return BS(source_code, "html.parser")
    
    def find_images(self):
        """Method finding images inside the HTML code"""
        images_found = []
        parser = parse.urlparse(self.url)
        scheme = parser.scheme
        netloc = parser.netloc
        soup = self.prepare_soup()
        for link in soup.find_all("a"):
            ref = link.get("href")
            if validators.url(ref):
                images_found.append(ref)
            else:
                images_found.append(scheme + netloc + ref)
        return images_found

    def find_urls(self):
        """Method finding other link inside the HTML code"""
        urls_found = []
        parser = parse.urlparse(self.url)
        scheme = parser.scheme
        netloc = parser.netloc
        soup = self.prepare_soup()
        for link in soup.find_all("a"):
            ref = link.get("href")
            if validators.url(ref):
                urls_found.append(ref)
            else:
                urls_found.append(scheme + netloc + ref)
        return urls_found
