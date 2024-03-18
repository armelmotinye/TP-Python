# priorisation de la file d'attente

class FileAttente:
    def __init__(self):
        self.file_attente_normale = []
        self.file_attente_prioritaire = []

    def ajouter_personne_en_attente(self, nom):
        self.file_attente_normale.append(nom)
        print(f"{nom} a été ajouté à la file d'attente normale.")

    def ajouter_personne_prioritaire(self, nom):
        self.file_attente_prioritaire.append(nom)
        print(f"{nom} a été ajouté à la file d'attente prioritaire.")

    def supprimer_personne_de_attente(self):
        if self.file_attente_prioritaire:
            personne_supprimee = self.file_attente_prioritaire.pop(0)
            print(f"{personne_supprimee} a été supprimé de la file d'attente prioritaire.")
        elif self.file_attente_normale:
            personne_supprimee = self.file_attente_normale.pop(0)
            print(f"{personne_supprimee} a été supprimé de la file d'attente normale.")
        else:
            print("La file d'attente est vide.")

# Exemple d'utilisation
file = FileAttente()
file.ajouter_personne_prioritaire("Armel")
file.ajouter_personne_prioritaire("Joel")
file.ajouter_personne_en_attente("Clarence")
file.ajouter_personne_en_attente("Cloe")

file.supprimer_personne_de_attente()
file.supprimer_personne_de_attente()
file.supprimer_personne_de_attente()
file.supprimer_personne_de_attente()