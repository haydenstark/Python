


import sqlite3

peopleValues = (('Ron', 'Obvious', 42), ('Luigi', 'Vercotti', 43), ('Arthur', 'Belling', 28))

with sqlite3.connect("test_database.db") as connection:
    c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS tbl_people")
    c.executescript("CREATE TABLE tbl_people (FirstName TEXT, LastName TEXT, Age INT)")
    c.executemany("INSERT INTO tbl_people VALUES (?, ?, ?)", peopleValues)
    c.execute("SELECT FirstName, Lastname FROM tbl_people WHERE Age > 30")
    while True:
        row = c.fetchone()
        if row is None:
            break
        print(row)
        
    #for row in c.fetchall():
        #print(row)
        
    #c.execute("UPDATE tbl_people SET Age=? WHERE FirstName=? AND LastName=?",
              #(45, 'Luigi', 'Vercotti'))
