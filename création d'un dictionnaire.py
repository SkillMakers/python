#création d'un dictionnaire

utilisateur = {
    "nom": "imad",
    "age": 35,
    "ville": "Paris"

}

# Accès aux valeurs
print("Nom:", utilisateur["nom"])

# Modification d'une valeur
utilisateur["age"] = 42

#Parcours du dictionnaire
for cle,valeur in utilisateur.items():
    print(cle, ":",valeur)