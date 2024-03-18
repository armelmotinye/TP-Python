def est_present(liste, valeur):

    if not liste:
        return False

    try:
        return valeur in liste
    except TypeError:
        print("Erreur : La liste n'est pas valide.")
        return False

# Test de la fonction
liste = input("Entrez les éléments de la liste séparés par des espaces : ").split()
valeur = input("Entrez la valeur à rechercher dans la liste : ")

if est_present(liste, valeur):
    print(f"La valeur {valeur} est présente dans la liste.")
else:
    print(f"La valeur {valeur} n'est pas présente dans la liste.")