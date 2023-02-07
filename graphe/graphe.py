def add_edge(graphe, depart, arrive):

    if graphe.has_edge(depart, arrive):
        graphe[depart][arrive]["weight"] += 1

    else:
        graphe.add_edge(depart, arrive, weight=1)



def add_node(graphe, token):

    if not(graphe.has_node(token)):
        graphe.add_node(token)
