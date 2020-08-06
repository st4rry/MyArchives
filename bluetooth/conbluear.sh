#!/bin/bash

echo -e "starting bluetoothctl\n"
echo "***********************************************"
echo -e "St4rry made this script because he's lazy!"
echo "***********************************************"
echo -e "\n"
{

echo -e "power on\n";
echo -e "agent on\n";
echo -e "default-agent\n";
echo -e "pair 4B:57:84:C8:97:3A\n";
echo -e "connect 4B:57:84:C8:97:3A\n";
echo -e "trust 4B:57:84:C8:97:3A\n"; } | bluetoothctl
echo -e "\n"
echo -e "TWS-S2 is successfully connected!\n"
echo "DONE!"
