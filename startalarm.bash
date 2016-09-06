#!/bin/bash

# turn on the TV
echo "on 0" | cec-client -s > /dev/null

sleep 10

# set this client as the active source
echo "as" | cec-client -s > /dev/null

sleep 10

musicpath='/home/pi/Music'

# number of files in the music dir
Nfiles=`ls $musicpath | wc -l`

# pick a random number r
let "filenum=$RANDOM % $Nfiles + 1"

# choose the rth file in the dir
file=`ls $musicpath | head -$filenum | tail -1`

# play that music file 20 times
mpg123 --loop 20 "$musicpath/$file"


