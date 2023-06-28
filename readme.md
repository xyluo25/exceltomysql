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
import exceltomysql as em
# generate the class instance

# STEP One, prepare your input pareameters

yourFile  = "test01.xls"  # available for xlsx, xls,csv
yourUsrID = ""
yourPWD   = ""
yourDBname= ""
save2tableName = ""  # Use your filename as tablename to MySQL Server or user define their prefered table name. e.g. : "test"

# get your local host name
# this will return your local computer name for your MySQL server database
host_name = em.hostname

# get your local ip address
# this will return your local ip address (if your sql server can be accessed by DNS)
ip = em.local_ip

yourHostORip  = "localhost"   # you need to change your host if needed, dns: local ip address


# STEP Two  convert your data to MySQL
em.exceltoDBtable(yourFile, yourHoseORip, yourUsrID, yourPWD, yourDBname, rename_table)


```

```python
output:
Successfully load excel data...
Secessfully connected to MySQL Server...
Secessfully saved 'yourtable' to MySQL Server...
```

# API Reference

exceltosqlserver.exceltoDBtable(`filePath, hostORip ="", usrID = "", pwd = "", database = "", rename_table = ""`)

filePath: str

hostORip: str  default :""

usrID: str  default: ""

pwd: str   default: ""

database: str  default: ""

rename_table: str   default: "",  will auto save your filename as tablename to MySQL Database. If assignmed value, will change tablename from your filename to the assigned value.
