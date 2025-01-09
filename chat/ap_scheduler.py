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
    XX = cursor.fetchall()
    print(XX)
    lst = []
    for i in range(len(XX)):
        lst.append(XX[i][0])
    print("qawsedrf"+str(lst))
    zenkai = list(DifferentialNum.objects.all().values())[0]
    
    if zenkai[0] is null:
        zenkai = 0
    if zenkai != sum(lst):
        print("更新あり")
        
    else:
        print("更新なし")
        
    print(zenkai)
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
    scheduler.add_job(notice, 'interval', seconds=30)
    scheduler.start()