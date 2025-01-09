#!/usr/bin/python3
from core_job_handler import day_selection, pop_up
import datetime
import os


while True:
    pop_up_message = ''
    date_today = datetime.datetime.today().date()
    try:
        file_with_date = open(f'/usr/bin/job_handler/core_job_handler/Data_Saved/{date_today}', 'r').readlines()
        for data in file_with_date:
            pop_up_message = pop_up_message + '\n' + data
        os.remove(f'/usr/bin/job_handler/core_job_handler/Data_Saved/{date_today}')
        pop_up.Pop_up(pop_up_message)
    except:
        pass
    

