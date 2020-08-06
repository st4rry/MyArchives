#! /bin/bash
set -euo pipefail

cat << "EOF"

< starry >
 --------
   \         ,        ,
    \       /(        )`
     \      \ \___   / |
            /- _  `-/  '
           (/\/ \ \   /\
           / /   | `    \
           O O   ) /    |
           `-^--'`<     '
          (_.)  _  )   /
           `.___/`    /
             `-----' /
<----.     __ / __   \
<----|====O)))==) \) /====
<----'    `--' `.__,' \
             |        |
              \       /
        ______( (_  / \______
      ,'  ,-----'   |        \
      `--{__________)        \/

EOF

#Generate Random Characters"
echo -e "Generating random characters... \n"

#You can modify the link to generate random characters
curl -s https://www.starwars.com/news/new-star-wars-the-rise-of-skywalker-updates-coming-to-mobile-games | grep "Star Wars" | cut -d ":" -f 4 | cut -d "<" -f 1 | sed -e '/^\/\//d' | sed -e '/^$/d'  > .randstr.txt

#Mixing ASCII
echo -e "Mixing random characters... \n"
man ascii | grep 0 | cut -d " " -f 19 | sed -e '/^$/d' >> .randstr.txt

#Define characters length
echo -e "makepass will make 8 chars password in default.\nYou can specify the password chars length\n\r"
echo -e "[!] Usage: makepass 5,8,16,20 or 40 (240 bit) \n\r"
echo -e "[@} Your 10 different secure passwords are -----\n\r"

#Generate password

cat /dev/urandom .randstr.txt | tr -dc 'A-Za-z0-9!#$%&\()*+-<=>?@[]^_{}~' | base64 --wrap ${1:-"8"} | head -n 10

#Clear Footprints
echo "___________________________"
echo -e "Clearing footprints..\n"
rm .randstr.txt 2>/dev/null
sleep 1
echo -e "Done!\n"
