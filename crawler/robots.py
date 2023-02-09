from clean_function import clean_url
from crawler import request_url
from urllib import robotparser



def request_robots(url):
    
    base_url = clean_url(url)

    urls_allowed =[]

    try:
        parser = robotparser.RobotFileParser()
        parser.set_url(base_url)
        parser.read()
        sitemaps = parser.site_maps()

        if sitemaps != None:
            urls_allowed = sitemaps
        else:
            urls_allowed = request_url.request_function(url)

    except:
        urls_allowed = request_url.request_function(url)

    return urls_allowed
