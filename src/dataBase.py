import sqlite3

def createTable():
    connection = sqlite3.connect('BaseDeDonnee.db')

    connection.execute("CREATE TABLE IF NOT EXISTS USERS(USERNAME TEXT NOT NULL,EMAIL TEXT,PASSWORD TEXT)")

    connection.execute("CREATE TABLE IF NOT EXISTS ETUDIANT(IDETUDIANT TEXT NOT NULL,ETUDIANTNAME TEXT ,MATRICULE TEXT,CLASSE TEXT,IMAGE BLOP)")

    connection.execute("INSERT INTO USERS VALUES(?,?,?)",('admin','admin','admin'))

    connection.commit()

    result = connection.execute("SELECT * FROM USERS")
    
    for data in result:
        print("Username : ",data[0])
        print("Email : ",data[1])
        print("Password :",data[2])

    connection.close()

createTable()
        
    
