class SalleCinema:
    def __init__(self, nb_places):
        self.nb_places = nb_places
        self.places_reservees = {}

    def reserver_place(self, nom, place):
        if place <= self.nb_places and place > 0:
            if place not in self.places_reservees:
                self.places_reservees[place] = nom
                print(f"Place {place} réservée pour {nom}.")
            else:
                print(f"La place {place} est déjà réservée.")
        else:
            print(f"La place {place} n'existe pas dans cette salle.")

    def afficher_places_reservees(self):
        if self.places_reservees:
            print("Places réservées :")
            for place, nom in self.places_reservees.items():
                print(f"Place {place} : {nom}")
        else:
            print("Aucune place n'a été réservée.")

# Exemple d'utilisation
salle = SalleCinema(50)

salle.reserver_place("Armel", 5)
salle.reserver_place("Joel", 10)
salle.reserver_place("Rolande", 15)
salle.reserver_place("Karine", 21)

salle.afficher_places_reservees()