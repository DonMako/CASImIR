def add_edge(graphe, link_depart, link_arrive):

    if graphe.has_edge(link_depart, link_arrive):
        graphe[link_depart][link_arrive]["weight"] += 1

    else:
        graphe.add_edge(link_depart, link_arrive, weight=1)



def add_node(graphe, link):

    if graphe.has_node(link):
        graphe.add_node(link)

