#!/usr/bin/python

import cgi
import cgitb
import os
import sys
import subprocess

# This is the server script controller that takes the input from the HTML form
# in alarm.html and sends it to various system commands:
#
# To stop and remove an alarm: run stopalarm.bash
#
# To print the current crontab on the browser: call print_crontab() which calls "crontab -l"
#
# To set a new alarm: run setalarm.bash with the hour and minute taken from the form variables

cgitb.enable()
print "Content-type: text/html\n"
print "<html><head><style> body {font-family: sans-serif; font-size:70px}"
print "#time-box { display: inline-block; font-size: 80px; padding: 20px; background-color: #AAFFAA; }"
print "</style></head><body>\n"

form = cgi.FieldStorage()

def has_var(var):
    return (var in form and form[var].value != "")

def print_crontab():
    try:
        output = subprocess.check_output(['crontab','-l'])
        print output.replace("\n", "<br>")
    except:
        print "Crontab empty."

if(has_var("remove_alarm")):
    command = "/home/pi/alarm/stopalarm.bash > /dev/null"
    os.system(command)
    print "Alarm removed!"

elif(has_var("check_crontab")):
    print_crontab()

elif(has_var("alarm_hour") and has_var("alarm_minute")):
    hour = int(form['alarm_hour'].value)
    minute = int(form['alarm_minute'].value)
    
    if(hour < 0 or hour > 23 or minute < 0 or minute > 59):
        print "Invalid time format. Try again"
    else:
        command = "/home/pi/alarm/setalarm.bash %s %s > /dev/null" % (hour, minute)
        os.system(command)
        print "Alarm set: <br/><div id='time-box'>%s:%s</div>" % (hour, minute)
        print "<br>"
        print_crontab()

else:
    print "Input error. Try again."

print "</body></html>"
