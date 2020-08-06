#!/bin/bash
ifconfig wlan0 10.10.48.5 netmask 255.255.0.0
ip route add 10.10.0.0/16 dev wlan0
route add default gw 10.10.0.254
