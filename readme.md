# Introduction

This package help to convert your excel files (xlsx,xls,csv) to Mysql database.

# Installation

exceltomysql can be installed as:

Windows:

```python
pip install esceltomysql
```

# Dependency

👍   [pandas](https://pandas.pydata.org/)

👍   [pymysql](https://github.com/PyMySQL/PyMySQL/)

👍   [sqlalchemy](https://www.sqlalchemy.org/)

# Reslase History

`0.1`

# QuickStart

```python
import exceltomysql

# generate the class instance

yourFile  = "test01.xls"  # available for xlsx, xls,csv
yourHost  = "localhost"   # you need to change your host if needed
yourUsrID = ""
yourPWD   = ""
yourDBname= ""

exceltomysql(yourFile,yourHose,yourUsrID,yourPWD,yourDBname)


```

```python
output:
Successfully load excel data...
Secessfully connected to mysql...
Successfully save data into database
```



# API Reference

exceltomysql(`filePath,server=False,usrID =False,pwd=False,database=False,save2tableName`)


filePath:

strserver: str  default :False

usrID: str  default: False

pwd: str   default: False

database: str  default:False

save2tableName: str   default:False, will auto save your file name as table name  into mysql database. If assignmed value, will change table name from your file name to the assigned value.
