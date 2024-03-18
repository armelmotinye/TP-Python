# Création de la liste de dictionnaires représentant les étudiants
etudiants = [
    {"nom": "Alice", "note": 15},
    {"nom": "Bob", "note": 8},
    {"nom": "Charlie", "note": 12},
    {"nom": "David", "note": 9},
    {"nom": "Eve", "note": 18}
]

# Affichage des noms des étudiants ayant obtenu une note supérieure ou égale à 10
print("Noms des étudiants avec une note supérieure ou égale à 10 :")
for etudiant in etudiants:
    if etudiant["note"] >= 10:
        print(etudiant["nom"])