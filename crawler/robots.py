from urllib import parse
from urllib import robotparser
from crawler.requete import request



def request_robots(url):
    
    o = parse.urlparse(url)
    base_url = "https://" + str(o.hostname)

    urls_allowed =[]

    try:
        parser = robotparser.RobotFileParser()
        parser.set_url(base_url)
        parser.read()
        sitemaps = parser.site_maps()

        if sitemaps != None:
            urls_allowed = sitemaps
        else:
            urls_allowed = request(url)

    except:
        urls_allowed = request(url)

    return urls_allowed