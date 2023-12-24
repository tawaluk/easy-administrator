import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton, QTableWidget, QLineEdit, QTextEdit, QWidget, QGridLayout
from src.gui.Windows import MainWindow, ModalWindow
from src.gui import gui_style

from src.actions.master_to_host_commands import Cash


def update_output_field(text, output_field):
    # Метод для обновления содержимого поля вывода текста
    output_field.append(text)

def main_gui():
    """Менеджер всея-GUI"""
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.setStyleSheet(gui_style.MAIN_COLOR)

    btn1 = QPushButton(parent=window, text="нажми на меня")
    xxx = Cash()
    yyy = xxx.check_port
    btn1.clicked.connect(yyy)

    btn2 = QPushButton(parent=window, text="нажми на меня")
    xxx = Cash()
    yyy = xxx.check_port
    btn1.clicked.connect(yyy)

    input_field = QLineEdit()
    output_window = QTextEdit('!')

    grid = QGridLayout()
    grid.addWidget(btn1, 0, 0)
    grid.addWidget(btn2, 0, 1)
    grid.addWidget(input_field, 1, 1)
    grid.addWidget(output_window, 1, 0)

    central = QWidget()
    central.setLayout(grid)
    window.setCentralWidget(central)



    window.show()

    sys.exit(app.exec_())


main_gui()