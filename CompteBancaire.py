class CompteBancaire:
    def __init__(self, solde_initial):
        self.solde = solde_initial

    def deposer(self, montant):
        self.solde += montant
        print("Dépot effectué. Nouveau solde :",self.solde)

    def retirer(self, montant):
        if montant <= self.solde:
            self.solde -= montant
            print("Retrait effectué. Nouveau solde :", self.solde)
        else:
            print("Erreur : solde insuffisant")
    
    def afficher(self):
        print("solde actuel : ",self.solde)

compte = CompteBancaire(100)

compte.afficher()
compte.deposer(50)
compte.retirer(30)
compte.afficher()