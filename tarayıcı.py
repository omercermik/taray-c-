import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction
from PyQt5.QtGui import QKeySequence

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        text_edit = QTextEdit(self)
        self.setCentralWidget(text_edit)
        exit_action = QAction("Exit", self)
        exit_action.setShortcut(QKeySequence.Quit)
        exit_action.triggered.connect(self.close)
        self.addAction(exit_action)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = Browser()
    browser.show()
    sys.exit(app.exec_())
