import mysql.connector as mysql 
connexion = mysql.Connect(
    user = "root",
    password = "",
    host = "localhost",
    database = "ecole"
)
requete = connexion.cursor()
requete.execute("select * from etudiant")
result = requete.fetchall()
# print result
for re in result:
    print(re)
    
