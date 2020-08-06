#!/bin/bash

echo "set wl mode on monitor";
ifconfig | egrep -i --color "wlo|wlan|eth|ath";

echo "Chose your interface: ";
read inter;

echo "Do you want to set your wireless on motnitor mode? (Y/N) :";
read yn;

echo "Your answer is: " $yn "and Your interface is: " $inter ".";

if [ "$yn" == "Y" ] || [ "$yn" == "y" ];

then
  echo "hello";
  ifconfig $inter down;
  iwconfig $inter mode monitor;
  sleep 1;
  iwconfig $inter | egrep -i --color "Mode|mode";
  sleep 2;

elif [ "$yn" == "N" ] || [ "$yn" == "n" ];

then
   echo "Nothing to do...";
   sleep 1;
   exit
   else echo "AnswerError: restart your script...";
fi
