from datetime import datetime, date
from apscheduler.schedulers.background import BackgroundScheduler
from .models import Message,Room
from accounts.models import User
from contents.models import NoticeList,DifferentialNum
import sqlite3
import datetime


def notice():#https://techis.jp/guide/django/django_insert_data
     pass
 """ 
    # queryset = super().get_queryset()
    
    cursor = sqlite3.connect("db.sqlite3").cursor()
    cursor.execute('SELECT * FROM chat_message')
    Chatdata = cursor.fetchall()
    cursor.execute('SELECT * FROM accounts_user')
    Userdata = cursor.fetchall()
    print("")
    print(Chatdata)
    print("")
    print(Userdata)
    print("")
    lst = []
    sabun = []
    for i in range(len(Chatdata)):
        lst.append(Chatdata[i][0])
    print("sabun_num"+str(lst))
    try:
        zenkai = list(DifferentialNum.objects.all().values())[0]
    except:
        zenkai = []
        zenkai.append(36)
    
    saishin = lst[-1]    #最新
    zenkai = zenkai[0]+1 #前回の更新以降
    for i in range(len(Chatdata)):
        if Chatdata[i][0] >= zenkai :
            sabun.append(Chatdata[i])

    print("")
    print("sabun")
    print(sabun)


        
    
    #チャットの投稿を通知に反映する部分
    last_count = 0
    model = User,NoticeList,Room
    
    queryset = Room.objects.all()
    
    # print("roomqs")
    # print(list(queryset.values()))
    
    # print(Message)
    dt_now = datetime.datetime.now()
    #自分が所属するチャットルームのルームIDを取得

    #ルームIDが自分のものと一致するメッセージを取得
    message_count = int(Message.objects.filter().values("id").count())
    differential = message_count- last_count 




    NoticeList.objects.all()
    # for i in range(0):#"前回更新時以降に増えた投稿の数"
    #     nl = NoticeList(posted_at=dt_now,title="チャットメッセージ",text="chatroom"+"に新規メッセージが届きました。")
    #     nl_list.append(nl)
    # for j in nl_list:
    #     j.save()
    cursor.close()
# """ 

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(notice, 'interval', seconds=10)
    scheduler.start()