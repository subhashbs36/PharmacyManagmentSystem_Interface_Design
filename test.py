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

admin_dashboard,_ = loadUiType(path.join(path.dirname("__file__"), "Dashboard_admin.ui"))

#-------py fles import--------------


#----------------------------------

class Main(QMainWindow, admin_dashboard):

	#------Common Constructor for PYQT------
	def __init__(self, parent= None):
		super(Main, self).__init__(parent)
		QMainWindow.__init__(self)
		self.setupUi(self)
		self.showMaximized()
        self.Handel_Buttons()



if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())