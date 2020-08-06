import sys
from PyQt4 import QtGui , QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from aprmd5 import md5_encode
import argparse
from urllib2 import urlopen
import os
from os import path
import sys
import random
import re
import shutil


class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(100,100,400,400)
        #self.setGeometry(50,50,500,300)
        self.setWindowTitle("Registeration")
        self.setWindowIcon(QtGui.QIcon('rs.png'))

        extractAction = QtGui.QAction ("&Exit the program", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip("Exit the program")
        extractAction.triggered.connect(self.close_application)

        runAction = QtGui.QAction ("Run the program", self)
        runAction.setShortcut("F9")
        runAction.setStatusTip("Run the program")
        runAction.triggered.connect(self.run_application)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("&File")
        fileMenu.addAction(extractAction)
        fileMenu.addAction(runAction)

        self.home()

    def home(self):

        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(0,40)

        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(10,100,250,20)
        self.btn = QtGui.QPushButton("Generate", self)
        self.btn.resize(btn.minimumSizeHint())
        self.btn.move(100,40)
        self.btn.clicked.connect(self.run_application)

        self.show()

    def close_application(self):
        choice = QtGui.QMessageBox.question(self,"Hold on!", "Do you really Want to Leave the APP?",
                                            QtGui.QMessageBox.Yes |
                                            QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            print("bye!")
            sys.exit()
        else:
            pass


    def run_application(self):
        self.setWindowTitle("Generating")
        UN = usrname, uok = QInputDialog.getText(self, 'Text Input Dialog', 'Enter your username:')
        PA = passwd, pok = QInputDialog.getText(self, 'Text Input Dialog', 'Enter your password:')
        ListInd = lind,lok = QInputDialog.getInt(self,"integer input dualog","enter a number")
        if uok and pok and lok:
            print ('username is: '+ usrname)
            print ('passwd is: '+ passwd)
            print ('list index is: '+ str(lind))

            url = "https://raw.githubusercontent.com/mhartl/bullish_case_for_bitcoin/master/bullish_case_for_bitcoin.txt"

            #print ("generating salt...\n")

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

            passwd_hash = str(passwd)
#hashing
            hashed = md5_encode(passwd_hash, salt)
            hashed_string = usrname + ':' + hashed
            print ('Your hashed string is: '+ hashed_string)
            print ('\n')
            with open('.htpasswd','w') as f:
                f.write(hashed_string)
                try:
                    check = open(".htpasswd")
                    print ('G0t Htpasswd!\n')

                except IOError:
                    print("File not accessible")
                finally:
                    check.close()

            self.clearing_track()

        else:
            print ('Please Enter username, password and list indext number to generate!...')

        self.completed = 0
        while self.completed < 100:
            self.completed += 0.01
            self.progress.setValue(self.completed)


###clearing salt####

    def clearing_track(self):
        os.remove("bosalt.txt")
        print ('Making sure if the track is clean...\n')
        try:
            check = open("bosalt.txt") #check if the file stills existing
            print ("Warning! not clean\n")
        except:
            print("well, it's clean\n")

        self.exit()

    def exit(self):
        print("Congratulations! all set. Now, copy the htaccess file into the dir you want to protect!\n")
        self.close_application()

#Main##
def main():

    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
