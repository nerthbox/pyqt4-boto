# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './mainWindow.ui'
#
# Created: Mon Apr 27 20:15:54 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class MyStream(QtCore.QObject):

    message = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(MyStream, self).__init__(parent)

    def write(self, message):
        self.message.emit(str(message))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(779, 397)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.txtAwsID = QtGui.QLineEdit(self.centralwidget)
        self.txtAwsID.setGeometry(QtCore.QRect(10, 70, 311, 33))
        self.txtAwsID.setEchoMode(QtGui.QLineEdit.Password)
        self.txtAwsID.setObjectName(_fromUtf8("txtAwsID"))
        self.btnClose = QtGui.QPushButton(self.centralwidget)
        self.btnClose.setGeometry(QtCore.QRect(210, 310, 97, 31))
        self.btnClose.setAutoDefault(False)
        self.btnClose.setDefault(True)
        self.btnClose.setObjectName(_fromUtf8("btnClose"))
        self.btnRun = QtGui.QPushButton(self.centralwidget)
        self.btnRun.setGeometry(QtCore.QRect(30, 310, 97, 31))
        self.btnRun.setObjectName(_fromUtf8("btnRun"))
        self.txtAwsSecret = QtGui.QLineEdit(self.centralwidget)
        self.txtAwsSecret.setGeometry(QtCore.QRect(10, 140, 311, 33))
        self.txtAwsSecret.setEchoMode(QtGui.QLineEdit.Password)
        self.txtAwsSecret.setObjectName(_fromUtf8("txtAwsSecret"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 40, 131, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 161, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.txtOutput = QtGui.QTextEdit(self.centralwidget)
        self.txtOutput.setGeometry(QtCore.QRect(363, 4, 411, 341))
        self.txtOutput.setObjectName(_fromUtf8("txtOutput"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 779, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menuAddCreds = QtGui.QAction(MainWindow)
        self.menuAddCreds.setObjectName(_fromUtf8("menuAddCreds"))
        self.menuRun = QtGui.QAction(MainWindow)
        self.menuRun.setObjectName(_fromUtf8("menuRun"))
        self.menuClose = QtGui.QAction(MainWindow)
        self.menuClose.setObjectName(_fromUtf8("menuClose"))
        self.menuFile.addAction(self.menuRun)
        self.menuFile.addAction(self.menuClose)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.btnClose.setText(_translate("MainWindow", "Close", None))
        self.btnRun.setText(_translate("MainWindow", "Run", None))
        self.label.setText(_translate("MainWindow", "Aws Access Key ID:", None))
        self.label_2.setText(_translate("MainWindow", "Aws Secret Access Key:", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuAddCreds.setText(_translate("MainWindow", "Add Creds", None))
        self.menuRun.setText(_translate("MainWindow", "Run", None))
        self.menuClose.setText(_translate("MainWindow", "Close", None))


