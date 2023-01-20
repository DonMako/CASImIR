# La fonction pour afficher le graphe orienté sur un serveur local



from graphe import fig_to_base64



def generate_page(graphe):

    encoded = fig_to_base64(graphe)
    my_html = '<img src="data:image/png;base64, {}">'.format(encoded.decode('utf-8'))