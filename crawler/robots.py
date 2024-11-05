"""Module allowing work on the robots.txt's files"""

from urllib import robotparser
from crawler.html_inspector import HTMLInspector


class Robots():
    """
    :param str url: url whose robots.txt's file will be consulted
    """

    def __init__(self, url: str):
        self.url = url

    def request_robots(self):
        """Function requesting the robot.txt's file of a given URL"""
        urls_allowed = []
        parser = robotparser.RobotFileParser()
        parser.set_url(self.url)
        parser.read()
        sitemaps = parser.site_maps()
        if sitemaps is not None:
            urls_allowed = sitemaps
        else:
            inspector = HTMLInspector(self.url)
            urls_allowed = inspector.find_urls()
        return urls_allowed
