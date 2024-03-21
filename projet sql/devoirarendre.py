
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

class ListePersonnes:
    def __init__(self):
        self.personnes = []

    def ajouter_personne(self, nom, age):
        nouvelle_personne = Personne(nom, age)
        self.personnes.append(nouvelle_personne)

    def afficher_personnes(self):
        if self.personnes:
            print("Liste des personnes:")
            for personne in self.personnes:
                print(f"Nom: {personne.nom}, Age: {personne.age}")
        else:
            print("La liste des personnes est vide.")


# Exemple d'utilisation
liste = ListePersonnes()
liste.ajouter_personne("Armel", 40)
liste.ajouter_personne("Joel", 25)
liste.ajouter_personne("Rolande", 35)
liste.ajouter_personne("Karine", 30)

liste.afficher_personnes()     
