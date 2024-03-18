# Gestion d'une file d'attente

class FileAttente:
    def __init__(self):
        self.file_attente = []

    def ajouter_personne_en_attente(self, nom):
        self.file_attente.append(nom)
        print(f"{nom} a été ajouté à la file d'attente.")

    def supprimer_personne_de_attente(self):
        if self.file_attente:
            personne_supprimee = self.file_attente.pop(0)
            print(f"{personne_supprimee} a été supprimé de la file d'attente.")
        else:
            print("La file d'attente est vide.")

# Exemple d'utilisation
file = FileAttente()
file.ajouter_personne_en_attente("Armel")
file.ajouter_personne_en_attente("Joel")
file.ajouter_personne_en_attente("Clarence")
file.ajouter_personne_en_attente("Cloe")

file.supprimer_personne_de_attente()
file.supprimer_personne_de_attente()
file.supprimer_personne_de_attente()
file.supprimer_personne_de_attente()