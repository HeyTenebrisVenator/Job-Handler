#!/usr/bin/python3
from core_job_handler import day_selection, pop_up
import datetime
import os

past_days = []
sent = False
while True:
    pop_up_message = ''
    date_today = datetime.datetime.today().date()
    if date_today not in past_days:
        past_days.append(date_today)
        sent = False
    try:
        file_with_date = open(f'/usr/bin/job_handler/core_job_handler/Data_Saved/{date_today}', 'r').readlines()
        for data in file_with_date:
            pop_up_message = pop_up_message + '\n' + data
        if sent == False:
            pop_up.Pop_up(pop_up_message)
            sent = True
    except:
        pass
    

