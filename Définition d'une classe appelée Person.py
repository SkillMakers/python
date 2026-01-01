# Définition d'une classe appelée Personne

class Personne:
    # Le constructeur : il est appelé automatiquement
    # Lors  de la création d'un nouvel objet
    def __init__(self, nom, age):
        #self.nom est un attribut de l'objet
        # il stocke le nom de la personne
        self.nom = nom
        self.age = age

    def se_presenter(self):
        print("Bonjour je m'appelle ", self.nom, "et j'ai ",self.age, " ans.")

p1 = Personne("Alice", 30)

p1.se_presenter()