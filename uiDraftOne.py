__author__ = 'nerth'
import sys
import boto.ec2
from PyQt4 import QtGui, QtCore
from mainWindow import Ui_MainWindow
####
from pprint import pprint
from mainWindow import MyStream


class Main(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #### Set Up Signals and other Actions of UI objects
        self.setupSignals()

        #### Global AWS_CREDS
        self.AWS_CREDS = ['', '']

        #### Global boto Connection
        self.conn = None


        ####
        ## for prnting to txtOutput Debug
        ####


    @QtCore.pyqtSlot()
    def on_btnRun(self):

        #### Get Creds return AWS_CREDS Tuple
        if not self.getCreds():
            self.on_myStream_message('Debug: Error With AWS_CREDS check')



        #### Creat a conn and will return a Conn type
        if not self.creatConn():
            self.on_myStream_message('Debug: Conn Failed')
    @QtCore.pyqtSlot(str)
    def on_myStream_message(self, message):
        self.ui.txtOutput.moveCursor(QtGui.QTextCursor.End)
        self.ui.txtOutput.insertPlainText(message)



    def getCreds(self):
        #### Take txtAws input and pass to AWS_CREDS Tuple
        self.AWS_CREDS = [unicode(self.ui.txtAwsID.text().toUtf8(), encoding="UTF-8"),
                          unicode(self.ui.txtAwsSecret.text().toUtf8(), encoding="UTF-8")]

        ####
        ## TODO: Need to double check logic!!!
        ####

        if boto.ec2.regions(aws_access_key_id=self.AWS_CREDS[0],
        #                   aws_secret_access_key=self.AWS_CREDS[1]):


        ## Debug ##

        self.on_myStream_message(self.AWS_CREDS[0] + '\n')
        self.on_myStream_message(self.AWS_CREDS[1] + '\n')
        return self.AWS_CREDS

    def creatConn(self):
        #### create a new Connection and return it

        #### HARD CODE Region, this si where the menu will pass its va
        self.conn = boto.ec2.connect_to_region('us-east-1', aws_access_key_id=(self.AWS_CREDS[0]),
                                               aws_secret_access_key=self.AWS_CREDS[1])

        if not self.conn:
            self.on_myStream_message('Error: Invalid Region, or Creds')
            return 0
        else:
            self.on_myStream_message('Debug: Connection Made')
            return self.conn

        #####################
        ####--Test Bed--####
        ##################

    def setupSignals(self):
        #### Sets Close button to shut kill instance
        self.ui.btnClose.clicked.connect(QtCore.QCoreApplication.instance().quit)

        #### Runs the btnRun_Click Function when Clicked
        self.ui.btnRun.clicked.connect(self.on_btnRun)





    def btnRun_Click(self):

        #### Get Creds return AWS_CREDS Tuple
        if not self.getCreds():
            print 'Debug: Error With AWS_CREDS check'



        #### Creat a conn and will return a Conn type
        if not self.creatConn():
            print 'Debug: Conn Failed'







if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    window = Main()
    window.show()

    stream = MyStream()
    stream.message.connect(window.on_myStream_message)
    sys.stdout = MyStream
    sys.exit(app.exec_())



