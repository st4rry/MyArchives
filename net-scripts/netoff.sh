#!/bin/bash
# My first script

echo "Stoping NetworkManager";
/etc/init.d/network-manager stop;
echo "Killing nm-applet";
kill $(ps -e |grep nm-applet | awk '{print $1}')
sleep 2

