import requests

try:
# URL de l'API 
    url = "https://api.github.com"


    # Envoi d'une requête HTTP GET
    response = requests.get(url, timeout=5)

    response.raise_for_status()

    # Afficher le statut de la réponse
    print("Status code : ",response.status_code)

    # Transformer la réponse JSON en objet Python
    data = response.json()

    print(data["current_user_url"])
except requests.exceptions.Timeout:
    print("Timeout: le serveur ne répond pas")
except requests.exceptions.ConnectionError:
    print("Erreur de connexio à l'api")
except requests.exceptions.HTTPError as e:
    print("Erreur Http:",e)
except requests.exceptions.RequestException as e:
    print("Erreur lors de la requête : ",e)