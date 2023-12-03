from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    """Класс-главное окно и его
    дефолтные поля и методы."""

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("easy_admin")
        self.setGeometry(100, 100, 800, 700)

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("дефолтный текст")
        self.main_text.move(100, 100)
        self.main_text.adjustSize()
