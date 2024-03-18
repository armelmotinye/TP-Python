class Livre:
    def __init__(self, titre, auteur, genre, prix):
        self.titre = titre
        self.auteur = auteur
        self.genre = genre
        self.prix = prix

    def get_titre(self):
        return self.titre

    def set_titre(self, titre):
        self.titre = titre

    def get_auteur(self):
        return self.auteur

    def set_auteur(self, auteur):
        self.auteur = auteur

    def get_genre(self):
        return self.genre

    def set_genre(self, genre):
        self.genre = genre

    def get_prix(self):
        return self.prix

    def set_prix(self, prix):
        self.prix = prix

    def afficher_details(self):
        print(f"Titre: {self.titre}")
        print(f"Auteur: {self.auteur}")
        print(f"Genre: {self.genre}")
        print(f"Prix: {self.prix} $CA")

class Librairie:
    def __init__(self):
        self.livres = {}

    def ajouter_livre(self, livre):
        self.livres[livre.get_titre()] = livre
        print(f"Le livre {livre.get_titre()} a ete ajoute a la librairie.")

    def supprimer_livre(self, titre_livre):
        if titre_livre in self.livres:
            del self.livres[titre_livre]
            print(f"Le livre {titre_livre} a ete suprimer de la librairie.")
        else:
            print(f"Le livre {titre_livre} n'existe pas dans la librairie")    


    def chercher_livre(self, titre_livre):
        if titre_livre in self.livres:
            livre = self.livres[titre_livre]
            print("Détails du livre :")
            livre.afficher_details()
        else:
            print(f"Le livre '{titre_livre}' n'a pas été trouvé dans la librairie.")

# Test de l'implémentation
librairie = Librairie()

# Ajout de livres
livre1 = Livre("Paw patrouille", "Dysney", "Animation", 75)
livre2 = Livre("Deception", "Armel", "Romance", 80)
livre3 = Livre("Star War", "Joel", "Science-fiction", 70)

librairie.ajouter_livre(livre1)
librairie.ajouter_livre(livre2)
librairie.ajouter_livre(livre3)