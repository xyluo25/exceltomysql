# -*- coding:utf-8 -*-
##############################################################
# Created Date: Monday, December 28th 2020
# Contact Info: luoxiangyong01@gmail.com
# Author/Copyright: Mr. Xiangyong Luo
##############################################################


import pandas as pd
import pymysql
import pyodbc
from sqlalchemy import create_engine

import socket

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)


# Pandas to sql need to use sqlalcemy to create engine


class exceltoDBtable:
    #  Available for sql server and mysql now
    def __init__(self,filePath,server=False,usrID =False,pwd=False,database=False,save2tableName=False):
        if not any([server, database, usrID, pwd]):
            raise Exception("Partially inputs, please check your inputs...")
        self.filePath = filePath
        self.server = server
        self.database=database
        self.usrID = usrID
        self.pwd = pwd
        self.save2tableName = save2tableName
        self.dbType = ["mysql","sqlserver"]
        self.readData()
        self.connect2DB()
        self.save2database()

    def connect2DB(self) -> "Connect to Database Server":

        try:
            # self.conn = pymysql.connect(host=self.server,user=self.usrID,password=self.pwd,db=self.database,charset="utf8",cursorclass=pymysql.cursors.DictCursor)

            self.engine = create_engine(
                f'mysql+pymysql://{self.usrID}:{self.pwd}@{self.server}:3306/{self.database}'
            )

            print("Successfully connected to MySQL...")
        except:
            raise Exception(
                f"Can not connect to {self.dbType}, please check your input info."
            )

    def readData(self) -> "DataFrame":
        if self.filePath.split(".")[-1] in ["xlsx","xls"]:
            self.file_data = pd.read_excel(self.filePath)
            print("Successfully load excel data...")
        elif self.filePath.split(".")[-1] in ["csv"]:
            self.file_data = pd.read_csv(self.filePath)
            print("Successfully load csv data...")
        else:
            raise Exception("Unable to load input file...")

    def save2database(self) -> "DataFrame to database":
        if self.save2tableName:
            tableName = self.save2tableName
        elif "/" in self.filePath:
            tableName = self.filePath.split("/")[-1].split(".")[0]
        else:
            tableName = self.filePath.split(".")[0]
        try:
            self.file_data.to_sql(tableName,con=self.engine)
            print(f"Successfully save {tableName} into database...")
        except Exception as e:
            raise Exception(e)


    
