import discord
import random
import sqlite3
import datetime


def GameRegister(userid, nickname):
  global nowDatetime
  now = datetime.datetime.now()
  nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')

  alr_exist = []
  con = sqlite3.connect("PreRegister.db", isolation_level=None)
  cur = con.cursor()

  cur.execute(
    "CREATE TABLE IF NOT EXISTS User1_Info(id INTEGER PRIMARY KEY, 닉네임 TEXT,전투력 INTEGER, 물리공격력 INTEGER, 마법공격력 INTEGER, 힘 INTEGER, 민첩 INTEGER, 지력 INTEGER, 공격속도 INTEGER, 명중률 INTEGER, 회피율 INTEGER, 최대체력 INTEGER, 현재체력 INTEGER, 최대행동력 INTEGER, 현재행동력 INTEGER, create_date TEXT, 보유스킬 TEXT, 사용스킬 TEXT, 보유아이템 TEXT, 장착아이템 TEXT)"
  )
  cur.execute(
    "CREATE TABLE IF NOT EXISTS Monster_Info(id INTEGER PRIMARY KEY, 닉네임 TEXT,전투력 INTEGER, 물리공격력 INTEGER, 마법공격력 INTEGER, 힘 INTEGER, 민첩 INTEGER, 지력 INTEGER, 공격속도 INTEGER, 명중률 INTEGER, 회피율 INTEGER, 최대체력 INTEGER, 현재체력 INTEGER, 최대행동력 INTEGER, 현재행동력 INTEGER, create_date TEXT, 보유스킬 TEXT, 사용스킬 TEXT, 보유아이템 TEXT, 장착아이템 TEXT)"
  )
  cur.execute(
    "CREATE TABLE IF NOT EXISTS Skill_Info(스킬1 TEXT, 스킬2 TEXT, 스킬3 TEXT, 스킬4 TEXT)"
  )
  cur.execute(
      "INSERT INTO SKill_Info VALUES(?, ?, ?, ?)",
      ('A','B','C','D' )
      )
  cur.execute(
    "CREATE TABLE IF NOT EXISTS Item_Info(아이템1 TEXT, 아이템2 TEXT, 아이템3 TEXT, 아이템4 TEXT)"
  ) 

  cur.execute("SELECT id FROM User1_Info WHERE id = ?", (userid, ))
  rows = cur.fetchall()

  for i in rows:
    alr_exist.append(i[0])
  if userid not in alr_exist:
    cur.execute(
      "INSERT INTO User1_Info VALUES(?, ?, ?, ?, ?, ?,?,?,?,?,?, ?,?,?,?,?,?,?,?,?)",
      (userid, nickname, 30, 10, 10, 5, 5, 5, 1, 50, 20, 100, 100, 100, 100,
       nowDatetime,'null','null','null','null'))
    con.close
    return 0

  elif userid in alr_exist:
    con.close
    return 1


file = open('token.txt', 'r')

# file 객체에서 문자열을 읽은 후 변수 x에 저장
token = file.read()

channel1 = 1020603460107915264
intents = discord.Intents.all()
client = discord.Client(intents=intents)


@client.event
async def on_ready():  # 봇이 실행 준비가 되었을 때 행동할 것
  print('Logged in as')
  print(client.user.name)  # 클라이언트의 유저 이름을 출력합니다.
  print(client.user.id)  # 클라이언트의 유저 고유 ID를 출력합니다.
  # 고유 ID는 모든 유저 및 봇이 가지고있는 숫자만으로 이루어진 ID입니다.
  print('------')


recom_menu = ['김치찌개', '라면', '부대찌개', '돈부리', '피자', '햄버거', '치킨']

global menu, Menu
menu = 0

recom_menudata = []
f = open("menu.txt", "rt", encoding='UTF8')
while True:
  line = f.readline().strip()
  if not line: break
  recom_menudata.append(line)


@client.event
async def on_message(message):  # 입력되는 메세지에서 찾기
  global menu, Menu
  if message.content == '테스트':
    await message.channel.send("{}|{},hello".format(message.author,
                                                    message.author.mention))
    print('테스트')
    await message.author.send("{}|{},hello".format(message.author,
                                                   message.author.mention))

##
  if message.content == '점메추' or message.content == '저메추' or message.content == '야메추' or message.content == '안메추':

    await message.channel.send(recom_menudata[random.randint(
      0, len(recom_menudata))])

  if message.content.startswith("!추천메뉴추가"):
    await message.channel.send("{}님께서 추천하신 메뉴는 {}입니다".format(
      message.author, message.content[8:]))
    #중복확인이 되어야함.
    #유사한 메뉴는 기록되거나 확인이 필요.
    Menu = message.content[8:]
    await message.channel.send("추천하신 메뉴가 맞다면 Y를 아니라면 N을 입력해주세요.")
    menu = 1
  if message.content == 'Y' and menu == 1:
    recom_menudata.append(Menu)
    f = open("menu.txt", "wt", encoding='UTF8')

    for name in recom_menudata:

      f.write(name + '\n')
      #f.write('A'+'\n')
    await message.channel.send("추천하신 메뉴 {}가 리스트에 추가되었습니다.".format(Menu))
    await message.channel.send("메뉴 리스트를 확인하세요{}.".format(
      recom_menudata[len(recom_menudata) - 3:]))
    menu = 0
  elif message.content == 'N' and menu == 1:
    await message.channel.send("메뉴추천을 위해서 처음부터 다시 진행해주시기 바랍니다.")
    menu = 0

