from datetime import datetime, date
from apscheduler.schedulers.background import BackgroundScheduler
from .models import User

def point_count_reset():
    model = User
    data = {"pt_give":1}
    User.objects.all().update(**data)
    print("point_count_reset")
    

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(point_count_reset, "cron", hour=0)#'interval', seconds=30)
    scheduler.start()