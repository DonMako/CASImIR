from visualisation.graphe import fig_to_base64
import urllib



def generate_page(graphe):

    encoded = fig_to_base64(graphe)
    my_html = '<img src="data:image/png;base64, {}">'.format(encoded.decode('utf-8'))



def display_html(html_file):
    page =  urllib.urlopen(html_file).read()
    print(page)
