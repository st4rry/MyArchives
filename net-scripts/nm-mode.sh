#!/bin/bash

if [ "$(id -u)" != "0" ]; then
	echo -e "\e[1;31m[!]\e[0m This script must be run as root" 1>&2
	exit 1
fi
# the Input 1
echo “Enter Interface name”
read -p "interface: " interface

# the Input 2
echo “Enter mode”
echo 1. managed
echo 2. not managed
read -p "choice: " choice

case $choice in
1)nmcli device set $interface managed yes
echo $interface is managed.;;
2)nmcli device set $interface managed no
echo $interface is not managed. 
esac

