from PyQt5.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
    QFrame, QSpacerItem, QSizePolicy
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

def setup_ui(window):
    main_layout = QVBoxLayout()

    # === Header ===
    header_frame = QFrame()
    header_frame.setStyleSheet("background-color: #2ecc71;")  # Green header
    header_layout = QHBoxLayout()
    header_layout.setContentsMargins(10, 5, 10, 5)

    header_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

    window.admin_button = QPushButton("ADMIN LOGIN")
    window.admin_button.setStyleSheet("""
        background-color: #3498db;
        color: white;
        padding: 6px 12px;
        font-weight: bold;
        border: none;
        border-radius: 4px;
    """)
    header_layout.addWidget(window.admin_button)

    header_frame.setLayout(header_layout)

    # === Title below header ===
    window.title_label = QLabel("Face Recognition System for Employee Attendance")
    window.title_label.setFont(QFont("Arial", 16, QFont.Bold))
    window.title_label.setAlignment(Qt.AlignCenter)

    # === Placeholder area ===
    window.placeholder = QFrame()
    window.placeholder.setFrameShape(QFrame.Box)
    window.placeholder.setStyleSheet("background-color: #f0f0f0;")
    window.placeholder.setFixedSize(640, 360)

    # === Dynamic text ===
    window.dynamic_label = QLabel("Real-time face detection (Tanggal & waktu dinamis di sini)")
    window.dynamic_label.setAlignment(Qt.AlignCenter)
    window.dynamic_label.setFont(QFont("Arial", 10))

    # === Assemble layout ===
    main_layout.addWidget(header_frame)
    main_layout.addSpacing(10)
    main_layout.addWidget(window.title_label)
    main_layout.addStretch()
    main_layout.addWidget(window.placeholder, alignment=Qt.AlignCenter)
    main_layout.addSpacing(10)
    main_layout.addWidget(window.dynamic_label)
    main_layout.addStretch()

    window.setLayout(main_layout)
