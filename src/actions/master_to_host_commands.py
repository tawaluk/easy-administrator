import socket

from fabric import Connection

from descriptors import Name, Body, Target, If_root
from global_public_variables import PROHIBITED_COMMANDS


class Cash:
    """
    Класс, содержащий в себе всё необходимое для работы с кассой.

    Params:
        ip_address: str - ip4 адрес кассы без маски
        port: str - port
        user: str - user сеанса
        password: str - пароль юзера для сеанса
        sudo: bool - уровень доступа. Только для активных действий.
        state_old: str - старое/искомое состояние обьекта/строки
        state_new: str - новое/желаемое состояние обьекта/строки
        command: str - команда выполняемая за 1 сеанс.
    По умолчанию:port='22', user='tc', password='324012', sudo=False.
    """

    def __init__(
            self,
            ip_address: str = "8.8.8.8",
            file: str = None,
            port: str = "22",
            user: str = "tc",
            password: str = "324012",
            sudo: bool = False,
            state_old: str = None,
            state_new: str = None,
            command: str = "echo you did not pass the command to execute",

    ) -> None:
        self.ip_address = ip_address
        self.port = port
        self.user = user
        self.password = password
        self.sudo = sudo
        self.state_old = state_old
        self.state_new = state_new
        self.command = command
        self.file = file

    def convert_txt_to_instance(self):
        """Преобразовать ip адрес в экземпляр класса."""
        return Cash(self.ip_address)

    def check_port(self) -> str:
        """Проверить доступность нужного порта у цели."""

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((self.ip_address, int(self.port)))
        if result == 0:
            responce = "Сокет открыт"
        else:
            responce = f"{self.ip_address}:{self.port} - Сокет закрыт или недоступен"
        return responce

    def execute_command(self) -> str:
        """Выполнить команду."""

        test = self.check_port()
        self.validate_command(self.command)

        if test == "Сокет открыт":
            with Connection(
                    host=self.ip_address,
                    user=self.user,
                    connect_kwargs={
                        'password': self.password
                    }
            ) as connection_session:
                result = connection_session.run(
                    self.command
                )
                terminal_responce = (result.stdout.strip())
                return terminal_responce
        else:
            return test

    def validate_command(self, command):
        self.command = command
        if self.command in PROHIBITED_COMMANDS:
            return 'invalid command!'

    def replace_string(self) -> None:
        """Заменить строку."""

        self.command = f"""
            sed -i 's/{self.state_old}/{self.state_new}/g' {self.file}"""
        self.execute_command()

    def reboot_cash(self) -> None:
        """Перезапустить кассу.
         УКАЗАТЬ ТОЛЬКО ХОСТ И ВСЁ!"""

        self.command = "sudo '/sbin/reboot'"
        self.execute_command()

    def __str__(self):
        """Вернуть экземпляр класса в читаемом значении."""
        return f"""{self.ip_address} = ip_address
        {self.port} = port
        {self.user} = user
        {self.password} = password
        {self.sudo} = sudo
        {self.state_old} = state_old
        {self.state_new} = state_new
        {self.command} = command
        {self.file} = file"""
