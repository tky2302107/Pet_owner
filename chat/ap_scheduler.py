from datetime import datetime, date
from apscheduler.schedulers.background import BackgroundScheduler
from .models import Message,Room
from accounts.models import User
from contents.models import NoticeList,DifferentialNum,PersonalNoticeList
import sqlite3
import datetime

def notice():#https://techis.jp/guide/django/django_insert_data
     pass
""" 
    cursor = sqlite3.connect("db.sqlite3").cursor()
    cursor.execute('SELECT * FROM chat_message')
    Chatdata = cursor.fetchall()
    cursor.execute('SELECT * FROM accounts_user')
    Userdata = cursor.fetchall()
    print("")
    print(Chatdata)
    print("")
    lst = []
    new = []
    for i in range(len(Chatdata)):
        lst.append(Chatdata[i][0])
    print("chat_id_list"+str(lst))
    
    cursor.execute("SELECT num FROM contents_differentialnum WHERE id=1")
    start = int(list(cursor.fetchall())[0][0])
    
    print("\nraw start "+str(start))
    
    end = int(lst[-1])    #最新
    for i in range(len(Chatdata)):
        if int(Chatdata[i][0]) >= start :
            print(i)
            new.append(Chatdata[i])

    print("")
    print("new")
    print(new)

    if new is None :
        pass
    else:
        savedata = []
        for i in range(len(new)):
            savedata.append(PersonalNoticeList(old_id=new[i][0],text=new[i][1],date=new[i][2],user=new[i][3],chargroup=new[i][4]))
        PersonalNoticeList.objects.bulk_create(savedata)
        d = DifferentialNum.objects.filter(id=1)
        d.update(num=end+1)

    
    #チャットの投稿を通知に反映する部分
    last_count = 0
    model = User,NoticeList,Room
    
    queryset = Room.objects.all()
    
    dt_now = datetime.datetime.now()
    #自分が所属するチャットルームのルームIDを取得

    #ルームIDが自分のものと一致するメッセージを取得
    message_count = int(Message.objects.filter().values("id").count())
    differential = message_count- last_count 
    NoticeList.objects.all()
    cursor.close()
""" 

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(notice, 'interval', seconds=60)
    scheduler.start()