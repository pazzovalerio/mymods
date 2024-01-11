#!/bin/bash
# GNU bash, version 4.4.20
#sleep 3
pkill -f coin.py
sleep 3
python /home/pi/up0.py
sleep 5
python /home/pi/coin.py
