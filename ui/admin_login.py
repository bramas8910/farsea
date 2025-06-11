from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFrame
from PyQt5.QtCore import Qt

class AdminLogin(QWidget):
    def __init__(self, back_callback):
        super().__init__()
        self.back_callback = back_callback
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Header
        header = QHBoxLayout()
        header_frame = QFrame()
        header_frame.setStyleSheet("background-color: #2ecc71;")
        header_frame.setFixedHeight(50)

        title = QLabel("FARSFEA")
        title.setStyleSheet("font-weight: bold; font-size: 18px; margin-left: 10px;")
        back_btn = QPushButton("BACK")
        back_btn.setStyleSheet("background-color: #e74c3c; color: white; padding: 5px 10px; margin-right: 10px;")
        back_btn.clicked.connect(self.back_callback)

        h_layout = QHBoxLayout(header_frame)
        h_layout.addWidget(title)
        h_layout.addStretch()
        h_layout.addWidget(back_btn)

        layout.addWidget(header_frame)

        # Form
        form_layout = QVBoxLayout()
        form_layout.setAlignment(Qt.AlignCenter)

        label = QLabel("Admin Login")
        label.setStyleSheet("font-size: 24px; font-weight: bold;")
        form_layout.addWidget(label)

        username = QLabel("USERNAME")
        username_input = QLineEdit()
        username_input.setPlaceholderText("Masukkan username")
        form_layout.addWidget(username)
        form_layout.addWidget(username_input)

        password = QLabel("PASSWORD")
        password_input = QLineEdit()
        password_input.setEchoMode(QLineEdit.Password)
        form_layout.addWidget(password)
        form_layout.addWidget(password_input)

        login_btn = QPushButton("LOGIN")
        login_btn.setStyleSheet("background-color: #3498db; color: white;")
        form_layout.addWidget(login_btn)

        layout.addLayout(form_layout)
        self.setLayout(layout)
