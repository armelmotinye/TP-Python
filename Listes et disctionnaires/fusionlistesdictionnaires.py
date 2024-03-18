# Création des listes de noms et d'âges
noms = ["Armel", "joel", "clarisse", "pauline"]
ages = [25, 30, 35, 18]

# Création du dictionnaire personnes en associant chaque nom à son âge correspondant
personnes = dict(zip(noms, ages))

# Affichage du dictionnaire personnes
print("Dictionnaire personnes:", personnes)

# Ajout d'une nouvelle personne au dictionnaire en utilisant une saisie utilisateur pour le nom et l'âge
nouveau_nom = input("Entrez le nom de la nouvelle personne : ")
nouvel_age = int(input("Entrez l'âge de la nouvelle personne : "))

personnes[nouveau_nom] = nouvel_age

# Affichage à nouveau du dictionnaire personnes après l'ajout
print("Dictionnaire personnes après l'ajout :", personnes)
for (k, v) in personnes.items():
   print ("{k} : {v}")  
   