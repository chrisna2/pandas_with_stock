import sys
from PyQt5.QtWidgets import *

'''
간단한 회면 처리
'''
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("Review")
        btn1 = QPushButton("click me", self)
        btn1.move(20, 20)
        btn1.clicked.connect(self.btn1_clicked)


    def btn1_clicked(self):
        QMessageBox.about(self, "message", "Clicked")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()