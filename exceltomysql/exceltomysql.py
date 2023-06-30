import pandas as pd
from sqlalchemy import create_engine


class exceltoDBtable(object):
    """This class is used to save excel/csv file into MySQL database.

    Args:
        filePath (str): The path of excel/csv file.
        server (str): The server name of MySQL database.
        usrID (str): The user ID of MySQL database.
        pwd (str): The password of MySQL database.
        database (str): The database name of MySQL database.
        rename_table (str): The table name of MySQL database. if not given, the table name will be the same as the file name.

    Returns:
        None: save local excel/csv file into MySQL database.

    """

    def __init__(self,
                 filePath,
                 server="",
                 usrID="",
                 pwd="",
                 database="",
                 rename_table=""):
        """_summary_

        Args:
            filePath (str): The path of excel/csv file.
            server (str): The server name of MySQL database.
            usrID (str): The user ID of MySQL database.
            pwd (str): The password of MySQL database.
            database (str): The database name of MySQL database.
            rename_table (str): The table name of MySQL database. if not given, the table name will be the same as the file name.

        Raises:
            Exception: If the input is not correct, raise an exception.
        """

        if not any([server, database, usrID, pwd]):
            raise Exception("Partially inputs, please check your inputs...")

        self.filePath = filePath
        self.server = server
        self.database = database
        self.usrID = usrID
        self.pwd = pwd
        self.rename_table = rename_table
        self.readData()
        self.connect2DB()
        self.save2database()

    def connect2DB(self):
        """Connect to MySQL database.

        Raises:
            Exception: If the connection is not successful, raise an exception.
        """

        try:
            # self.conn = pymysql.connect(host=self.server,user=self.usrID,password=self.pwd,db=self.database,charset="utf8",cursorclass=pymysql.cursors.DictCursor)
            self.engine = create_engine('mysql+pymysql://%s:%s@%s:3306/%s' % (self.usrID, self.pwd, self.server, self.database))
            print("Successfully connected to MySQL...")
        except Exception as e:
            raise Exception(
                "Can not connect to MySQL, please check your input info."
            ) from e

    def readData(self):
        """Read excel/csv file.

        Raises:
            Exception: If the file is not excel/csv file, raise an exception.
        """

        if self.filePath.split(".")[-1] in ["xlsx", "xls"]:
            self.file_data = pd.read_excel(self.filePath)
            print("Successfully load excel data...")
        elif self.filePath.split(".")[-1] in ["csv"]:
            self.file_data = pd.read_csv(self.filePath)
            print("Successfully load csv data...")
        else:
            raise Exception("Unable to load input file...")

    def save2database(self):
        """Save excel/csv file into MySQL database.

        Raises:
            Exception: If the saving process is not successful, raise an exception.
        """

        if self.rename_table:
            tableName = self.rename_table
        elif "/" in self.filePath:
            tableName = self.filePath.split("/")[-1].split(".")[0]
        else:
            tableName = self.filePath.split(".")[0]

        try:
            self.file_data.to_sql(tableName, con=self.engine)
            print("Successfully save %s into database..." % tableName)
        except Exception as e:
            raise Exception(e) from e
