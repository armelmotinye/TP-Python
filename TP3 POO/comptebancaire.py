# creation d'un système de compte bancaire simple en utilisant les principes de la POO

class CompteBancaire:

    # Permettre aux utilisateurs de créer un nouveau compte bancaire avec un solde initial.
    def __init__(self, solde_initial=0):
        self.solde = solde_initial

        # Permettre aux utilisateurs de déposer de l'argent sur leur compte.

    def depot(self, montant):
        self.solde += montant
        print(f"Armel {montant}$ a ete depose dans votre compte")
        self.verifier_solde()

        # Permettre aux utilisateurs de retirer de l'argent de leur compte (si le solde est suffisant)

    def retrait(self, montant):
        if self.solde >= montant:
            self.solde -= montant
            print(f"Armel {montant}$ a ete retire de votre compte")
        else:
            print("Solde insuffisant pour le retrait.")
        self.verifier_solde()

        # Permettre aux utilisateurs de vérifier leur solde de compte

    def verifier_solde(self):
        print(f"votre Solde actuel : {self.solde}$")

e1 = CompteBancaire(4200)
e1.verifier_solde()
e1.depot(1000)
e1.retrait(250)
e1.verifier_solde()

