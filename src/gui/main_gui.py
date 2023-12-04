import sys

from PyQt5 import QtWidgets
from src.gui.Windows import MainWindow, ModalWindow
from src.gui import gui_style


def main_gui():
    """Менеджер всея-GUI"""
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.setStyleSheet(gui_style.MAIN_COLOR)

    btn = QtWidgets.QPushButton(window)
    btn.setText("Нажми на меня!")
    btn.setStyleSheet(gui_style.BATTON_COLOR)
    btn.clicked.connect(MainWindow.open_modal_window)
    btn.show()

    window.show()
    sys.exit(app.exec_())
