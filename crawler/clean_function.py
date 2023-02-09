from urllib import parse



def clean_url(url: str):

    o = parse.urlparse(url)
    return (o.scheme + "://" + o.netloc) 



def clean_list(list: list):

    list_urls = []
    for url in list:
        list_urls.append(clean_url(url))
    return list_urls
