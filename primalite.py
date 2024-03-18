def est_premier(x):
    """
    Vérifie si un entier est premier.
    
    Args:
    - x : un entier
    
    Returns:
    - True si l'entier est premier, False sinon
    """
    if x <= 1:
        return False
    elif x <= 3:
        return True
    elif x % 2 == 0 or x % 3 == 0:
        return False
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i += 6
    return True

# Test de la fonction avec contrôle de sécurité
while True:
    try:
        entier = int(input("Entrez un entier positif : "))
        if entier < 0:
            raise ValueError("Entrez un entier positif.")
        if est_premier(entier):
            print(f"L'entier {entier} est premier.")
        else:
            print(f"L'entier {entier} x'est pas premier.")
        break
    except ValueError as e:
        print(e)
        