from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication

import sys
from os import path
from PyQt5.uic import loadUiType
import ui_Splash as splash

import psycopg2 as psy

counter = 0



login,_ = loadUiType(path.join(path.dirname("__file__"), "login.ui"))
splash_screen,_ = loadUiType(path.join(path.dirname("__file__"), "Splash.ui"))
admin_dashboard,_ = loadUiType(path.join(path.dirname("__file__"), "Dashboard_admin.ui"))
#emplopyee_dashboard,_ = loadUiType(path.join(path.dirname("__file__"), "User_admin.ui"))






        
#----------Admin page------------------
class Login(QDialog, login):

    def __init__(self):
        super(Login, self).__init__()      
        self.setupUi(self)
        self.Handel_Buttons()
        

    def Handel_Buttons(self):
        self.clear.clicked.connect(self.Reset)
        self.login.clicked.connect(self.Login)
        self.quit.clicked.connect(self.Quit)
    def Login(self):
        username = self.admin_username.text()
        password = self.admin_password.text()
        if ((username == "hello") & (password == "123")):
            print("Access Granted")
            self.runIt()
        else:
            QMessageBox.warning(self, "Invalid", "Invalid Username or Password")
           

    def Reset(self):
        self.admin_username.setText("")
        self.admin_password.setText("")       

    def Quit(self):
        self.close()

    def runIt(self):
        self.accept()


#------------------------------------------------------

#--------------------------------------------------

class Main(QMainWindow, admin_dashboard):

	#------Common Constructor for PYQT------
	def __init__(self, parent= None):
		super(Main, self).__init__(parent)
		QMainWindow.__init__(self)
		self.setupUi(self)
		self.showMaximized()


        





#----------main-------------
def main():
    app = QApplication(sys.argv)
    login = Login()
    if login.exec_() == QDialog.Accepted:
        window = splash.SplashScreen()
        window.show()
        sys.exit(app.exec_())    


if __name__ == "__main__":
    main()



    
