from random import randint
from datetime import timedelta

def vary_time(dt, variance):
    """Randomly adjusts a given datetime by `variance` minutes"""
    min_DT_time = dt - timedelta(minutes=variance)
    minutes_added = randint(0, variance)
    return min_DT_time + timedelta(minutes=minutes_added)