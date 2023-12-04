import time

from src.actions import global_public_variables, basic_logic
from src.gui.main_gui import main_gui


def main():
    """Выбор режима работы с программой."""
    choice: str = input("Включить GUI? yes/no/exit\n ")
    if choice in global_public_variables.AGREE:
        main_gui()
    elif choice in global_public_variables.REFUSAL:
        print("Продолжаю работу в терминальном режиме")
        time.sleep(1)
        basic_logic.engine()

    elif choice in global_public_variables.EXIT:
        print("Выключаю программу")
        time.sleep(2)
    else:
        print('введите ответ в указанном формате..')
        main()


if __name__ == "__main__":
    main_gui()





