import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, 
QTextEdit, QLineEdit, QGridLayout)
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import time

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        title = QLabel('')
        author = QLabel('')
        review = QLabel('input')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid  =QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)



        self.browser = QWebEngineView()
        url = 'http://127.0.0.1:8050/'
        self.browser.load(QUrl(url))

        grid.addWidget(review, 2, 0)
        grid.addWidget(self.browser, 2,1)

        self.browser1 = QWebEngineView()
        url = 'file:///home/aurorayqz/AuroraGithub/DataAnalysisOfStarbucks/test/precipitation4_3.html'
        self.browser1.load(QUrl(url))

        grid.addWidget(author, 2, 0)
        grid.addWidget(self.browser1, 3, 1,85,2)

        self.setLayout(grid)

        self.setGeometry(1300, 1300, 1350, 1000)
        self.setWindowTitle('output')        
        self.show()



class Mythread(QThread):
    # 定义信号,定义参数为str类型
    _signal = pyqtSignal(str)

    def __init__(self):
        super(Mythread, self).__init__()

    def run(self):
        for i in range(2000000):
            # 发出信号

            self._signal.emit('当前循环值为:%s' % i)
            # 让程序休眠

            time.sleep(0.5)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()

    def chuli():
        ex.browser1 = QWebEngineView()
        url = 'file:///home/aurorayqz/AuroraGithub/DataAnalysisOfStarbucks/test/precipitation4_2.html'
        ex.browser1.load(QUrl(url))


    # 创建线程
    thread = Mythread()
    # 注册信号处理函数
    thread._signal.connect(chuli)
    # 启动线程
    #thread.start()
    sys.exit(app.exec_())