import paramiko


ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname="193.233.75.75", username="root", password="fo5GhARNXNg7")

# Выполнение команды
channel = ssh.invoke_shell()

# Отправка команды
channel.send("cd noda/\n")
channel.send("python3 bot.py &\n")

# Прочтение вывода (если требуется)
output = channel.recv(4096)

# Вывод результата
print(output.decode())

# Закрытие канала
channel.close()

# Закрытие соединения
ssh.close()