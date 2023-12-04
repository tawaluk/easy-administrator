import sys

from PyQt5 import QtWidgets
from src.gui.Windows import MainWindow, ModalWindow
from src.gui import gui_style


def main_gui():
    """Менеджер всея-GUI"""
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.setStyleSheet(gui_style.MAIN_COLOR)

    window.button(parent=window, target_event=MainWindow.open_modal_window)

    window.show()
    sys.exit(app.exec_())
