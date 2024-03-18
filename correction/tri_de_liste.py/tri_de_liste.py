"""
Écrivez une fonction appelée tri_croissant qui prend une liste de nombres
en entrée et renvoie une nouvelle liste contenant les mêmes éléments triés
par ordre croissant.
"""
def creer_liste ():
    liste = []
    # control de saisir pour la taille de la liste 
    while True:
        try:
            taille = int(input("saisir la taille de votre liste :"))
            if taille > 0 :
                break
            else :
                print("saisit un nombre positif SVP !")
        except ValueError:
            print ("vellez entres un monbre SVP !")
    # remplissage de la liste 
    """ while True :
       # try :
            for i in range (1,taille):
                element = int(input(f"entrez votre {i} element :"))
                break
                element.append
    """
    for i in range (0,taille):
        while True:
            try:
                element = int(input(f"entrez votre {i+1} element :"))
                liste.append(element)
                break
            except ValueError:
                print("on a besoin que des nombres")
    return liste

def tri_croissant(liste:list):
    return sorted(liste)


liste = creer_liste()
liste_trie = tri_croissant(liste)
print(liste_trie)  