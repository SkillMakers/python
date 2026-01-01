# Classe 1 : comportement de base
class Vehicule:
    def demarrer(self):
        print("Le véhicule démarre")


# Classe 2 : capacité électrique
class Electrique:
    def charger(self):
        print("Le véhicule se recharge")


# Classe 3 : capacité de connexion
class Connecte:
    def connecter(self):
        print("Connexion au système embarqué")


# Classe enfant : héritage multiple
class VoitureElectriqueConnectee(Vehicule, Electrique, Connecte):
    pass


# Utilisation
voiture = VoitureElectriqueConnectee()

voiture.demarrer()
voiture.charger()
voiture.connecter()
