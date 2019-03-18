import subprocess as s
import notify2
import time
from datetime import datetime

from apscheduler.scheduler import Scheduler
# s.call(['notify-send']


def job_function():
    #notify2.init('notifications')
    hour=datetime.now().strftime('%H:%M')
    if hour=='12:46':
        s.Popen(['notify-send', 'message'])
    elif hour=='13:30':
        s.Popen(['notify-send', 'message'])
    elif hour =='17:30':
        s.Popen(['notify-send', 'message'])
    elif hour =='18:30':
        s.Popen(['notify-send', 'message'])
    else:
        pass

sched = Scheduler()
sched.start()
sched.add_cron_job(job_function, minute=1)