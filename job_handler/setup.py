#!/usr/bin/python3
import os
service = """
[Unit]
Description=Job Handler
After=graphical.target
Requires=graphical.target

[Service]
ExecStart=/usr/bin/python3 /usr/bin/job_handler/run.py
Enviroment=Display=:1

[Install]
WantedBy=graphical.target"""

script = """#!/usr/bin/python3
import os
os.system('sudo python3 /usr/bin/job_handler/add_date.py')
"""



os.system(f'sudo cp -r ../job_handler /usr/bin')
os.system(f'sudo touch /lib/systemd/system/job_handler.service; sudo echo "{service}" > /lib/systemd/system/job_handler.service')

os.system(f'sudo echo "{script}" > /usr/local/bin/make_date')

os.system(f'sudo chmod 777 /usr/local/bin/make_date')
os.system(f'sudo chmod 777 /usr/bin/job_handler/*')


#colocar o add_date no /usr/local/bin

