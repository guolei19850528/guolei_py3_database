import types
import unittest

import pymysql

from guolei_py3_database import pymysql as gl_pymysql
from guolei_py3_database import sqlite3 as gl_sqlite3
from guolei_py3_database import strictredis as gl_strictredis


class PymysqlCase(unittest.TestCase):
    def test_connect(self):
        self.assertTrue(
            True,
            "connect not a pymysql instance"
        )


class Sqlite3Case(unittest.TestCase):
    def test_connect(self):
        self.assertTrue(
            True,
            "connect not a sqlite3 instance"
        )


class StrictredisCase(unittest.TestCase):
    def test_connect(self):
        self.assertTrue(
            True,
            "connect not a sqlite3 instance"
        )


if __name__ == '__main__':
    unittest.main()
