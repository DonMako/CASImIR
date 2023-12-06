from datetime import datetime

from bokeh.io import curdoc

from bokeh.layouts import column, row
from bokeh.models import PasswordInput, TextInput
from bokeh.models.widgets import Button, Div

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

logo = Div(text="<img src='myapp/static/logo.png'>", margin=(0, 15, 0, -10))

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


# LES CHANGEMENTS DE PAGE

page = column(
    column(logo, identifier, password, row(valider, effacer))
)


def deconnect():
    efface()
    page.children.pop()
    page.children.append(
        column(logo, identifier, password, row(valider, effacer))
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
                    row(logo,
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
                    row(logo,
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
                logo,
                alert,
                identifier,
                password,
                row(valider, effacer),
            )
        )


def access_profil():
    val = identifier.value
    mdp.value = password.value
    page.children.pop()
    page.children.append(
        column(
            row(logo, column(row(home, retour), row(deco, home_button))),
            TextInput(
                value=val, title="Identifiant :", disabled=True, margin=(0, 0, 10, 700)
            ),
            mdp,
            confirm,
            chgt,
        )
    )


def change():
    val = identifier.value
    if mdp.value == confirm.value:
        page.children.pop()
        page.children.append(
            column(
                row(logo, column(row(home, retour), row(deco, home_button))),
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
            )
        )
        liste_connexion[val] = mdp.value
    else:
        confirm.value = ""
        page.children.pop()
        page.children.append(
            column(
                row(logo, column(row(home, retour), row(deco, home_button))),
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
            )
        )

chgt.on_click(change)

profil.on_click(access_profil)

retour.on_click(connect)

valider.on_click(connect)

curdoc().add_root(page)
