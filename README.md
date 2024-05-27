# guolei_py3_database

## introduce

**guolei python3 database library**



## software architecture

~python 3.11

## installation tutorial

```shell
pip install guolei_py3_database
```

## catalog description
### pymysql

```python
# import module
from guolei_py3_database import pymysql

cfg = {
    'host': '<HOST>',
    'port': '<PORT>',
    'user': '<USER>',
    'password': '<PASSWORD>',
    'database': '<DATABASE>',
}
connect = pymysql.get_connect(**cfg)


@pymysql.call_get_connect()
def _call_get_connect():
    return {
        'host': '<HOST>',
        'port': '<PORT>',
        'user': '<USER>',
        'password': '<PASSWORD>',
        'database': '<DATABASE>',
    }


connect = _call_get_connect()


@pymysql.call_execute(connect=connect, is_closed_connect=False)
def _call_execute():
    query = "your sql"
    args = "your sql parameters"
    return query, args


print(_call_execute())


@pymysql.call_execute_many(connect=connect, is_closed_connect=False)
def _call_execute_many():
    query = "your sql"
    args = "your sql parameters"
    return query, args


print(_call_execute_many())


@pymysql.call_execute_fetch_one(connect=connect, is_closed_connect=False)
def _call_execute_fetch_one():
    query = "your sql"
    args = "your sql parameters"
    return query, args


print(_call_execute_fetch_one())


@pymysql.call_execute_fetch_all(connect=connect, is_closed_connect=False)
def _call_execute_fetch_all():
    query = "your sql"
    args = "your sql parameters"
    return query, args


print(_call_execute_fetch_all())


@pymysql.call_execute_transaction(connect=connect, is_closed_connect=False)
def _call_execute_transaction():
    query = "your sql"
    args = "your sql parameters"
    # more sql and args
    # ...
    return [(query, args)]


print(_call_execute_transaction())

```

### sqlite3
```python
from guolei_py3_database import sqlite3

cfg = {
    # sqlite3 parameters
}
connect = sqlite3.get_connect(**cfg)


@sqlite3.call_get_connect()
def _call_get_connect():
    return {
        # sqlite3 parameters
    }


connect = _call_get_connect()


@sqlite3.call_execute(connect=connect, is_closed_connect=False)
def _call_execute():
    query = "your sql"
    args = "your sql parameters"
    return query, args


print(_call_execute())


@sqlite3.call_execute_many(connect=connect, is_closed_connect=False)
def _call_execute_many():
    query = "your sql"
    args = "your sql parameters"
    return query, args


print(_call_execute_many())


@sqlite3.call_execute_fetch_one(connect=connect, is_closed_connect=False)
def _call_execute_fetch_one():
    query = "your sql"
    args = "your sql parameters"
    return query, args


print(_call_execute_fetch_one())


@sqlite3.call_execute_fetch_all(connect=connect, is_closed_connect=False)
def _call_execute_fetch_all():
    query = "your sql"
    args = "your sql parameters"
    return query, args


print(_call_execute_fetch_all())


@sqlite3.call_execute_transaction(connect=connect, is_closed_connect=False)
def _call_execute_transaction():
    query = "your sql"
    args = "your sql parameters"
    # more sql and args
    # ...
    return [(query, args)]


print(_call_execute_transaction())

```
### strictredis

```python
from guolei_py3_database import strictredis

cfg = {
    # StrictRedis parameters
}
connect = strictredis.get_connect()


@strictredis.call_get_connect()
def _call_get_connect():
    return {
        # StrictRedis parameters
    }


@strictredis.call_execute(connect=connect, attr="get")
def _call_execute():
    return "attr parameters"
```



