"""
Main GUI window module for the Android servicing tool.
"""

from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):
    """Basic main window placeholder."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Android Servicing Tool")
        self.resize(1000, 700)

        central = QWidget()
        layout = QVBoxLayout(central)
        header = QLabel("Android Servicing Tool")
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header.setFont(QFont("Arial", 18))
        layout.addWidget(header)
        self.setCentralWidget(central)
