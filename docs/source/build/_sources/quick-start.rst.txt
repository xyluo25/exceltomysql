===========
Quick Start
===========

In this section, some examples are provided to quickly show how to use utdf2gmns to match movements with synchro signal data.


Simple Example
==============

.. code-block:: python

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


    # output:
    # Successfully load excel data...
    # Secessfully connected to MySQL Server...
    # Secessfully saved 'yourtable' to MySQL Server...


