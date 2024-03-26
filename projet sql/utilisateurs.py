import mysql.connector as mysql

# Fonction de connexion à la base de données MySQL
def connexion_db():
    connexion = mysql.connect(
        user='root',
        password='',
        host='localhost',
        database='ecole'
    )
    return connexion

# Création d'un utilisateur
def create_user(email, password, nom):
    cursor = connexion.cursor()

    sql = "INSERT INTO users(email, password, nom) VALUES(%s,%s,%s)"
    cursor.execute(sql, (email, password, nom))
    connexion.commit()

    return (nom, email)

# Lister utilisateurs
def read_users():
    cursor = connexion.cursor()

    sql = "SELECT * FROM users"
    cursor.execute(sql)
    users = cursor.fetchall()
    for user in users:
        print(user)

# Mettre à jour un utilisateur
def update_user(ID, email, password, nom):
    cursor = connexion.cursor()

    sql = "UPDATE users SET email=%s, password=%s, nom=%s WHERE id=%s"
    cursor.execute(sql, (email, password, nom, ID))
    connexion.commit()

# Supprimer un utilisateur
def delete_user(ID):
    cursor = connexion.cursor()

    sql = "DELETE FROM users WHERE id=%s"
    cursor.execute(sql, (ID,))
    connexion.commit()

# Menu principal
def main_menu():
    while True:
        print("\nMenu principal:")
        print("1. Ajouter un utilisateur")
        print("2. Mettre à jour un utilisateur")
        print("3. Supprimer un utilisateur")
        print("4. Lister les utilisateurs")
        print("5. Quitter")

        choice = input("Choisissez une option : ")

        if choice == "1":
            email = input("Entrez l'adresse e-mail de l'utilisateur : ")
            password = input("Entrez le mot de passe de l'utilisateur : ")
            nom = input("Entrez le nom complet de l'utilisateur : ")
            create_user(ID, email, password, nom)
        elif choice == "2":
            ID = input("Entrez l'ID de l'utilisateur à mettre à jour : ")
            email = input("Entrez la nouvelle adresse e-mail : ")
            password = input("Entrez le nouveau mot de passe : ")
            nom = input("Entrez le nouveau nom complet : ")
            update_user(ID, email, password, nom)
        elif choice == "3":
            ID = input("Entrez l'ID de l'utilisateur à supprimer : ")
            delete_user(ID)
        elif choice == "4":
            print("\nListe des utilisateurs :")
            read_users()
        elif choice == "5":
            print("Au revoir !")
            break
        else:
            print("Option invalide. Veuillez choisir une option valide.")

# Connexion à la base de données
connexion = connexion_db()

# Lancement du menu principal
main_menu()