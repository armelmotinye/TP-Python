def est_pair(nombre):
    """
    Vérifie si un entier est pair en demandant à l'utilisateur d'entrer un entier.
    
    Returns:
    - True si l'entier est pair, False sinon
    """
    while True:
        try:
            entier = int(input("Entrez un entier : "))
            return True
        except ValueError:
            print("Veuillez entrer un entier valide.")

# Test de la fonction
resultat = est_pair(nombre)
print("L'entier est pair :", resultat)