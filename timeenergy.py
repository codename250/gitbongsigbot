import threading
import sqlite3
import datetime
import random
import numpy as np
i=1
userid=414818708582825984
def charge_energy():

    global i
    con = sqlite3.connect("PreRegister.db", isolation_level=None)
    cur = con.cursor()
    cur.execute("SELECT 최대행동력 FROM User_Info")  # *는 전부라는 의미, 따라서 users로부터 모든것을 선택
    maxen = cur.fetchall()

    #print('usernum=',lenmaxen))
    
    if i!=0:
        cur.execute("SELECT * FROM User_Info")  # *는 전부라는 의미, 따라서 users로부터 모든것을 선택
        nowen= cur.fetchall()
        for usernum in range(0,len(maxen)-1):
            
            
            aa=nowen[usernum][1]
            
            
            newenergy=nowen[usernum][14]+1
            print(aa)
            if newenergy<=nowen[usernum][13]:
                print('usernum=',usernum,'___','newenergy=',newenergy)
            
                cur.execute("UPDATE User_Info SET 현재행동력 = ? WHERE id = ?", (newenergy, aa,))
            else :
                print('Energy is already max')

        
            

        i=i+1

charge_energy()

