import subprocess

process = {"clients": [], "servers": []}


def proc_killer(name: str):
    """
    This function take a key for work with process dictionary and kill all process with that keyword
    :param name: name which used as description of process type in process dictionary
    :return: this function have no returned data
    """
    while process[name]:
        victim = process.pop()
        victim.kill()


if __name__ == "__main__":
    while True:
        action = input('Выберите действие: q - выход,'
                       's - запустить сервер и клиенты,'
                       'x - закрыть все окна,'
                       'xs - закрыть все серверы,'
                       'xc - закрыть все клиенты')

        if action == 'q':
            break
        elif action == 's':
            process["servers"].append(subprocess.Popen('python server.py', creationflags=subprocess.CREATE_NEW_CONSOLE))
            process["clients"].append(
                subprocess.Popen('python client.py -n test1', creationflags=subprocess.CREATE_NEW_CONSOLE))
            process["clients"].append(
                subprocess.Popen('python client.py -n test2', creationflags=subprocess.CREATE_NEW_CONSOLE))
            process["clients"].append(
                subprocess.Popen('python client.py -n test3', creationflags=subprocess.CREATE_NEW_CONSOLE))
        elif action == 'x':
            proc_killer("clients")
            proc_killer("servers")
        elif action == 'xs':
            proc_killer("servers")
        elif action == 'xc':
            proc_killer("clients")
