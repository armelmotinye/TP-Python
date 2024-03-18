def moyenne(nombre):
    liste_nombre = nombre

    while True:
        try:
            nombres = input("Entrez les nombres séparés par des espaces : ").split()
            nombres = [float(nombre) for nombre in nombres]
            return sum(nombres) / len(nombres)
        except ValueError:
            print("Veuillez entrer des nombres valides.")

# Test de la fonction
moyenne_resultat = moyenne(nombre)
print("La moyenne est :", moyenne_resultat)