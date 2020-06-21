import socket

# Посмотрим что там за добро внутри
# for el in dir(socket):
#     print(el)

"""
family
AF_INET для сетевого протокола IPv4
AF_INET6 для IPv6
AF_UNIX для локальных сокетов (используя файл)
См. https://docs.python.org/3/library/socket.html#socket.AF_INET

type
SOCK_STREAM (надёжная потокоориентированная служба (сервис) или потоковый сокет)
SOCK_DGRAM (служба датаграмм или датаграммный сокет)
SOCK_RAW (Сырой сокет — сырой протокол поверх сетевого уровня).
См. https://docs.python.org/3/library/socket.html#socket.SOCK_STREAM

proto
Протоколы обозначаются символьными константами с префиксом IPPROTO_* (например, IPPROTO_TCP или IPPROTO_UDP). 
Если protocol=0, используется значение по умолчанию для данного вида соединений.
"""

# Сокет с явным указанием всех параметров
my_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0)

# Точно такой же сокет, но с парметрами по умолчанию
default_socket = socket.socket()

my_socket.close()
default_socket.close()
