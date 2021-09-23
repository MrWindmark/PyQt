import ipaddress
import platform
import re
import subprocess
import chardet

from tabulate import tabulate


def user_menu(*args, **kwargs):
    sys_platform = platform.system()

    if sys_platform == "Windows":
        ping_com = ['-n', '4']
    else:
        ping_com = ['-c', '4']

    columns = ['command', 'description', 'command ID']
    functions = (
        ('ping', 'ping list of IP or addresses', '1'),
        ('net_ping', 'ping IP in same subnet from Start to End IP address', '2'),
        ('exit', 'close script process', '0'),
    )

    print(tabulate(functions, headers=columns))
    while True:
        user_command = input("command: ")
        if user_command == '0':
            break
        elif user_command == '1':
            print('Enter destinations with "Space" as divider')
            user_list = input("Enter addresses: ")
            url_list = user_list.split(' ')
            for elem in url_list:
                elem = elem.replace(',', '.')
                host_ping(elem, ping_com)
        elif user_command == '2':
            ip_start = dot_checker(input("Enter start of IP range: "))
            ip_end = dot_checker(input("Enter end of IP range: "))
            if ip_start != 0 and ip_end != 0:
                try:
                    host_range_ping(ip_start, ip_end, ping_com)
                except IOError:
                    print('IP value error')
        else:
            print('Error in command ID. Enter valid ID for work')


def dot_checker(data: str):
    if ',' in data:
        data.replace(',', '.')
    check = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", data)
    if check:
        return data
    else:
        return 0


def subnet_check(ip1: str, ip2: str):
    data1 = ip1.split('.')
    data2 = ip2.split('.')

    for i in range(0, 3):
        if data1[i] == data2[i]:
            pass
        else:
            return 0
    return 1


def ping_stat(address, ping_com):
    process = subprocess.Popen(['ping', str(address), *ping_com], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, error = process.communicate()
    text_encode = chardet.detect(out)
    data = out.decode(text_encode['encoding']).split('\n')
    to_drop = data.count('')
    for i in range(0, to_drop):
        data.remove('')
    if process.returncode == 1:
        return 1
    elif process.returncode == 0:
        return data


def host_ping(data: list, ping_com):
    ping_com[1] = '1'
    try:
        result = ping_stat(data, ping_com)
        if result == 1:
            print(data, 'is down!')
        else:
            print(data, 'is up!')
    except Exception as e:
        print(e)
    print('-' * 15)


def host_range_ping(ip1, ip2, ping_com):
    start = end = ipaddress.ip_address('0.0.0.0')
    table = {'Available': [], 'Unreachable': []}
    if subnet_check(ip1, ip2) == 1:
        try:
            ip1 = ipaddress.ip_address(ip1)
            ip2 = ipaddress.ip_address(ip2)
        except Exception as e:
            return 0
        if ip2 > ip1:
            start = ip1
            end = ip2
        elif ip1 > ip2:
            start = ip2
            end = ip1
        elif ip1 == ip2:
            print("Funny...")
            ping_stat(ip1, ping_com)
        print("*" * 15)
        print("Start address checking...")
        print("*" * 15)
        while end >= start:
            result = ping_stat(start, ping_com)
            if result == 0:
                print(start, 'is up!')
                table['Available'].append(str(start))
            else:
                print(start, 'is down!')
                table['Unreachable'].append(str(start))
            print('-' * 15)
            start += 1
    else:
        print("IP in different subnet or other subnet problem")

    host_range_ping_tab(table)


def host_range_ping_tab(data: dict):
    print('Total results:')
    print(tabulate(data, headers='keys', tablefmt="pipe", stralign="center"))


if __name__ == '__main__':
    print('''
    Welcome to host_ping utility v1.1
    This script can help net administrator to check current IPv4 network state.
    Created by MrWindmark
    ''')

    user_menu()
