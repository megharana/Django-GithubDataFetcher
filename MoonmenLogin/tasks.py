from celery.task.schedules import crontab
from celery.decorators import periodic_task,task
from datetime import timedelta
from MoonmenLogin.models import SaveCounterAdvanced
from django.db.models import F


@periodic_task(run_every=(crontab(minute="*/15")), name="some_task", ignore_result=True)
# @periodic_task(run_every=timedelta(seconds=30), name="some_task")
def counter_set():
	"""setting the counter to 0"""
	counterDbObject=SaveCounterAdvanced.objects.get_or_create(uniqueId=1)
	counterDbObject[0].saveCount = 0
	counterDbObject[0].save()

# c=SaveCounter.objects.get_or_create(saveCount=0)
@task(name="increment_of_counter")
def increment():
	"""increment of counter """
	counterDbObject=SaveCounterAdvanced.objects.get_or_create(uniqueId=1)
	counterDbObject[0].saveCount = F('saveCount') + 1
	counterDbObject[0].save()
	




# from celery.decorators import per


# @task(name="sum_two_numbers")
# def add():
# 	counter


