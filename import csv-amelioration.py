import csv
import os


def get_csv_path(filename):
    """
    Retourne le chemin complet du fichier CSV
    en se basant sur l'emplacement du script Python.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, filename)


def charger_clients(csv_path):
    """
    Charge les clients depuis le fichier CSV
    et retourne une liste de dictionnaires.
    """
    clients = []

    with open(csv_path, mode="r", encoding="utf-8") as fichier:
        lecteur = csv.DictReader(fichier, delimiter=";")

        for ligne in lecteur:
            client = {
                "id": ligne["id"],
                "nom": ligne["nom"],
                "email": ligne["email"],
                "pays": ligne["pays"],
                "age": ligne["age"],
                "actif": ligne["actif"]
            }
            clients.append(client)

    return clients


def afficher_clients_actifs(clients):
    """
    Affiche uniquement les clients actifs.
    """
    print("\n=== Clients actifs ===")
    for client in clients:
        if client["actif"] == "oui":
            print("-", client["nom"], "(", client["pays"], ")")


def afficher_clients_sans_age(clients):
    """
    Affiche les clients dont l'âge n'est pas renseigné.
    """
    print("\n=== Clients sans âge ===")
    for client in clients:
        if client["age"] == "":
            print("-", client["nom"])


def main():
    csv_path = get_csv_path("clients.csv")
    clients = charger_clients(csv_path)

    afficher_clients_actifs(clients)
    afficher_clients_sans_age(clients)


if __name__ == "__main__":
    main()
