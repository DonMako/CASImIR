import matplotlib.pyplot as plt
import networkx as nx


def create_graphe(graphe):

    pos = nx.spring_layout(graphe, seed=225)
    nx.draw(graphe, pos)
    plt.savefig('graphe.png', format='png')

G = nx.Graph()
create_graphe(G)