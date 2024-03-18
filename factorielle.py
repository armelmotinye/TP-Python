def factorielle(z):
    """
    Calcule la factorielle d'un entier z.
    
    Args:
    - z : un entier
    
    Returns:
    - La factorielle de z
    """
    if z == 0:
        return 1
    else:
        return z * factorielle(z - 1)

# Test de la fonction avec contrôle de sécurité
while True:
    try:
        entier = int(input("Entrez un entier positif : "))
        if entier < 0:
            raise ValueError("Entrez un entier positif.")
        print("La factorielle de", entier, "est", factorielle(entier))
        break
    except ValueError as e:
        print(e)
