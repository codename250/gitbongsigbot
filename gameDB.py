import sqlite3
def GameRegister(userid):
    con = sqlite3.connect("Test2.db", isolation_level = None)
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS User_Info(id INTEGER PRIMARY KEY, 전투력 TEXT, 공격력 INTEGER, 마법공격력 INTEGER, 힘 INTEGER, 민첩 INTEGER, 지능 INTEGER, 공격속도 INTEGER, create_date TEXT)")

  
    cur.execute("SELECT id FROM UserInfo WHERE id = ?", (id,))
    rows = cur.fetchall()

    for i in rows :
        alr_exist.append(i[0])
    if id not in alr_exist :
        cur.execute("INSERT INTO User_Info VALUES(?, ?, ?, ?, ?,?,?,?,?)", (userid, 5959, 8282, 10000, 1,2,3,4,"5"))
        return 0
    elif id in alr_exist :
        return 1
    con.close

    
    
    
    #cur.execute("INSERT INTO User_Info VALUES(?, ?, ?, ?, ?)", (123456787, "OO은행", "1234-1234-165412", 10000, "2021-02-21"))


