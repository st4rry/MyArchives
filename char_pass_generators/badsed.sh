#!/bin/bash
sed -e 's/\\x11\|\\x21\|\\x31\|\\x41\|\\x51\|\\x61\|\\x71\|\\x81\|\\x91\|\\xa1\|\\xb1\|\\xc1\|\\xd1\|\\xe1\|\\xf1\|$/\n&/g'

