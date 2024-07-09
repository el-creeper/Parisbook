# Serveur Web Post - (c) Jean Diraison 2019 sous licence GPLv3
# <jean.diraison@ac-rennes.fr>
#
# Principe de fonctionnement d'un serveur web non sécurisé, en Python
#
# le site doit être placé dans un sous-répertoire SITE placé dans le
# même répertoire que le programme exécuté
#
# utilisez l'URL http://localhost:8080/ avec le navigateur
#

import socket
import subprocess
import os

PORT = 8080

RACINE_SITE = "SITE"

PYTHON_EXE = "python"		# interpreteur a utiliser pour les CGI

############################################
# Traitement non sécurisé des requêtes web #
############################################

# renvoie la reponse à la requête transmise, sous la forme
# de données binaires en respectant le protocole HTTP
def traiter_requete(requete):
    # conversion des lignes de la requete en liste de lignes
    requete = (requete.decode("utf8")).split("\r\n")
    # détermination de la méthode à partir de la première ligne
    methode, chemin, protocole = requete[0].split(" ")
    # dictionnaire des champs de la requête (non utilisé ici)
    champs = dict([champ.partition(": ")[::2] for champ in requete[1:]])
    print(methode, chemin)
    if methode == "GET":   # prise en charge de la méthode GET
        reponse_succes, reponse_type, reponse_donnees = traiter_GET(chemin)
    elif methode == "POST": # prise en charge de la méthode POST
        reponse_succes, reponse_type, reponse_donnees = traiter_POST(chemin, requete)
    else:                  # autres méthodes PUT, DELETE, ...
        reponse_succes, reponse_type, reponse_donnees = 501, "text/html", b"Not Implemented"
    # renvoie le résultat de la méthode GET conformément au protocole HTTP
    return """HTTP/1.0 {} OK\r
Content-Type: {}\r
Content-Length: {}\r
Connection: close\r
Server: python\r
\r
""".format(reponse_succes, reponse_type, len(reponse_donnees)).encode() + reponse_donnees


# implémentation de la méthode GET
# renvoie le code de retour, le type mime et les données pour le fichier
# dont le chemin est passé en argument
def traiter_GET(chemin):
    if chemin == "/":
        chemin += "index.html"
    try:
        with open(RACINE_SITE + chemin, "rb") as fichier:
            donnees = fichier.read()
            return 200, type_de_fichier(chemin), donnees
    except (OSError, IOError) as exception:
        return 404, "text/plain", b"""Erreur 404"""


# implémentation de la méthode POST
# (exécute le script CGI en appelant l'interpréteur python, transmet en entrée
#  les données du POST et récupère en sortie les données à retransmettre)
# renvoie le code de retour, le type mime et les données fournies par le script
def traiter_POST(chemin, requete):
    post = requete[-1]
    env = dict(os.environ)
    env.update({"REQUEST_METHOD":"POST"})
    try:
        print(RACINE_SITE + chemin)
        with subprocess.Popen([PYTHON_EXE, RACINE_SITE + chemin], stdin=subprocess.PIPE, stdout=subprocess.PIPE, env=env) as cgi:
            reponse = cgi.communicate(input=post.encode(), timeout=5)[0]
            cgi.wait(timeout=5)
        if not reponse:
            raise OSError
        separateur = b"\r\n\r\n" if b"\r" in reponse[:64] else b"\n\n"
        contenu, sep, donnees = reponse.partition(separateur)
        content_type = contenu.partition(b": ")[-1].decode()
        return 200, content_type, donnees
    except (OSError, ValueError, subprocess.TimeoutExpired) as exception:
        return 404, "text/plain", b"""Erreur 404"""


# renvoie le type mime associé au fichier
# se base uniquement sur l'extension du nom du fichier
def type_de_fichier(chemin):
    types_mime = {
        "html":"text/html; charset=UTF-8",
        "css" :"text/css",
        "py"  :"text/x-python",
        "jpeg":"image/jpeg", "jpg":"image/jpeg",
        "png" :"image/png",
        "gif" :"image/gif",
        "mp4" :"video/mp4",
        "mp3" :"audio/mpeg",
        "txt" :"text/plain",
        "zip" :"application/zip",
        "exe" :"application/x-ms-dos-executable",
        "gz"  :"application/gzip",
        "bin" :"application/octet-stream"
    }
    extension = chemin.split(".")[-1].lower()
    if extension in types_mime:
        return types_mime[extension]
    return "application/octet-stream"


###############
# Serveur web #
###############

# se met en écoute sur le port 8080 et traite les requetes HTTP
def lancer_serveur_web():
    # allouer une communication TCP sur IP
    serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # fixer la communication sur le port PORT=8080 (non privilegié)
    serveur.bind(("", PORT))
    # réserver une file d'attente de 10 connexions
    serveur.listen(10)
    # boucle principale
    while True:
        # mise en attente jusqu'à réception d'une connection cliente
        client, info = serveur.accept()
        # reception de la requete du client
        requete = client.recv(4096)
        # le client a-t-il envoyé une requête ou fermé sa connexion ?
        if len(requete) > 0:
            # traitement de la requete (reponse = page html, image, ... binaire)
            reponse = traiter_requete(requete)
            # renvoie la reponse dans sa totalite (par petits bouts)
            while len(reponse) > 0:
                taille = client.send(reponse)
                reponse = reponse[taille:]
        # fermeture de la connexion etablie avec le client
        client.close()


lancer_serveur_web()
