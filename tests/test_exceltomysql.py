# -*- coding:utf-8 -*-
##############################################################
# Created Date: Sunday, March 3rd 2024
# Contact Info: luoxiangyong01@gmail.com
# Author/Copyright: Mr. Xiangyong Luo
##############################################################


import pytest
from exceltomysql import ExcelToDB

import sqlalchemy
import pymysql
import sys
import pandas as pd
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.absolute()))


def test_excel_to_db_connect2db():
    excel = ExcelToDB("test_data/test01.xls", "localhost", "root", "123456", " test_db", "test_table")
    excel._connect2DB()
    assert excel.engine is not None
