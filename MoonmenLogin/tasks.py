from celery.task.schedules import crontab
from celery.decorators import periodic_task, task

from MoonmenLogin.models import SaveCounterAdvanced
from django.db.models import F
from datetime import datetime

@periodic_task(run_every=(crontab(minute="*/02")), name="reset_counter", ignore_result=True)
"""
Runs at every 2 miutes, sets counter to 0 at every end of 2 minutes
"""
def counter_set():
	counterDbObject = SaveCounterAdvanced.objects.get_or_create(uniqueId=1)
	currentTime = datetime.now()
	report(counterDbObject[0].saveCount,currentTime)
	counterDbObject[0].saveCount = 0
	counterDbObject[0].save()

@task(name="increment_of_counter")
"""
Called to increase the counter variable
"""
def increment():
	counterDbObject = SaveCounterAdvanced.objects.get_or_create(uniqueId=1)
	counterDbObject[0].saveCount = F('saveCount') + 1
	counterDbObject[0].save()
	
def report(countAtEnd, currentTime):
"""
generates a file containing no. of users saved at end of every 2 minutes, just before reset
'countAtEnd' -> conatins count just before reset
'currentTime' -> Sends time before reset
"""
	reportFile = "SavedUsers_" + currentTime.strftime("%H%M%S") + ".txt"
	f = open(reportFile, "w")
	content = "The No.of users saved are " + str(countAtEnd)
	f.write(content)
	f.close()