#!/bin/bash
set -euo pipefail

while true
do
    export DISPLAY=:0.0
    battery_percent=$(acpi -b | grep -P -o '[0-9]+(?=%)')
    if on_ac_power; then
        if [ "$battery_percent" -gt 98 ]; then
            notify-send -i "$PWD/batteryfull.png" "Battery full." "Level: ${battery_percent}% " &&
            espeak -s 125 -v english+f4 "Hey starry! your battery is fully charged. Please remove your charger right away!"
        fi
    fi
    sleep 300 # (5 minutes)
done
