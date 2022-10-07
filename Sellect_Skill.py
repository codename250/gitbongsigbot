import sqlite3
import datetime
import re
import random
# 내 스텟스킬 , 몬스터 스텟스킬 불러오기
userid=414818708582825984
def Fight(userid, monsterid):
    
    
    con = sqlite3.connect("PreRegister5.db", isolation_level=None)
    cur = con.cursor()
    
    cur.execute("SELECT 사용스킬 FROM User_Info WHERE id = ?", (userid, ))
    temp999 = cur.fetchall()
    
    print(temp999[0][0])

    
    print(temp999)
    

    string = temp999[0][0]
    
    numbers = re.findall(r'\d+', string)
    print(numbers)
    skills=numbers[random.randint(0,len(numbers))]
    cur.execute("SELECT 스킬이름 FROM Skill_Info WHERE 스킬번호 = ?", (skills, ))
    temp997 = cur.fetchall()
    print(temp997[0][0],'num=',skills)
    '''
    for skills in numbers :
        cur.execute("SELECT 스킬이름 FROM Skill_Info WHERE 스킬번호 = ?", (skills, ))
        temp997 = cur.fetchall()
        print(temp997[0][0],'num=',skills)
    '''
    cur.execute("SELECT * FROM Monster_Info WHERE id = ?", (monsterid, ))
    temp998 = cur.fetchall()
    #temp999[0][?]
    # 0-id 1-닉네임 2-전투력 3-물리공격력 4-마법공격력 5-힘 6-민첩 7-지력 8-공격속도
    # 9-명중률 10- 회피율 11-최대HP 12-현재HP 13-최대행동력 14-현재행동력 15- CREATE-DATE
    mynick=temp999[0]
Fight(userid,1)
