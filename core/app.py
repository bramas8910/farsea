from PyQt5.QtWidgets import QWidget, QStackedLayout
from ui.main_window import MainWindow
from ui.admin_login import AdminLogin

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FARSFEA App")
        self.setGeometry(100, 100, 800, 600)

        self.layout = QStackedLayout()
        self.setLayout(self.layout)

        self.main_window = MainWindow(self.show_admin_login)
        self.admin_login = AdminLogin(self.show_main_window)

        self.layout.addWidget(self.main_window)
        self.layout.addWidget(self.admin_login)

        self.layout.setCurrentWidget(self.main_window)

    def show_admin_login(self):
        self.layout.setCurrentWidget(self.admin_login)

    def show_main_window(self):
        self.layout.setCurrentWidget(self.main_window)
