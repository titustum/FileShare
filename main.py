import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Swara")
        self.setGeometry(100, 100, 400, 600)
        
        self.label = QLabel("Welcome to Swara", self)
        self.label.setGeometry(100, 50, 200, 50)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
