import socket

from .exceltomysql import ExcelToDB

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

__all__ = ["ExcelToDB", "local_ip", "hostname"]