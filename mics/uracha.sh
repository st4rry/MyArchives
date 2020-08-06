usrname="it.pgr@pyaygarden.com";
passwod="*(pgrIT@dmin)*";
curl -u $usrname:$passwod --silent "https://mail.google.com/mail/feed/atom" | egrep --color -i -o "Room Availability" > uracha.log;
if grep -Fxqi "Room Availability" uracha.log;
then
  echo "Hi, You have 'Updated Room Availablility List' Informations";
  ./tl241.sh;
else echo "Sadly, you have no Room Availability informations.";
fi
sleep 2;