#######################################################################################


#######################################################################################
  if message.content == '봉식이만 혼자 레벨업 회원가입':
    global nick

    username = message.author.id
    return1 = 0
    nick = 1
    await message.channel.send("[!봉혼레닉네임 원하는닉네임]을 입력해주세요.")
  if message.content.startswith("!봉혼레닉네임") and nick == 1:
    nickname = message.content[8:]
    return1 = GameRegister(message.author.id, nickname)

    nick = 0

    if return1 == 0:
      await message.channel.send("{}님께서 지정하신 닉네임은 {}입니다".format(
        message.author, message.content[8:]))

      embed = discord.Embed(
        title="호봉식이만 혼자 레벨업에 가입하신 것을 축하드립니다.",
        description="{}".format(nickname),
        color=0x62c1cc)  # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
      embed.add_field(name="전투력", value="전투력 : " + '30', inline=True)

      embed.add_field(name="체력",
                      value="최대체력 : " + '100' + '\n' + "현재체력 : " + '100',
                      inline=True)
      embed.add_field(name="공격력",
                      value="물리공격력 : " + '10' + '\n' + "마법공격력: " + '10',
                      inline=True)
      embed.add_field(name="스텟",
                      value="힘 : " + '5' + '\n' + '민첩 : ' + '5' + '\n' +
                      '지력 : ' + '5',
                      inline=True)
      embed.add_field(name="부가스텟",
                      value="공격속도 : " + '1' + '\n' + '명중률 : ' + '50' + '\n' +
                      '회피율 : ' + '20',
                      inline=True)
      embed.add_field(name="부가정보",
                      value="행동력 : " + '100/100' + '\n' + "칭호 : " + '늅봉식이' + '\n' + '계정생성일 : ' +  '{}'.format(nowDatetime),inline=True)

      #embed.set_footer(text="하단 설명") # 하단에 들어가는 조그마한 설명을 잡아줍니다
      await message.channel.send(embed=embed)  # embed를 포함 한 채로 메시지를 전송합니다.
      #await message.channel.send("할 말", embed=embed) # embed와 메시지를 함께 보내고 싶으시면 이렇게 사용하시면 됩니다.

    if return1 == 1:
      embed = discord.Embed(
        title="호봉식이만 혼자 레벨업에 가입 실패하셨습니다.",
        description="이미 가입되어있습니다.",
        color=0x62c1cc)  # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
      embed.set_footer(text="오류가 의심되는 경우 연락부탁드립니다.")  # 하단에 들어가는 조그마한 설명을 잡아줍니다
      await message.channel.send(embed=embed)  # embed를 포함 한 채로 메시지를 전송합니다.
      #await message.channel.send("할 말", embed=embed) # embed와 메시지를 함께 보내고 싶으시면 이렇게 사용하시면 됩니다.

#######################################################################################

##  ~는 바보라는 뜻
  if message.content == '우바':
    await message.channel.send('우아가바보라는뜻이다요')
  if message.content == '모귀바':
    await message.channel.send('위이이이잉챱')
  if message.content == '웅바':
    await message.channel.send('웅잉바보라는뜻')
  if message.content == '봉바':
    await message.channel.send('봉식이바보아니라라는뜻')
  if message.content == '노바':
    await message.channel.send('노쓰바보라는뜻')
  if message.content == '레바':
    await message.channel.send('레이바보라는뜻')
  if message.content == '달바':
    await message.channel.send('달아달아밝은달아 이태백에 밝은달곰바보라는뜻')

  if message.content.startswith("안녕하세요"):

    await message.channel.send("반가워요")


## 특정 채널에서만 기능이 작동
  if message.content.startswith("!공지"):
    print(message.channel.id)
    if message.channel.id == channel1:  #공지 명령어를 입력한 채널이 공지명령어 채널인지 확인합니다.
      print(message.channel.id)
      await client.get_channel(channel1).send('공지사항')
    else:
      await message.channel.send("해당 명령어는 이 채널에서 사용하실수 없습니다."
                                 )  #이 메시지를 보내도록 합니다.
      print(message.channel.id)
  #elif message.content.startswith("웅바"):
  #await message.channel.send('웅바보라는뜻')

  if message.content == "특정입력":
    ch = client.get_channel(channel1)
    await ch.send("{} | {}, User, Hello".format(message.author,
                                                message.author.mention))

client.run(token)
