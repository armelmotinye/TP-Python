import mysql.connector

# Etablir une connexion a la base de donnee
connexion = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'crudpython'
)

def create_user(nom, email):
    cursor = connexion.cursor()
    cursor.execute("""
        INSERT INTO utilisateurs (nom, email)
        VALUES (%s, %s)
    """, (nom, email))
    connexion.commit()

def read_users():
    cursor = connexion.cursor()
    cursor.execute("SELECT * FROM utilisateurs")
    for (id, nom, email) in cursor:
        print(f"ID: {id}, Nom: {nom}, Email: {email}")
def update_user(id, email):
    cursor = connexion.cursor()
    cursor.execute("""
       UPDATE utiisateurs
       SET email= %s
       WHERE id= %s
     """, (email, id))
    connexion.commit()

    def delete_user(id):
        cursor = connexion.cursor
        cursor.execute("""
       DELETE FROM utiisateurs
       SET email= %s
       WHERE id= %s
     """, (email, id))
    connexion.commit()

# create_user("Armel", "motar@gmail.com")
read_users()
update_user(1, "joel@gmail.com")