# Job-Handler

ATTENTION: JOB HANDLER ONLY WORKS IN LINUX

Job handler is a program that helps you in your daily tasks. 

The Function of this is to send you notifications when today's date reaches the programmed date

First, it's important to install all the modules at requirement.txt

To do this, just use the command:
*pip install -r requirement.txt*

After this, you can make the instalation executing the setup.py

So, after all this, just execute the command:

*sudo systemctl start job_handler*

To stop, use:

*sudo systemctl stop job_handler*

To configure a new date, use the command:

sudo make_date
