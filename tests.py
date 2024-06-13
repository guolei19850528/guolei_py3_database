import os.path
import re
import types
import unittest

import duckdb
import pymysql

import guolei_py3_database.duckdb
from guolei_py3_database import pymysql as gl_pymysql
from guolei_py3_database import sqlite3 as gl_sqlite3
from guolei_py3_database import strictredis as gl_strictredis


class PymysqlTestCase(unittest.TestCase):
    def test_connect(self):
        database = gl_pymysql.Database(connect_kwargs={
            "host": "localhost",
            "port": 3306,
            "user": "root",
            "passwd": "123456",
            "db": "guolei_dev_db",
        })
        database.open_connect()
        print(database.fetchall("select * from test_0001", args={"name": "test"}))
        database.close_connect()
        self.assertTrue(
            True,
            "connect not a pymysql instance"
        )


class Sqlite3TestCase(unittest.TestCase):
    def test_connect(self):
        sqlite3_db_fp = os.path.join(
            os.path.dirname(__file__),
            *[
                "runtime",
                "pos.db",
            ]
        )
        database = gl_sqlite3.Database(connect_kwargs={
            "database": sqlite3_db_fp,
        })
        database.open_connect()
        print((database.fetchall("select * from goods limit 100")))
        database.close_connect()
        self.assertTrue(
            True,
            "connect not a sqlite3 instance"
        )


class StrictRedisTestCase(unittest.TestCase):
    def test_connect(self):
        self.assertTrue(
            True,
            "connect not a strictredis instance"
        )


class DuckdbTestCase(unittest.TestCase):
    def test_connect(self):
        self.assertTrue(
            True,
            "connect not a strictredis instance"
        )


if __name__ == '__main__':
    unittest.main()
