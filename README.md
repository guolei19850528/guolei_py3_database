## 介绍

**guolei python3 database library**



## 软件架构

~python 3.*

## 安装教程

```shell
pip install guolei-py3-database
```

## 目录说明
### pymysql 示例

```python
from guolei_py3_database import pymysql as gl_pymysql

database=gl_pymysql.Database(connect_args=(), connect_kwargs={})

# must be call
database.open_connect()

database.execute()
database.executemany()
database.transaction()
database.rowcount()
database.lastrowid()
database.fetchone()
database.fetchall()

# must be call
database.close_connect()


```




