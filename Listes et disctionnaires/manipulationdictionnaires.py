# Création du dictionnaire personne
personne = {
    "nom": "Armel",
    "age": 40,
    "ville": "St Eustache"
}

# Affichage de la valeur associée à la clé "âge"
print("Âge de la personne:", personne["age"])

# Modification de la valeur associée à la clé "ville" pour "Paris"
personne["ville"] = "Paris"

# Ajout d'une nouvelle paire clé-valeur pour représenter le sexe de la personne
personne["sexe"] = "masculin"

# Suppression de la clé "ville" du dictionnaire
del personne["ville"]

# Affichage du dictionnaire résultant
print("Dictionnaire résultant:", personne)
print("----------------------------------------")
for k,v in personne.items(): # Affichage de la boucle "for"
    print (f"{k} : {v}")
           
