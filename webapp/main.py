from datetime import datetime
from multiprocessing.dummy import Value
import validators

from bokeh.io import curdoc

from bokeh.layouts import column, row
from bokeh.models import (
    PasswordInput,
    TableColumn,
    TextInput,
)
from bokeh.models.widgets import Button, Div, Dropdown

# conn = pyodbc.connect(
#    "DRIVER={MySQL ODBC 3.51 Driver};SERVER=localhost;PORT= 5432;DATABASE=y;UID=root;PWD=123456789;"
# )
# cursor = conn.cursor()


# L'ÉCRAN DE CONNEXION

liste_connexion = {
    "insee": ["insee", "admin"],
    "test1": ["ensai", "user"],
    "test2": ["ensae", "user"],
}


identifier = TextInput(title="Identifiant :", margin=(0, 0, 10, 700))
password = PasswordInput(title="Mot de passe :", margin=(0, 0, 10, 700))
valider = Button(label="SE CONNECTER", margin=(0, 0, 10, 700))
effacer = Button(label="effacer", button_type="light")

picto = Div(text="<img src='myapp/static/ecoute.jpg'>", margin=(250, 0, 0, 10))
header = Div(text="<img src='myapp/static/header.png'>", margin=(0, 15, 0, -10))
logo = Div(
    text="<a href='https://air.defense.gouv.fr/'><img src='myapp/static/logo.png'></a>",
    margin=(50, 0, 0, 120),
)

alert = Div(
    text="<a style='background-color: rgb(255, 238, 221); outline: solid red;'>Les informations transmises n'ont pas permis de vous authentifier.</a>",
    margin=(0, 0, 10, 700),
)


t1 = Div(text="Du ", margin=(0, 0, 10, 690))
t2 = Div(text=" au ", margin=(0, 0, 10, 5))
t01 = TextInput(value="2023-10-01", margin=(0, 0, 10, 5))
t02 = TextInput(value="2023-10-31", margin=(0, 0, 10, 5))


def efface():
    identifier.value = ""
    password.value = ""


effacer.on_click(efface)


# LE HEADER DE TOUTES LES PAGES

bonhomme = Div(text="<img src='myapp/static/profil.png'>", margin=(65, 0, 0, 0))
profil = Button(
    label="Modifier le profil", margin=(65, 0, 0, 0), button_type="light", height=45
)
deco = Div(text="<img src='myapp/static/deconnect.png'>", margin=(10, 0, 0, 0))
home_button = Button(
    label="DÉCONNEXION", button_type="danger", margin=(10, 0, 0, 0), height=45
)
home = Div(text="<img src='myapp/static/home.png'>", margin=(65, 0, 0, 0))
retour = Button(
    label="Retourner au menu", margin=(65, 0, 0, 10), button_type="light", height=45
)


# LE FORMULAIRE DE CONTACT

date = TextInput(
    value=datetime.today().strftime("%Y-%m-%d"), title="Date :", margin=(0, 0, 10, 700)
)
duree = TextInput(title="Durée d'exposition (s) :", margin=(0, 0, 10, 700))
url = TextInput(title="Lien du contenu choquant :", margin=(0, 0, 10, 700))
comment = TextInput(title="Commentaire éventuel :", margin=(0, 0, 10, 700))
bouton = Button(label="VALIDER", button_type="success", margin=(15, 0, 0, 725))


def verif():
    if (
        datetime.strptime(date.value, "%Y-%m-%d")
        and isinstance(duree.value, int)
        and validators.url(url.value)
    ):
        bouton.button_type = "success"
    else:
        date.value = datetime.today().strftime("%Y-%m-%d")
        duree.value = ""
        url.value = ""


bouton.on_click(verif)


# LA PAGE PROFIL

mdp = TextInput(title="Mot de passe :", margin=(0, 0, 10, 700))
confirm = TextInput(
    title="Confirmez votre nouveau mot de passe :", margin=(0, 0, 10, 700)
)
chgt = Button(label="VALIDER LE CHANGEMENT", margin=(15, 0, 0, 700))

pb = Div(
    text="<a style='background-color: rgb(255, 238, 221); outline: solid red;'>Les mots de passe ne correspondent pas.</a>",
    margin=(0, 0, 10, 700),
)

success = Div(
    text="<a style='background-color: rgb(144, 238, 144); outline: solid green;'>Votre mot de passe a été changé.</a>",
    margin=(10, 0, 0, 700),
)


