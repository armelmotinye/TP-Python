"""
L'objectif de cet exercice est de créer deux classes en Python pour modéliser un système d'école : une classe Student pour représenter les étudiants et une classe Course pour représenter les cours.
"""

# Création de la classe Student en Définissant un constructeur __init__()
class Course:
    def __init__(self, name, credits):
        self._name = name
        self._credits = credits

    @property
    def name(self):
        return self._name

    @property
    def credits(self):
        return self._credits

    def __str__(self):
        return f"{self._name} ({self._credits} crédits)"

# Création de la classe Course en Définissant un constructeur __init__()

class Student:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        self._courses = []

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def courses(self):
        return self._courses

    def add_course(self, course):
        self._courses.append(course)

    def display_details(self):
        print(f"Nom : {self._name}")
        print(f"Age : {self._age}")
        print("Cours suivis :")
        for course in self._courses:
            print(f"- {course}")


# Création des instances de la classe Course
mathematiques = Course("Mathématiques", 4)
histoire = Course("Histoire", 3)
science = Course("Science", 5)
francais = Course("Français", 3)

# Création des instances de la classe Student
etudiant1 = Student("Alice", 20)
etudiant2 = Student("Bob", 22)

# Ajout des cours aux étudiants
etudiant1.add_course(mathematiques)
etudiant1.add_course(histoire)
etudiant2.add_course(science)
etudiant2.add_course(francais)

# Affichage des détails des étudiants avec les cours suivis
print("Etudiant 1 :")
etudiant1.display_details()
print()

print("Etudiant 2 :")
etudiant2.display_details()


def ajouter_etudiant():
    nom = input("Entrez le nom de l'étudiant : ")
    age = int(input("Entrez l'âge de l'étudiant : "))
    return Student(nom, age)


# Menu d'ajout d'étudiants
etudiants = []

while True:
    print("\n--- Menu ---")
    print("1. Ajouter un nouvel étudiant")
    print("2. Afficher les détails des étudiants")
    print("3. Quitter")

    choix = input("Choisissez une option : ")

    if choix == "1":
        etudiant = ajouter_etudiant()
        etudiants.append(etudiant)
        print("Etudiant ajouté avec succès.")
    elif choix == "2":
        print("\nDétails des étudiants :")
        for etudiant in etudiants:
            etudiant.display_details()
            print()
    elif choix == "3":
        print("Programme terminé.")
        break
    else:
        print("Option invalide. Veuillez entrer un nombre entre 1 et 3.")