
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def afficher_details(self):
        print(f"Nom: {self.nom}, Age: {self.age}")


class ListePersonnes:
    def __init__(self):
        self.personnes = []

    def ajouter_personne(self, nom, age):
        personne = Personne(nom, age)
        self.personnes.append(personne)

    def afficher_personnes(self):
        print("Liste des personnes:")
        for personne in self.personnes:
            personne.afficher_details()

    def rechercher_personne(self, nom):
        found = False
        for personne in self.personnes:
            if personne.nom == nom:
                personne.afficher_details()
                found = True
        if not found:
            print("Personne non trouvée.")

    def filtrer_personnes_par_age(self, min_age, max_age):
        print(f"Personnes entre {min_age} et {max_age} ans:")
        for personne in self.personnes:
            if min_age <= personne.age <= max_age:
                personne.afficher_details()


class FileAttente:
    def __init__(self):
        self.attente = []

    def ajouter_personne_en_attente(self, nom):
        self.attente.append(nom)

    def supprimer_personne_de_attente(self):
        if self.attente:
            print(f"La personne {self.attente.pop(0)} a été supprimée de la file d'attente.")
        else:
            print("La file d'attente est vide.")


class FileAttentePrioritaire(FileAttente):
    def __init__(self):
        super().__init__()
        self.prioritaires = []

    def ajouter_personne_prioritaire(self, nom):
        self.prioritaires.append(nom)

    def supprimer_personne_de_attente(self):
        if self.prioritaires:
            print(f"La personne prioritaire {self.prioritaires.pop(0)} a été supprimée de la file d'attente.")
        elif self.attente:
            print(f"La personne {self.attente.pop(0)} a été supprimée de la file d'attente.")
        else:
            print("La file d'attente est vide.")


def menu_principal():
    print("Menu Principal:")
    print("1. Gérer Liste de Personnes")
    print("2. Gérer File d'Attente")
    print("3. Quitter")
    choix = input("Entrez votre choix : ")
    return choix


def menu_gestion_personnes(liste_personnes):
    while True:
        print("\nMenu Gestion de Liste de Personnes:")
        print("1. Ajouter une personne")
        print("2. Afficher la liste de personnes")
        print("3. Rechercher une personne")
        print("4. Filtrer les personnes par âge")
        print("5. Retour")
        choix = input("Entrez votre choix : ")
        if choix == "1":
            nom = input("Entrez le nom de la personne : ")
            age = int(input("Entrez l'âge de la personne : "))
            liste_personnes.ajouter_personne(nom, age)
        elif choix == "2":
            liste_personnes.afficher_personnes()
        elif choix == "3":
            nom = input("Entrez le nom de la personne à rechercher : ")
            liste_personnes.rechercher_personne(nom)
        elif choix == "4":
            min_age = int(input("Entrez l'âge minimum : "))
            max_age = int(input("Entrez l'âge maximum : "))
            liste_personnes.filtrer_personnes_par_age(min_age, max_age)
        elif choix == "5":
            break
        else:
            print("Choix invalide.")


def menu_gestion_file_attente(file_attente):
    while True:
        print("\nMenu Gestion de File d'Attente:")
        print("1. Ajouter une personne en attente")
        print("2. Supprimer une personne de la file d'attente")
        print("3. Ajouter une personne prioritaire en attente")
        print("4. Retour")
        choix = input("Entrez votre choix : ")
        if choix == "1":
            nom = input("Entrez le nom de la personne à ajouter en attente : ")
            file_attente.ajouter_personne_en_attente(nom)
        elif choix == "2":
            file_attente.supprimer_personne_de_attente()
        elif choix == "3":
            nom = input("Entrez le nom de la personne prioritaire à ajouter en attente : ")
            file_attente.ajouter_personne_prioritaire(nom)
        elif choix == "4":
            break
        else:
            print("Choix invalide.")


def main():
    liste_personnes = ListePersonnes()
    file_attente = FileAttentePrioritaire()

    while True:
        choix = menu_principal()
        if choix == "1":
            menu_gestion_personnes(liste_personnes)
        elif choix == "2":
            menu_gestion_file_attente(file_attente)
        elif choix == "3":
            print("Au revoir !")
            break
        else:
            print("Choix invalide.")


if __name__ == "__main__":
    main()