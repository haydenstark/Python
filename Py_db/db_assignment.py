

import sqlite3

conn = sqlite3.connect('practice.db')



fileList = ('information.docx','Hello.txt','myImage,png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
lst = list(fileList)
commitList = []

for i in lst:
    if i.endswith(".txt"):
        commitList.append(i)

print("These are the files we're adding to the database:")
print(commitList)


with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileName TEXT)")
    for i in commitList:
        cur.execute("INSERT INTO tbl_files(col_fileName) VALUES (?)", \
                ("{}".format(i),))
    conn.commit()
conn.close()
