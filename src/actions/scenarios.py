import datetime

from typing import Dict

from src.actions.master_to_host_commands import Cash


class ScenarioCash:
    """Класс сценариев работы с кассой.
    В разработке!!!!!!!!!!!!!!!!!!!!!
    В релиз выйдет с докой и примерами, для самых маленьких."""

    def __init__(
            self,
            name: str,
            description: str,
            dict_actions: Dict[str, Cash]
    ):

        self.name = name
        self.description = description
        self.dict_actions = dict_actions

    @staticmethod
    def time_logger() -> str:
        x = datetime.datetime.now()
        x_str = x.strftime("%Y-%m-%d %H:%M:%S")
        return x_str

    def run_scenario(self) -> dict:
        text_log = {"Время начала сценария": self.time_logger()}
        for name_command, command in self.dict_actions.items():
            text_log[name_command] = f"{command()} {self.time_logger()}"
        text_log["Время завершения сценария"] = self.time_logger()
        return text_log


def test_case():
    """Тестовый кейс. Проверяет и отвечает только за свой класс!
    Создаются корректные экземпляры класса Cash.
    Выполняется создание экземпляра(ов) класса ScenarioCash.
    Выполняется метод run_scenario ( + вызывается time_logger ).
    Возвращается словарь и приводится к читаемому виду
    ориентированно на терминал, силами test_case()."""

    test_dict_1 = {
        "test_command_1": Cash(ip_address='192.168.150.208').check_port,
        "test_command_2": Cash(ip_address='192.168.151.208').check_port,
        "test_command_3": Cash(ip_address='192.168.150.208').check_port,
    }

    script = ScenarioCash(
        name="Тестовый сценарий",
        description="Проверяет 22 порты в 3 кассах.",
        dict_actions=test_dict_1
    )

    result_list = script.run_scenario()

    for name, name_command in result_list.items():
        print(name, name_command)


test_case()
