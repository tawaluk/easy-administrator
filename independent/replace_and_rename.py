from fabric import Connection
import paramiko
import ping3
import datetime


shops = open("list_targets.txt", "r")
logs = open("logs.txt", "a")

old: str = '192.168.7.65'
new: str = '10.78.140.65'

file_location: str = '/mnt/sda1/tce/storage/crystal-cash/modules/loader/cash-system-config.xml'
file_location_2: str = '/mnt/sda1/tce/storage/crystal-cash/config/cash-config.xml'


def check(target):
    """Проверяет доступность цели"""
    response = ping3.ping(target)
    if response is not None:
        if response is not False:
            return 'yes'
        else:
            return 'incorrect address!!'
    else:
        return 'unavailable!!'


def string_replacement(target):
    with Connection(target, user='tc', connect_kwargs={'password': '324012'}) as conn:

        rename_command_1 = f'''sed -i 's/{new}/{old}/g' {file_location}'''
        rename_command_2 = f'''sed -i 's/{new}/{old}/g' {file_location_2}'''

        result = conn.run(
            f'{rename_command_1} & {rename_command_2} & cash save')

        terminal_response = (result.stdout.strip())
        logs.write(f'save check ==== {terminal_response}')


def rebot_cash(target):
    """Отдельный костыль для ребута!"""
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=target, username='tc', password='324012')
    ssh.exec_command("sudo /sbin/reboot", get_pty=True)
    ssh.close()
    logs.write(f'reboot {target}\n')


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
            logs.write('\n=========================\n')
            logs.write(f'\nShop number {number_shop}\n')
            logs.write(f'Time {datetime.datetime.now()}')
            logs.write(f'\nPing {shop} --> {check(shop)}\n')
            if check(shop) == 'yes':
                try:
                    try:
                        string_replacement(target=shop)
                        try:
                            rebot_cash(target=shop)
                            logs.write('REBOT YES\n')
                        except:
                            logs.write('REBOT NONE')
                    except:
                        logs.write('COMMAND EXECUTION ERROR - string_replacement\n')
                except:
                    logs.write('COMMAND EXECUTION ERROR\n')
            else:
                logs.write('ACCESS ERROR\n')
        except:
            print(f'{shop} -unsuccessfully')
            logs.write(f'{shop} -unsuccessfully')


if __name__ == '__main__':
    main()
