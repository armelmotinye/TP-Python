import mysql.connector as mysql
connect_db = mysql.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "ecole",
)

cursor = connect_db.cursor() 
def insertion():
    sql ="INSERT INTO etudiant(code_permanent, nom, prenom, date_naissance, specialite) values('NOUR2201', 'Tekam', 'Rolande', '1987-01-22', 'Medecine')"
    cursor.execute(sql)

    connect_db.commit()
def afficher():
    sql = "SELECT * FROM etudiant "
    cursor.execute(sql)
    # Recuperation des donnees
    etudiants = cursor.fetchall()
    
    for etudiant in etudiants:
        print(etudiant)
# insertion()
afficher()

