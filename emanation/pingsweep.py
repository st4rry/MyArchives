#!/usr/bin/python

import subprocess
import os
devnull = open(os.devnull, 'w')

for ip in range(1,255):
    nid="10.10.48.{0}".format(ip)
    run=subprocess.call(['ping', '-c', '1', '-w 1', nid],stdout=devnull)
    if run==0:
        print nid
