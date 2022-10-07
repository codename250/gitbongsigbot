import sqlite3
import datetime
import random
# 내 스텟스킬 , 몬스터 스텟스킬 불러오기
userid=414818708582825984
def Fight(userid, monsterid):
    
    
    con = sqlite3.connect("PreRegister.db", isolation_level=None)
    cur = con.cursor()
    
    cur.execute("SELECT * FROM User_Info WHERE id = ?", (userid, ))
    temp999 = cur.fetchall()
    cur.execute("SELECT * FROM Skill_Info WHERE 스킬1 = ?", ('A', ))
    temp997 = cur.fetchall()
    print(temp997)

    
    print(temp999)
    cur.execute("SELECT * FROM Monster_Info WHERE id = ?", (monsterid, ))
    temp998 = cur.fetchall()
    #temp999[0][?]
    # 0-id 1-닉네임 2-전투력 3-물리공격력 4-마법공격력 5-힘 6-민첩 7-지력 8-공격속도
    # 9-명중률 10- 회피율 11-최대HP 12-현재HP 13-최대행동력 14-현재행동력 15- CREATE-DATE
    mynick=temp999[0][1]
    mypower=temp999[0][2]
    myaddam=temp999[0][3]
    myapdam=temp999[0][4]
    mystr=temp999[0][5]
    mydex=temp999[0][6]
    myint=temp999[0][7]
    myatkspeed=1/temp999[0][8]
    myaccu=temp999[0][9]
    myaccu=temp999[0][9]
    myvoid=temp999[0][10]
    mymaxhp=temp999[0][11]
    #화이팅화이팅
    
    myhp=temp999[0][12]
    energy=temp999[0][14]

    #### 몬스터 스텟
    #print(temp998)
    #print(temp998[0][0])
    
    monsnick=temp998[0][1]
    monspower=temp998[0][2]
    monsaddam=temp998[0][3]
    monsapdam=temp998[0][4]
    monsstr=temp998[0][5]
    monsdex=temp998[0][6]
    monsint=temp998[0][7]
    monsatkspeed=1/temp998[0][8]
    monsaccu=temp998[0][9]
    monsaccu=temp998[0][9]
    monsvoid=temp998[0][10]
    monsmaxhp=temp998[0][11]
    
    monshp=temp998[0][12]
    


    
   # 레하레하~^^


    

    
    
      
    # 행동력 확인 및 소모
    if energy >= 1:
        # 전투
        # 30초동안 싸움
        timerend=30
        timerstart=0
        
        T3=0
        # 몬스터의 공격시간과 내 공격시간 [ 쿨타임은 따로 stack? 또는 tiktok ]
        # 공격쿨타임은 1/공격속도 sec
        
        #monsatkspeed=1/temp998[0][8]
        
        #선빵
        if monsatkspeed>=myatkspeed:
            T1=myatkspeed
            T2=monsatkspeed
                #몬스터 공격 페이
            T3=T1
        else:
            T1=myatkspeed
            T2=monsatkspeed
            T3=T2
            
        while T3<timerend:
            if T1<=T2 : #T1. 플레이어 공격턴
                T3=T1   #현재시간
                T1=T1+myatkspeed #다음 플레이어 공격시간
                               
                #ATK Phaze

                
                # 공격방법은 평타+랜덤스킬
                     #공격방법 선택후 공격
                # 공격 데미지 계산 / 방어력 / 공격력 / 마법공격력
                #atkmethod=skills[randint(0,len(skills))]
                myatkdam=myaddam #임시
                
                
                # 공격 HIT확률 계산 / 미스 / 명중 / 크리
                hit=random.randint(0,101)
                monsavoid=random.randint(0,101)
                print('time=',T3,'Player Attack Phaze')
                
                if hit<=2:#critical
                    dam=myaddam*2
                    monshp=monshp-dam
                    print('critical!! damage =',dam)
                elif myaccu <= hit or monsavoid <= monsvoid:#miss
                    print('miss!','hit',hit,'monsavoid',monsavoid)
                    print('miss!')
                    pass
                else: #명중
                    dam=myaddam
                    monshp=monshp-dam
                    print('damage =',dam)
                print('monshp',monshp,'/',monsmaxhp)
                
                if monshp<=0:
                    print('monster died')
                    break
            else: 
                 #T2. 몬스터  공격턴
                T3=T2   #현재시간
                T2=T2+monsatkspeed #다음 플레이어 공격시간
                               
                #ATK Phaze

                
                # 공격방법은 평타+랜덤스킬
                     #공격방법 선택후 공격
                # 공격 데미지 계산 / 방어력 / 공격력 / 마법공격력
                #atkmethod=skills[randint(0,len(skills))]
                monsatkdam=monsaddam #임시
                #ad공-ad방
                #ap공-ap방
                #트루뎀
                ## 피격 데미지반사, 가격 데미지흡수, 체력회복
                
                
                # 공격 HIT확률 계산 / 미스 / 명중 / 크리
                hit=random.randint(0,101)
                # 명중률, 회피율, 크리확률
                myavoid=random.randint(0,101)
                
                print('time=',T3,'Monster Attack Phaze')
                
                if hit<=2:#critical
                    dam=monsaddam*2
                    myhp=myhp-dam
                    print('critical!! damage =',dam)
                elif monsaccu <= hit or myavoid <= myvoid:#miss
                    
                    print('miss!')#,'hit',hit,'myavoid',myavoid)
                    pass
                else: #명중
                    dam=monsaddam
                    myhp=myhp-dam
                    print('damage =',dam)
                print('myhp',myhp,'/',mymaxhp)
                
                if myhp<=0:
                    print('you died')
                    break
            if T3>=30:
                print('Time out')
            
        #행동력 소모
        energy=energy-1
        cur.execute("UPDATE User_Info SET 현재행동력 = ? WHERE id = ?", (energy, userid,))
    elif energy == 0 :
        print('No energy')

        # 비전투



# 공격방법은 평타+랜덤스킬
# 공격 HIT확률 계산 / 미스 / 명중 / 크리
# 공격 데미지 계산 / 방어력 / 공격력 / 마법공격력
#// 물리방어력과 마법방어력, 방어관통력 크리티컬시 데미지 얼마?

# 내 체력이 0이되면 패배
# 몬스터 체력이 0이되면 승리
# 30초가 지나면 무승부[사실상 패배]
# 보상시스템



    con.close
Fight(userid,1)
