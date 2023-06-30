import pandas as pd
from sqlalchemy import create_engine


class exceltoDBtable:
    """This class is used to save excel/csv file into MySQL database.
    """

    def __init__(self,
                 filePath,
                 server="",
                 usrID="",
                 pwd="",
                 database="",
                 rename_table=""):
        """Initialize the class.

        Parameters
        ----------
        filePath : str
            The path of excel/csv file.
        server : str, optional
            The server name of MySQL database, by default ""
        usrID : str, optional
            The user ID of MySQL database, by default ""
        pwd : str, optional
            The password of MySQL database, by default ""
        database : str, optional
            The database name of MySQL database, by default ""
        rename_table : str, optional
            The table name of MySQL database. if not given, the table name will be the same as the file name, by default ""

        Raises
        ------
        an
            If the input is not correct
        Exception
            Input is not correct, please check your input...
        """

        if not any([server, database, usrID, pwd]):
            raise Exception("Input is not correct, please check your input...")

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

        Raises
        ------
        an
            If the connection is not successful, raise an exception.
        Exception
            Can not connect to MySQL, please check your input info.

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

        Raises
        ------
        an
            If the file is not excel or csv file, raise an exception.
        Exception
            Unable to load input file...

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

        Raises
        ------
        an
            If the table name is not given, raise an exception.
        Exception
            Please give the table name...
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
