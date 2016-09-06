#!/bin/bash

if [ $# -lt 2 ]; then
  echo "setalarm hour minute"
  exit
fi

hour=$1
minute=$2

echo $hour:$minute

# set the crontab at $hour:$minute
(crontab -l 2>/dev/null ; echo "$minute $hour * * * /home/pi/alarm/startalarm.bash") | crontab

crontab -l
