from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from PyQt5 import uic
import sys,time

from thread_deneme_python import Ui_MainWindow

class thread_deneme(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.threads={}
        self.ui.pushButton.clicked.connect(self.start_worker_1)
        self.ui.pushButton_2.clicked.connect(self.start_worker_2)
        self.ui.pushButton_3.clicked.connect(self.start_worker_3)
        self.ui.pushButton_4.clicked.connect(self.stop_worker_1)
        self.ui.pushButton_5.clicked.connect(self.stop_worker_2)
        self.ui.pushButton_6.clicked.connect(self.stop_worker_3)


    def start_worker_1(self):
        self.threads[1]=ThreadClass(parent=None,index=1)
        self.threads[1].start()
        self.threads[1].any_signal.connect(self.my_function)
        self.ui.pushButton.setEnabled(False)
    
    def start_worker_2(self):
        self.threads[2]=ThreadClass(parent=None,index=2)
        self.threads[2].start()
        self.threads[2].any_signal.connect(self.my_function)
        self.ui.pushButton_2.setEnabled(False)
    
    def start_worker_3(self):
        self.threads[3]=ThreadClass(parent=None,index=3)
        self.threads[3].start()
        self.threads[3].any_signal.connect(self.my_function)
        self.ui.pushButton_3.setEnabled(False)

    def stop_worker_1(self):
        self.threads[1].stop()
        self.ui.pushButton.setEnabled(True)
    
    def stop_worker_2(self):
        self.threads[2].stop()
        self.ui.pushButton_2.setEnabled(True)
    
    def stop_worker_3(self):
        self.threads[3].stop()
        self.ui.pushButton_3.setEnabled(True)
    
    def my_function(self,counter):
        cnt=counter
        index=self.sender().index
        if index==1:
            self.ui.progressBar.setValue(cnt)
        if index==2:
            self.ui.progressBar_2.setValue(cnt)
        if index==3:
            self.ui.progressBar_3.setValue(cnt)

class ThreadClass(QThread):
    any_signal=pyqtSignal(int)
    def __init__(self,parent=None,index=0):
        super(ThreadClass,self).__init__(parent)
        self.index=index
        self.is_running=True

    def run(self):
        cnt=0
        while True:
            cnt+=1
            if cnt==99: cnt=0
            time.sleep(0.02)
            self.any_signal.emit(cnt)

    def stop(self):
        self.is_running=False
        self.terminate()

app=QApplication(sys.argv)
mainWindow=thread_deneme()
mainWindow.show()
sys.exit(app.exec_())