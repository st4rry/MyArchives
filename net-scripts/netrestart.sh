#!/bin/bash
# My first script



/etc/init.d/network-manager restart;
kill $(ps -e |grep nm-applet |awk '{ print $1 }');

nm-applet;
