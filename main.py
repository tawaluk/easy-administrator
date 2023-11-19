import os
import time

from resources import global_public_variables
from core import basic_logic


def main():
    """Выбор режима работы с программой."""
    choice: str = input("Включить GUI? yes/no/exit\n ")
    if choice in global_public_variables.AGREE:
        print("Запускаю GUI...\n3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)

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
    main()





