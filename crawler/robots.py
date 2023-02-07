from urllib import parse, robotparser
import request_url



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
            urls_allowed = request_url.request_function(url)

    except:
        urls_allowed = request_url.request_function(url)

    return urls_allowed