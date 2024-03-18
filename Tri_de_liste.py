def tri_croissant(liste):
    """
    Trie une liste de nombres par ordre croissant.
    
    Args:
    - liste : une liste de nombres
    
    Returns:
    - Une nouvelle liste contenant les mêmes éléments triés par ordre croissant
    """
    try:
        sorted_list = sorted(liste)
        return sorted_list
    except TypeError:
        print("Erreur : La liste contient des éléments non comparables.")
        return []

# Test de la fonction
while True:
    try:
        elements = input("Entrez les nombres séparés par des espaces : ").split()
        elements = [float(element) for element in elements]
        sorted_elements = tri_croissant(elements)
        print("Liste triée par ordre croissant :", sorted_elements)
        break
    except ValueError:
        print("Erreur : Veuillez entrer des nombres valides.")
