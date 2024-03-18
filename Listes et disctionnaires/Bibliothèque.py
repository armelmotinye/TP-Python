# livre.py

class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur

    def __str__(self):
        return f"{self.titre} - {self.auteur}"

# librairie.py
    
from .livre import Livre

class Librairie:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, titre, auteur):
        livre = Livre(titre, auteur)
        self.livres.append(livre)

    def afficher_livres(self):
        for livre in self.livres:
            print(livre)

# main.py
            from bibliotheque.librairie import Librairie

# Création d'une instance de Librairie
ma_librairie = Librairie()

# Ajout de quelques livres
ma_librairie.ajouter_livre("le corbeau et le renard", "J. Lafontaine")
ma_librairie.ajouter_livre("CID", "J. Armel")

# Affichage des livres de la librairie
print("Livres dans la librairie :")
ma_librairie.afficher_livres()

