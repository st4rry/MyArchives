#!/usr/bin/env python
import sys

badchar_inchar = ""
unibadchars = [0x00, 0x0A, 0x0D]

for badchar in range (0x00, 0xFF+1):
    if badchar not in unibadchars:
        badchar_inchar += chr(badchar)

with open ("badchar.list", "wb") as file:
    file.write(badchar_inchar)


badchar_inhex = "" 
for badchars in range(1,256):
    badchar_inhex = str(sys.stdout.write("\\x"+'{:02x}'.format(badchars)))



