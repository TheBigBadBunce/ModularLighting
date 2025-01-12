from random import randint
from datetime import datetime, date, timedelta

def vary_time(time, variance):
    """Randomly adjusts a given time by `variance` minutes"""
    dt_time = datetime.combine(date.today(), time)
    min_DT_time = dt_time - timedelta(minutes=variance)
    minutes_added = randint(0, variance)
    return (min_DT_time + timedelta(minutes=minutes_added)).time()