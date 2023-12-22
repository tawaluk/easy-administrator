from fabric import Connection
import socket

import pandas  # + pip install openpyxl

shops = open("list_targets.txt", "r")   # надо создать
logs = open("logs.txt", "a")  # надо создать


prohibited_commands = ("sudo su", "sudo", "su", "sudo ls",)


class TargetCash:
    """
    Класс, содержащий в себе всё необходимое для работы с кассой.

    Params:
        ip_address: str - ip4 адрес кассы без маски
        port: str - port
        user: str - user сеанса
        password: str - пароль юзера для сеанса
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
            state_old: str = None,
            state_new: str = None,
            command: str = "echo you did not pass the command to execute",

    ) -> None:
        self.ip_address = ip_address
        self.port = port
        self.user = user
        self.password = password
        self.state_old = state_old
        self.state_new = state_new
        self.command = command
        self.file = file

    def convert_txt_to_instance(self):
        """Преобразовать ip адрес в экземпляр класса."""
        return TargetCash(self.ip_address)

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

        xxxx = self.validate_command(self.command)
        print(xxxx)

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
        if self.command in prohibited_commands:
            return 'hello world!'

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
        {self.state_old} = state_old
        {self.state_new} = state_new
        {self.command} = command
        {self.file} = file"""


def main():
    number_shop = 0
    while True:
        number_shop += 1
        shop: str = shops.readline()
        shop = shop.rstrip('\n')
        if not shop:
            print('Список подошел к концу!')
            break

        try:
            one_iteration_target = TargetCash(
                ip_address=shop,
                command='ls -al'  # Сюда вместо ls указать нужную команду
            )

        except:
            logs.write('COMMAND EXECUTION ERROR - string_replacement\n')


#if __name__ == '__main__':
#    main()


def test_case():
    xxx = TargetCash(ip_address="192.168.0.6", command='sudo ls')
    print(xxx)
    xxx.execute_command()


#test_case()

test_pandas = pandas.read_excel(io='test.xlsx')
test_dist = test_pandas.to_dict()
print(test_dist)
data = pandas.DataFrame(
    test_pandas, columns=[
        'number',
        'ip_address',
        'number_teminals',
        'name_file'
    ]
)


for i in data.values:
    xxx = str(i[1])
    print(xxx)
    yyy = TargetCash(xxx)
    print(yyy)
    print(yyy.check_port())
