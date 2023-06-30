import socket

from .exceltomysql import exceltoDBtable

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

