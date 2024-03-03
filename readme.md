# Introduction

This package help to convert your excel files (xlsx,xls,csv) to MySQL Server database.

# Installation

exceltomysql can be installed as:

Windows:

```python
pip install exceltomysql
```

# Dependency

👍   [pandas](https://pandas.pydata.org/)

👍   [pymysql](http://www.pymssql.org/)

👍   [sqlalchemy](https://www.sqlalchemy.org/)

# QuickStart

```python
from exceltomysql import ExcelToDB

# Step 1, prepare your input pareameters

yourFile  = "test01.xls"  # available for xlsx, xls,csv
yourUsrID = ""
yourPWD   = ""
yourDBname= ""
rename_table = ""  # Use your filename as tablename to MySQL Server or user define their prefered table name. e.g. : "test"

# get your local host name
# this will return your local computer name for your MySQL server database
host_name = em.hostname

# get your local ip address
# this will return your local ip address (if your sql server can be accessed by DNS)
IP = em.local_ip
yourHostOrIP  = "localhost"   # you need to change your host if needed, dns: local ip address

# Step 2, save your data onto MySQL
ex = ExcelToDB(yourFile, yourHoseOrIP, yourUsrID, yourPWD, yourDBname, rename_table)
ex.save2db()

```


```python
output:
Successfully load excel data...
Secessfully connected to MySQL Server...
Secessfully saved 'yourtable' to MySQL Server...
```

# API Reference

exceltomysql.ExcelToDB(`filePath, host_ip ="", usrID = "", pwd = "", db_name = "", rename_table = ""`)

filePath: str

hostORip: str  default :""

usrID: str  default: ""

pwd: str   default: ""

db_name: str  default: ""

rename_table: str   default: "",  will auto save your filename as tablename to MySQL Database. If assignmed value, will change tablename from your filename to the assigned value.
