from PyQt5.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFrame,
    QSpacerItem, QSizePolicy
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

def setup_ui(window):
    main_layout = QVBoxLayout()

    # === Header ===
    header = QFrame()
    header.setStyleSheet("background-color: #2ecc71;")
    header_layout = QHBoxLayout()
    header_layout.setContentsMargins(10, 5, 10, 5)

    header_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

    login_btn = QPushButton("ADMIN LOGIN")
    login_btn.setStyleSheet("background-color: #3498db; color: white; padding: 6px 12px;")
    login_btn.clicked.connect(window.show_admin_login)
    header_layout.addWidget(login_btn)

    header.setLayout(header_layout)

    # === Judul utama ===
    title = QLabel("Face Recognition System for Employee Attendance")
    title.setFont(QFont("Arial", 16, QFont.Bold))
    title.setAlignment(Qt.AlignCenter)

    # === Placeholder dan label dinamis ===
    placeholder = QFrame()
    placeholder.setFrameShape(QFrame.Box)
    placeholder.setStyleSheet("background-color: #f0f0f0;")
    placeholder.setFixedSize(640, 360)

    dynamic_label = QLabel("Real-time face detection (Tanggal & waktu dinamis di sini)")
    dynamic_label.setAlignment(Qt.AlignCenter)
    dynamic_label.setFont(QFont("Arial", 10))

    # === Layout akhir ===
    main_layout.addWidget(header)
    main_layout.addSpacing(10)
    main_layout.addWidget(title)
    main_layout.addStretch()
    main_layout.addWidget(placeholder, alignment=Qt.AlignCenter)
    main_layout.addSpacing(10)
    main_layout.addWidget(dynamic_label)
    main_layout.addStretch()

    window.setLayout(main_layout)
