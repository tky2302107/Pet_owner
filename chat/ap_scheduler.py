from datetime import datetime, date
from apscheduler.schedulers.background import BackgroundScheduler
from .models import Message
from accounts.models import User
from contents.models import NoticeList
import datetime


def notice():#https://techis.jp/guide/django/django_insert_data
    pass
""" #チャットの投稿を通知に反映する部分
    model = User,Message,NoticeList
    dt_now = datetime.datetime.now()
    
    NoticeList.objects.all()
    for i in range("前回更新時以降に増えた投稿の数"):
        nl = NoticeList(posted_at=dt_now,title="チャットメッセージ",text="chatroom"+"に新規メッセージが届きました。")
        nl_list.append(nl)
    for j in nl_list:
        j.save()

""" 

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(notice, 'interval', seconds=30)
    scheduler.start()