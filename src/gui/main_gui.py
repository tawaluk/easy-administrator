import sys

from PyQt5 import QtWidgets
from src.gui.Window import MainWindow


def main_gui():
    """Менеджер всея-GUI"""
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
