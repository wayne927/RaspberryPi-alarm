# RaspberryPi-alarm

An alarm clock app running on my Raspberry Pi with a web browser interface. A python controller parses input from the HTML interface and then calls various system commands. The alarm jobs are scheduled using crontab.

alarm.html is the browser interface. You can set or stop/remove an alarm, or even print out the current crontab to make sure everything is working. The HTML form sends its input to alarm.py.

alarm.py is the server CGI script that takes input from alarm.html. The script parses the input, and calls setalarm.bash, stopalarm.bash, or crontab -l.

setalarm.bash is a Bash script that takes the hour and the minute as two arguments, and inserts a new crontab job that runs startalarm.bash

stopalarm.bash is another Bash script that stops the app that is playing the music alarm music, and the remove all the alarm clock entries in the crontab.

startalarm.bash is the actual Bash script that plays the music using CEC-client and mpg123. The Raspberry Pi is connected to a TV via HDMI, and CEC-client allows the Pi to control the TV by turning it on and switching the Pi's input (my Pi isn't connected to its own speaker, so it has to turn on the TV to blast music). mpg123 is an mp3 player that came with the Raspbian OS.
