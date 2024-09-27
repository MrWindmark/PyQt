import subprocess

process = {"clients": [], "servers": []}

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
        while process["clients"]:
            victim = process.pop()
            victim.kill()
        while process["servers"]:
            victim = process.pop()
            victim.kill()
    elif action == 'xs':
        while process["servers"]:
            victim = process.pop()
            victim.kill()
    elif action == 'xc':
        while process["clients"]:
            victim = process.pop()
            victim.kill()
