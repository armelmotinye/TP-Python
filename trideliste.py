def creer_liste ():
    liste = []
    while True:
        elements = input("entrer le prochain nombre ou q pour quitter")
        if elements.lower() == 'q':
            break
        try:
            nombre = int(elements)
            liste.append(nombre)
        except ValueError:
            print("veillez entrer un nombre valide ou q pour terminer")
    return liste
def trie_croissant(liste:list):
    return sorted(liste)
liste = creer_liste()
liste_trie = trie_croissant(liste)
print(liste_trie)
