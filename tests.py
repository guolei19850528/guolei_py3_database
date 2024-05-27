import unittest

import pymysql

from guolei_py3_database.pymysql import get_connect,call_get_connect,call_execute_fetch_one,call_execute_fetch_one


class PymysqlCase(unittest.TestCase):
    def test_connect(self):
        connect = get_connect(**{
            'host': 'localhost',
            'port': 3306,
            'user': 'root',
            'password': '123456',
            'database': 'jtwy_smarty_community_dev_db',
        })
        self.assertTrue(
            isinstance(connect, pymysql.Connect),
            "connect not a pymysql instance"
        )

    def test_call_connect(self):
        @call_get_connect()
        def _call_connect():
            return {
                'host': 'localhost',
                'port': 3306,
                'user': 'root',
                'password': '123456',
                'database': 'jtwy_smarty_community_dev_db',
            }
        connect = _call_connect()
        print(connect)
        self.assertTrue(
            isinstance(connect, pymysql.Connect),
            "connect not a pymysql instance"
        )

    def test_call_fetch_all(self):
        @call_get_connect()
        def _call_connect():
            return {
                'host': 'localhost',
                'port': 3306,
                'user': 'root',
                'password': '123456',
                'database': 'jtwy_smarty_community_dev_db',
            }

        connect = _call_connect()

        @call_execute_fetch_one(connect=connect)
        def _call_execute_fetch_all():
            return "select * from ws_parking_auth_auto_audits",{}
        results = _call_execute_fetch_all()
        print(results)



if __name__ == '__main__':
    unittest.main()
