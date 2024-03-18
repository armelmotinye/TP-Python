def pgcd():
    """
    Calcule le plus grand commun diviseur (PGCD) de deux entiers en demandant à l'utilisateur d'entrer les entiers.
    
    Returns:
    - Le PGCD des deux entiers saisis par l'utilisateur
    """
    while True:
        try:
            a = int(input("Entrez le premier entier : "))
            b = int(input("Entrez le deuxième entier : "))
            while b:
                a, b = b, a % b
            return a
        except ValueError:
            print("Veuillez entrer des entiers valides.")

# Test de la fonction
pgcd_result = pgcd()
print("Le PGCD est :", pgcd_result)