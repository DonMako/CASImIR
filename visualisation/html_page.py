import urllib



#def generate_page(graphe):



def display_html(html_file):
    page =  urllib.urlopen(html_file).read()
    print(page)
