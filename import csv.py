import csv
import os

# dossier ou se trouve le script Python
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# chemin complet vers le fichier csv
csv_path = os.path.join(BASE_DIR, "clients.csv")

# Ouvrir le fichier en mode lecture

with open(csv_path, mode = "r", encoding="utf-8") as fichier:
    # Créer un lcteur csv
    # Chaque ligne est lue sous forme de liste
    lecteur = csv.reader(fichier, delimiter=";")
    # Lire et ignorer la première ligne (en-têtes)
    entetes = next(lecteur)

    for ligne in lecteur:
        # Associer chaque colonne à une variable
        print(ligne)
        id_client = ligne[0]
        nom  = ligne[1]
        email = ligne[2]
        pays = ligne[3]
        age = ligne[4]
        actif = ligne[5]

        if(actif == "oui"):
            print(nom, " est un client actif")

        if age == "":
            print(nom, " n'a pas d'age renseigné")