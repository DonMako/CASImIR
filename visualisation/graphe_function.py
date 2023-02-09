import matplotlib.pyplot as plt
import networkx as nx



def add_edge(graphe, depart, arrive):

    if graphe.has_edge(depart, arrive):
        pass

    else:
        graphe.add_edge(depart, arrive, weight = 1)



def add_node(graphe, token):

    if not(graphe.has_node(token)):
        graphe.add_node(token)



def create_graphe(graphe):

    labels = {}    
    for node in graphe.nodes():
        labels[node] = node
    pos = nx.spring_layout(graphe)
    nx.draw_networkx(graphe, pos, node_shape = 's', node_color="yellow", with_labels=False)
    nx.draw_networkx_labels(graphe, pos, labels)    
    plt.savefig('./visualisation/graphe.png', bbox_inches='tight', pad_inches=0, format='png')
