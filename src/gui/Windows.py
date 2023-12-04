import sys

from PyQt5.QtWidgets import QMainWindow, QDialog


class MainWindow(QMainWindow):
    """Класс-главное окно и его
    дефолтные поля и методы."""

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("easy_admin")
        self.setMinimumSize(600, 400)
        self.setStyleSheet("background-color: #85929e;")



    def open_modal_window(self):
        modal_window = ModalWindow()
        modal_window.exec_()


class ModalWindow(QDialog):
    """Класс-модальное окно и его
    дефолтные поля и методы."""

    def __init__(self):
        super(ModalWindow, self).__init__()

        self.setWindowTitle("Модальное окно")
        self.setStyleSheet("background-color: #db8971;")
        self.adjustSize()

