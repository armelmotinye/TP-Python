class SalleCinema:
    def __init__(self, nb_places, nb_places_speciales):
        self.nb_places = nb_places
        self.nb_places_speciales = nb_places_speciales
        self.places_reservees = {}
        self.places_speciales_reservees = {}

    def nombre_places_disponibles(self):
        return self.nb_places - len(self.places_reservees)

    def reserver_place(self, nom, place):
        if place <= self.nb_places and place > 0:
            if place not in self.places_reservees:
                self.places_reservees[place] = nom
                print(f"Place {place} réservée pour {nom}.")
            else:
                print(f"La place {place} est déjà réservée.")
        else:
            print(f"La place {place} n'existe pas dans cette salle.")

    def reserver_place_speciale(self, nom):
        if len(self.places_speciales_reservees) < self.nb_places_speciales:
            place_speciale = self.nb_places + len(self.places_speciales_reservees) + 1
            self.places_speciales_reservees[place_speciale] = nom
            print(f"Place spéciale réservée pour {nom}.")
        else:
            print("Toutes les places spéciales sont déjà réservées.")

    def afficher_places_reservees(self):
        if self.places_reservees:
            print("Places réservées :")
            for place, nom in self.places_reservees.items():
                print(f"Place {place} : {nom}")
        else:
            print("Aucune place n'a été réservée.")

        if self.places_speciales_reservees:
            print("\nPlaces spéciales réservées :")
            for place, nom in self.places_speciales_reservees.items():
                print(f"Place spéciale {place} : {nom}")

    def filtrer_reservations_par_personne(self, nom):
        reservations = [(place, nom_personne) for place, nom_personne in self.places_reservees.items() if nom_personne == nom]
        if reservations:
            print(f"Réservations pour {nom} :")
            for place, nom_personne in reservations:
                print(f"Place {place}")
        else:
            print(f"Aucune réservation trouvée pour {nom}.")

    def annuler_reservation(self, nom):
        reservations_a_annuler = [place for place, nom_personne in self.places_reservees.items() if nom_personne == nom]
        if reservations_a_annuler:
            for place in reservations_a_annuler:
                del self.places_reservees[place]
            print(f"Réservations annulées pour {nom}.")
        else:
            print(f"Aucune réservation trouvée pour {nom}.")

# Fonction pour afficher le menu principal
def afficher_menu_principal():
    print("\nMenu Principal :")
    print("1. Réserver une place")
    print("2. Réserver une place spéciale")
    print("3. Afficher les places réservées")
    print("4. Vérifier le nombre de places disponibles")
    print("5. Filtrer les réservations par personne")
    print("6. Annuler des réservations")
    print("7. Quitter")

# Exécution du programme
salle = SalleCinema(50, 5)

while True:
    afficher_menu_principal()
    choix = input("Entrez votre choix : ")

    if choix == "1":
        nom = input("Entrez votre nom : ")
        place = int(input("Entrez le numéro de la place : "))
        salle.reserver_place(nom, place)

    elif choix == "2":
        nom = input("Entrez votre nom : ")
        salle.reserver_place_speciale(nom)

    elif choix == "3":
        salle.afficher_places_reservees()

    elif choix == "4":
        print("Nombre de places disponibles :", salle.nombre_places_disponibles())

    elif choix == "5":
        nom = input("Entrez le nom de la personne : ")
        salle.filtrer_reservations_par_personne(nom)

    elif choix == "6":
        nom = input("Entrez le nom de la personne dont vous voulez annuler les réservations : ")
        salle.annuler_reservation(nom)

    elif choix == "7":
        print("Au revoir !")
        break

    else:
        print("Choix invalide. Veuillez entrer un nombre entre 1 et 7.")
        