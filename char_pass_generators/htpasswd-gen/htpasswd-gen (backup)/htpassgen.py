#!/usr/bin/env python3
from aprmd5 import md5_encode
import argparse
from urllib2 import urlopen
import os
import sys
import random
import re

print ("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print ("@@         htpasswd Generator          @@")
print ("@@-----------Author: starry------------@@")
print ("@@-----------Name: htpassgen-----------@@")
print ("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print ("\n")


if len(sys.argv) < 4:
  print ("Usage               : python htpassgen.py <username> <passwd> <list indicator number>")
  print ("Example             : python htpassgen.py starry starry57422Y 12")

  sys.exit(0)

username = sys.argv[1]
passwd   = sys.argv[2]
lind = sys.argv[3]

url = "https://raw.githubusercontent.com/mhartl/bullish_case_for_bitcoin/master/bullish_case_for_bitcoin.txt"

print ("generating salt...\n")

with open('bosalt.txt','w') as f:
    f.write(urlopen(url).read())
try:
    check = open("bosalt.txt")
    print ('G0t$a1t!\n')
    salt = ""
    salt += open('bosalt.txt','r').read().split(",")[int(lind)]
    salt += random.choice(salt) 
    print ("your random salt is: ", salt)
except IOError:
    print("File not accessible")
finally:
    check.close()

def hashing_method(passwd_hash, salt):
    hashed = md5_encode(passwd_hash, salt)

    print ('Your hash for htpasswd is =>', username+':'+hashed)
    print ('\n')
    clearing_track()

def clearing_track():
    os.remove("bosalt.txt")
    print ('Making sure if the track is clean...\n')
    try:
        check = open("bosalt.txt") #check if the file stills existing
        print ("not clean")
    except:
        print("well, it's clean")

def main():
    print ('Hashing Done!\n...')
    passwd_hash = passwd
    hashing_method(passwd_hash, salt)

if __name__ == '__main__':
    main()
