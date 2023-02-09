import matplotlib.pyplot as plt
import networkx as nx



def set_edge(graphe: nx.Graph, depart: str, arrive: str):

    if graphe.has_edge(depart, arrive):
        pass

    else:
        graphe.add_edge(depart, arrive)



def get_node_size(token: str):

    return(len(token))



def set_node(graphe: nx.Graph, token: str):

    if not(graphe.has_node(token)):
        graphe.add_node(token, size = get_node_size(token))



def create_graphe(graphe: nx.Graph):

    labels = {}    
    for node in graphe.nodes():
        labels[node] = node
    pos = nx.spring_layout(graphe)
    nx.draw_networkx(graphe, pos, node_shape = "s", node_color = "yellow", with_labels = False)
    nx.draw_networkx_labels(graphe, pos, labels)
    plt.tight_layout()
    plt.savefig("./visualisation/graphe.png", bbox_inches = "tight", pad_inches = 0, format = "png")
