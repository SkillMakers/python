"""
Lecture 14 - Cas pratiques concrets
Objectif : utiliser listes, dictionnaires, tuples et sets dans des situations réelles.

Astuce : exécute ce fichier, lis les sorties, puis modifie les données pour t'entraîner.
"""

# ------------------------------------------------------------
# Cas pratique 1 : Liste d'utilisateurs (liste de dictionnaires)
# ------------------------------------------------------------
print("=== Cas 1 : Liste d'utilisateurs (list de dict) ===")

users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"},
]

# Afficher tous les utilisateurs
for user in users:
    print(f"User #{user['id']} => {user['name']}")

# Chercher un utilisateur par id (exemple simple)
target_id = 2
found_user = None
for user in users:
    if user["id"] == target_id:
        found_user = user
        break

print("Utilisateur trouvé :", found_user)
print()


# ------------------------------------------------------------
# Cas pratique 2 : Configuration d'une application (dictionnaire)
# ------------------------------------------------------------
print("=== Cas 2 : Configuration (dict) ===")

config = {
    "host": "localhost",
    "port": 8080,
    "debug": True,
    "retries": 3,
}

print("Host :", config["host"])
print("Port :", config["port"])
print("Debug :", config["debug"])

# Exemple : mettre debug à False (le dict est modifiable)
config["debug"] = False
print("Debug après modification :", config["debug"])
print()


# ------------------------------------------------------------
# Cas pratique 3 : Coordonnées GPS (tuple)
# ------------------------------------------------------------
print("=== Cas 3 : Coordonnées GPS (tuple) ===")

# Un tuple est adapté quand les données sont fixes (ex: latitude/longitude)
location = (48.85, 2.35)  # Paris (exemple)
lat = location[0]
lng = location[1]

print("Location :", location)
print("Latitude :", lat)
print("Longitude :", lng)

# Important : un tuple est immuable -> on ne peut pas le modifier
# location[0] = 50  # Décommente pour voir l'erreur
print()


# ------------------------------------------------------------
# Cas pratique 4 : Emails uniques (set)
# ------------------------------------------------------------
print("=== Cas 4 : Emails uniques (set) ===")

emails = {"a@test.com", "b@test.com", "a@test.com", "c@test.com"}  # doublons possibles
print("Emails uniques :", emails)

# Tester rapidement si un email existe (super rapide avec un set)
email_to_check = "b@test.com"
print(f"{email_to_check} existe ?", email_to_check in emails)

# Ajouter / supprimer
emails.add("new@test.com")
emails.remove("a@test.com")
print("Emails après add/remove :", emails)
print()


# ------------------------------------------------------------
# Cas pratique 5 : Nettoyer une liste en supprimant les doublons (set)
# ------------------------------------------------------------
print("=== Cas 5 : Nettoyer des données (suppression doublons) ===")

raw_tags = ["python", "api", "python", "backend", "api", "clean-code"]
print("Tags bruts :", raw_tags)

clean_tags = set(raw_tags)  # supprime les doublons automatiquement
print("Tags uniques (set) :", clean_tags)

# Si tu veux revenir à une liste (par exemple pour afficher)
clean_tags_list = list(clean_tags)
print("Tags uniques (list) :", clean_tags_list)
print()


# ------------------------------------------------------------
# Cas pratique 6 : Combiner plusieurs structures (comme en production)
# ------------------------------------------------------------
print("=== Cas 6 : Combiner plusieurs structures ===")

# Exemple réaliste : liste de produits (dict) avec une taille fixe (tuple)
products = [
    {"name": "Laptop", "price": 1200, "size": (30, 20)},  # (largeur, hauteur)
    {"name": "Mouse", "price": 25, "size": (10, 5)},
    {"name": "Keyboard", "price": 80, "size": (45, 15)},
]

# Calculer le prix total
total = 0
for p in products:
    total += p["price"]

print("Prix total :", total)

# Filtrer les produits "chers" (ex: >= 100)
expensive = []
for p in products:
    if p["price"] >= 100:
        expensive.append(p["name"])

print("Produits chers :", expensive)

# Extraire les tailles uniques (set de tuples)
unique_sizes = set()
for p in products:
    unique_sizes.add(p["size"])

print("Tailles uniques :", unique_sizes)
print()


# ------------------------------------------------------------
# Récap : Comment choisir la bonne structure ?
# ------------------------------------------------------------
print("=== RÉCAP : Choisir la bonne structure ===")
print("- List  : plusieurs éléments, ordre important, modifiable")
print("- Dict  : clé -> valeur (structure claire, lisible)")
print("- Tuple : données fixes, ordonnées, immuables")
print("- Set   : valeurs uniques, pas d'ordre, très rapide pour 'in'")
