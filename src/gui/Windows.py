import sys

from PyQt5.QtWidgets import QMainWindow, QDialog, QWidget, QGridLayout, QLineEdit
from src.gui import gui_style
from src.actions.master_to_host_commands import Cash


class MainWindow(QMainWindow, QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("easy_admin")
        self.setMinimumSize(600, 400)
        self.setStyleSheet("background-color: #85929e;")

        self.initUI()

    def init_ui(self):

        grid = QGridLayout()
        self.setLayout(grid)

        line_edit_1 = QLineEdit()
        grid.addWidget(line_edit_1, )


class ModalWindow(QDialog):
    """Класс-модальное окно и его
    дефолтные поля и методы."""

    def __init__(self):
        super(ModalWindow, self).__init__()

        self.setWindowTitle("Модальное окно")
        self.setStyleSheet("background-color: #db8971;")
        self.adjustSize()
