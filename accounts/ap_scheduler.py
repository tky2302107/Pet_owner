from datetime import datetime, date
from apscheduler.schedulers.background import BackgroundScheduler
from .models import User
from contents.models import NoticeList
from accounts.models import fund
def point_count_reset():
    model = User
    data = {"pt_give":1}
    User.objects.all().update(**data)
    
def point_notice():
    data = {
        "title":"募金状態の定例通知",
        "text":"現在のポイント募金総額は"+str(list(fund.objects.filter().values())[0]["points_sum"])+"ptです。今後もよろしくお願いします。"
        }
    NoticeList.objects.filter().create(**data)
    

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(point_count_reset, "cron", hour=0)#'interval', seconds=30)
    scheduler.add_job(point_notice, 'interval', weeks=1 )
    scheduler.start()