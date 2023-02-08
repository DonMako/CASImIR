import jinja2
import matplotlib.pyplot as plt
import networkx as nx
import webbrowser



def create_graphe(graphe):

    labels = {}    
    for node in graphe.nodes(): 
        labels[node] = node
    pos = nx.spring_layout(graphe, seed=225)
    nx.draw_networkx(graphe, pos, node_shape = 's', node_color="None", with_labels=False)
    nx.draw_networkx_labels(graphe, pos, labels)    
    plt.savefig('graphe.png', format='png')



def generate_page(image):

    outputfile = 'mygraphe.html'

    subs = jinja2.Environment(loader = jinja2.FileSystemLoader('./')).get_template('template.html').render(mydata=image)
    
    with open(outputfile,'w') as f:
        f.write(subs)

    return outputfile



def display_page(file):

    url = file
    webbrowser.open(url,new=2)



def page_from_scratch(image):

    display_page(generate_page(image))
