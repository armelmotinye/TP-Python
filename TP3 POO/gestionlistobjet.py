
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

class ListePersonnes:
    def __init__(self):
        self.personnes = []

    def ajouter_personne(self, nom, age):
        personne = Personne(nom, age)
        self.personnes.append(personne)

    def afficher_personnes(self):
        if not self.personnes:
            print("Aucune personne dans la liste.")
        else:
            print("Liste des personnes :")
            for personne in self.personnes:
                print(f"Nom: {personne.nom}, Age: {personne.age}")

    def rechercher_personne(self, nom):
        personne_trouvee = None
        for personne in self.personnes:
            if personne.nom == nom:
                personne_trouvee = personne
                break
        if personne_trouvee:
            print(f"Personne trouvée : Nom: {personne_trouvee.nom}, Age: {personne_trouvee.age}")
        else:
            print(f"Aucune personne trouvée avec le nom {nom}.")

    def filtrer_personnes_par_age(self, min_age, max_age):
        personnes_filtrees = [personne for personne in self.personnes if min_age <= personne.age <= max_age]
        if personnes_filtrees:
            print("Personnes dont l'âge est compris entre", min_age, "et", max_age, ":")
            for personne in personnes_filtrees:
                print(f"Nom: {personne.nom}, Age: {personne.age}")
        else:
            print("Aucune personne trouvée avec l'âge compris entre", min_age, "et", max_age)

# Exemple d'utilisation :
liste_personnes = ListePersonnes()

# Ajout de personnes à la liste
liste_personnes.ajouter_personne("Armel", 40)
liste_personnes.ajouter_personne("Joel", 30)
liste_personnes.ajouter_personne("Rolande", 35)

# Affichage des détails des personnes dans la liste
liste_personnes.afficher_personnes()

# Recherche d'une personne par son nom
liste_personnes.rechercher_personne()

# Filtrage des personnes par âge
liste_personnes.filtrer_personnes_par_age(30, 35)