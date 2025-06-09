from PyQt5.QtWidgets import QWidget
from ui.main_window import setup_ui

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Face Recognition System for Employee Attendance")
        self.setGeometry(100, 100, 800, 600)
        setup_ui(self)
