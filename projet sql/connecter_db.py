import mysql.connector

# Fonction pour se connecter à la base de données
def connecter_bd():
        connect = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ecole"
        )
        return connect
    
connect = connecter_bd()
# Fonction pour insérer un étudiant dans la base de données
def inserer_etudiant(connect, code_permanent, nom, prenom, date_naissance, specialite):
    
        cursor = connect.cursor()
        sql = "INSERT INTO Etudiant (code_permanent, nom, prenom, date_naissance, specialite) VALUES (%s, %s, %s, %s, %s)"
        val = (code_permanent, nom, prenom, date_naissance, specialite)
        cursor.execute(sql, val)
        connect.commit()
        print(f"{cursor.rowcount} étudiant(s) inséré(s) avec succès.")
    

# Fonction pour afficher tous les étudiants de la base de données
def afficher_etudiants(connect):
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM Etudiant")
        etudiants = cursor.fetchall()
        for etudiant in etudiants:
            print(etudiant)

   

# Menu principal
def menu_principal():
    while True:
        print("\nMenu Principal:")
        print("1. Insérer un étudiant")
        print("2. Afficher tous les étudiants")
        print("3. Quitter")
        choix = input("Votre choix : ")
        if choix == "1":
            code_permanent = input("Entrez le code permanent de l'étudiant : ")
            nom = input("Entrez le nom de l'étudiant : ")
            prenom = input("Entrez le prenom de l'étudiant : ")
            date_naissance = input("Entrez la date de naissance de l'étudiant : ")
            specialite = input("Entrez la specialite de l'étudiant : ")
            inserer_etudiant(connect, code_permanent, nom, prenom, date_naissance, specialite)
        elif choix == "2":
            afficher_etudiants(connect)
        elif choix == "3":
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez choisir à nouveau.")

# Point d'entrée du programme
if __name__ == "__main__":
   menu_principal()
