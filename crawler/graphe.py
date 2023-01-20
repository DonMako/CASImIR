# La fonction permettant de générer un graphe orienté pour représenter les liens entre les URLs collectés.



import io
import base64



def ajout_arc(graphe, link_depart, link_arrive):

    # Si le graphe possède déjà l'arc, on augmente juste le poids de l'arc
    if graphe.has_edge(link_depart, link_arrive):
        graphe[link_depart][link_arrive]["weight"] += 1

    # Sinon, on crée l'arc.
    else:
        graphe.add_edge(link_depart, link_arrive, weight=1)



def fig_to_base64(fig):

    img = io.BytesIO()
    fig.savefig(img, format='png', bbox_inches='tight')
    img.seek(0)

    return base64.b64encode(img.getvalue())

