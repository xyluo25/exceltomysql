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
import exceltomysq as em
# generate the class instance

# STEP One, prepare your input pareameters

yourFile  = "test01.xls"  # available for xlsx, xls,csv
yourUsrID = ""
yourPWD   = ""
yourDBname= ""
save2tableName = False  # save your file name table name onto MySQL Server or A string like: "test"

# get your local host name
# this will return your local computer name for your MySQL server database
host_name = em.hostname   

# get your local ip address 
# this will return your local ip address (if your sql server can be accessed by DNS)
ip = em.local_ip  

yourHostORip  = "localhost"   # you need to change your host if needed, dns: local ip address


# STEP Two  convert your data to sql server
em.exceltoDBtable(yourFile,yourHoseORip,yourUsrID,yourPWD,yourDBname,save2tableName)


```

```python
output:
Successfully load excel data...
Secessfully connected to MySQL Server...
Secessfully saved 'yourtable' into SQL Server...
```

# API Reference

exceltosqlserver.exceltoDBtable(`filePath,hostORip=False,usrID =False,pwd=False,database=False,save2tableName`)

filePath: str

hostORip: str  default :False

usrID: str  default: False

pwd: str   default: False

database: str  default:False

save2tableName: str   default:False, will auto save your file name as table name  into mysql database. If assignmed value, will change table name from your file name to the assigned value.