# LA PAGE POUR CONSULTER / TÉLÉCHARGER LES DONNÉES

options = ["Afficher par 10", "Afficher par 20", "Afficher par 50", "Afficher par 100"]
liste_deroul = Dropdown(label="Afficher par 20", menu=options, margin=(0, 0, 10, 700))

dico = {
    "urls": [
        "http://example.com/back.htm?basket=airport",
        "https://adjustment.example.com/beds",
        "http://advertisement.example.com/?amusement=blow",
        "http://www.example.com/?activity=believe",
        "https://airport.example.com/approval.php?acoustics=back",
        "https://ants.example.edu/afternoon",
        "http://branch.example.com/bikes/books",
        "https://bat.example.com/",
        "https://www.example.com/",
        "http://arm.example.com/",
        "http://afternoon.example.com/",
        "http://www.example.com/account.htm",
    ],
    "comments": [
        "Images choquantes d'une attaque sur des civils",
        "",
        "Meurtres avec violences",
        "Mise à mort de soldats rebelles",
        "Attentat suicide d'un terroriste islamique",
        "Attaque au véhicule blindé sur des civils dans le centre-ville",
        "Lapidation d'un soldat",
        "Vidéo de meurtre d'otages",
        "Décapitation",
        "",
        "Tirs de roquette sur un convoi humanitaire",
        "Attaque de journalistes européens",
    ],
}


columns = [
    TableColumn(field="urls", title="URLs"),
    TableColumn(field="comments", title="Commentaires"),
]


# LES CHANGEMENTS DE PAGE

page = column(
    column(row(logo, header), identifier, password, row(valider, effacer), picto)
)


def deconnect():
    efface()
    page.children.pop()
    page.children.append(
        column(row(logo, header), identifier, password, row(valider, effacer), picto)
    )


home_button.on_click(deconnect)


def connect():
    val = identifier.value
    if (
        val in liste_connexion.keys()
        and password.value == liste_connexion[identifier.value][0]
    ):
        if liste_connexion[identifier.value][1] == "user":
            date.value = datetime.today().strftime("%Y-%m-%d")
            duree.value = ""
            url.value = ""
            comment.value = ""
            page.children.pop()
            page.children.append(
                column(
                    row(
                        logo,
                        header,
                        column(row(bonhomme, profil), row(deco, home_button)),
                    ),
                    TextInput(
                        value=val,
                        title="Identifiant :",
                        disabled=True,
                        margin=(0, 0, 10, 700),
                    ),
                    date,
                    duree,
                    url,
                    comment,
                    bouton,
                )
            )
        else:
            page.children.pop()
            page.children.append(
                column(
                    row(
                        logo,
                        header,
                        column(row(bonhomme, profil), row(deco, home_button)),
                    ),
                    row(t1, t01, t2, t02),
                )
            )
    else:
        efface()
        page.children.pop()
        page.children.append(
            column(
                row(logo, header),
                alert,
                identifier,
                password,
                row(valider, effacer),
                picto,
            )
        )


def access_profil():
    val = identifier.value
    mdp.value = password.value
    page.children.pop()
    page.children.append(
        column(
            row(logo, header, column(row(home, retour), row(deco, home_button))),
            TextInput(
                value=val, title="Identifiant :", disabled=True, margin=(0, 0, 10, 700)
            ),
            mdp,
            confirm,
            chgt,
            picto,
        )
    )


def change():
    val = identifier.value
    if mdp.value == confirm.value:
        page.children.pop()
        page.children.append(
            column(
                row(logo, header, column(row(home, retour), row(deco, home_button))),
                TextInput(
                    value=val,
                    title="Identifiant :",
                    disabled=True,
                    margin=(0, 0, 10, 700),
                ),
                mdp,
                confirm,
                chgt,
                success,
                picto,
            )
        )
        liste_connexion[val] = mdp.value
    else:
        confirm.value = ""
        page.children.pop()
        page.children.append(
            column(
                row(logo, header, column(row(home, retour), row(deco, home_button))),
                pb,
                TextInput(
                    value=val,
                    title="Identifiant :",
                    disabled=True,
                    margin=(0, 0, 10, 700),
                ),
                mdp,
                confirm,
                chgt,
                picto,
            )
        )


def handler(event):
    liste_deroul.label = event.item


liste_deroul.on_click(handler)

chgt.on_click(change)

profil.on_click(access_profil)

retour.on_click(connect)

valider.on_click(connect)

curdoc().add_root(page)
