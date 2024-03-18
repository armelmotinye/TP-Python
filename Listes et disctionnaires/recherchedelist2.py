# saisie du nombre d'étudiants
nombre_etudiants = int(input("Entrez le nombre d'étudiants : "))

# Création d'un dictionnaire vide pour stocker les informations des étudiants
etudiants = {}

# Boucle pour saisir les noms et les notes des étudiants
for i in range(nombre_etudiants):
    nom = input(f"Entrez le nom de l'étudiant {i+1} : ")
    note = int(input(f"Entrez la note de {nom} : "))
    etudiants[nom] = note

    # Affichage des noms des étudiants ayant obtenu une note supérieure ou égale à 10
print("Noms des étudiants avec une note supérieure ou égale à 10 :")
for nom, note in etudiants.items():
    if note >= 10:
        print(nom)
        