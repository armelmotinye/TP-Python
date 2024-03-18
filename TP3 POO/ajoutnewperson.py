class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

class ListePersonnes:
    def __init__(self):
        self.liste_personnes = []

    # Ajout d'une nouvelle personne 

    def ajouter_personne(self, nom, age):
        personne = Personne(nom, age)
        self.liste_personnes.append(personne)

    def afficher_personnes(self):
        print("Liste des personnes :")
        for personne in self.liste_personnes:
            print(f"Nom: {personne.nom}, Age: {personne.age}")

liste = ListePersonnes()
liste.ajouter_personne("Armel", 30)
liste.ajouter_personne("Joel", 25)
liste.ajouter_personne("Clarence", 40)
liste.ajouter_personne("Cloe", 35)

liste.afficher_personnes()