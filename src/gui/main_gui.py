import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton
from src.gui.Windows import MainWindow, ModalWindow
from src.gui import gui_style

from src.actions.master_to_host_commands import Cash
from src.actions import global_public_variables


def add_label():
    xxx = Cash()
    xxx.check_port()


def main_gui():
    """Менеджер всея-GUI"""
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.setStyleSheet(gui_style.MAIN_COLOR)

    pole = QtWidgets.QLineEdit("z", parent=window)

    xx = QPushButton(parent=window, text="нажми на меня")
    xx.geometry()
    xx.clicked.connect(add_label)


    #  window.button(parent=window, target_event=Cash.check_port)

    window.show()
    pole.show()
    sys.exit(app.exec_())


main_gui()