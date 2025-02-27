"""Module allowing work on the HTML code"""

from urllib import request
from bs4 import BeautifulSoup as BS


class HTMLInspector():
    
    """
    :param str url: URL of the page which HTML code will be inspected
    """

    def __init__(self, url: str):
        self.url = url

    def prepare_soup(self):
        """Method used by others to find what needed inside the HTML code"""
        response = request.get(self.url)
        return BS(response.text, "html.parser")

    def find_images(self):
        """Method finding images inside the HTML code"""
        images_found = []
        soup = self.prepare_soup()
        for link in soup.find_all("img"):
            source = link.get("src")
            images_found.append(source)
        return images_found

    def find_urls(self):
        """Method finding URL inside the HTML code"""
        urls_found = []
        soup = self.prepare_soup()
        for link in soup.find_all("a"):
            ref = link.get("href")
            urls_found.append(ref)
        return urls_found
