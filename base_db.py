#-*- coding:utf-8-*-
import sqlite3


DATABASES = {
    # "维权": {"create":, "query":, "insert":,}
}


class DB():
    def __init__(self, db):
        self._conn = sqlite3.connect(db)
        self._cursor = self._conn.cursor()
        self._db = db
    
    def create_table(self, table_name, field_type ):
        try:
            self._cursor.execute('create table {0} ({1});'.format(table_name, field_type))
        except sqlite3.OperationalError as e:
            print("{0}".format(e))

    def __del__(self):
        try:
            self._cursor.close()
            self._conn.close()
        except:
            pass

    def close(self):
        self.__del__()

    def _select(self, sql):
        try:
            result = self._cursor.execute(sql)
        except sqlite3.Error as e:
            print(e)
            result = False
        return result

    def query(self, table_name, column='*', condition=''):
        condition = ' where ' + condition if condition else None
        if condition:
            sql = "select %s from %s %s" % (column, table_name, condition)
        else:
            sql = "select %s from %s" % (column, table_name)
        self._select(sql)
        return self._cursor.fetchall()

    def insert(self, table_name, tdict):
        column = ''
        value = ''
        for key in tdict:
            column += ',' + key
            value += "','" + tdict[key]
        column = column[1:]
        value = value[2:] + "'"
        sql = "insert into %s(%s) values(%s)" % (table_name, column, value)
        try:
            self._cursor.execute(sql)
            self._conn.commit() 
        except sqlite3.IntegrityError as e:
            print(e)
            return -1 
        return self._cursor.lastrowid #返回最后的id

    def update(self, table_name, tdict, condition=''):
        if not condition:
            print ("must have id")
            exit()
        else:
            condition = 'where ' + condition
        value = ''
        for key in tdict:
            value += ",%s='%s'" % (key, tdict[key])
        value = value[1:]
        sql = "update %s set %s %s" % (table_name, value, condition)
        self._cursor.execute(sql)
        return self._affected_num()

    def delete(self, table_name, condition=''):
        condition = 'where ' + condition if condition else None
        sql = "delete from %s %s" % (table_name, condition)
        # print sql
        self._cursor.execute(sql)
        self._conn.commit()
        return self._affected_num() #返回受影响行数

    def rollback(self):
            self._conn.rollback()

    def _affected_num(self):
        return self._cursor.rowcount

def get_time():
    import time
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

if __name__ == '__main__':
    
    db='db/test.db'
    d = DB(db)

    field_type="id integer  primary key AUTOINCREMENT,\
                project varchar(128) not null, \
                name varchar(40) not null,\
                floor varchar(20) not null,\
                time varchar(40) not null,\
                UNIQUE (project, name, floor)"

    table_name='user'
    d.create_table(table_name, field_type)
    tdict = {
        "project": PROJECTS["001"],
        "name":"lilei",
        "floor": "2012",
        "time":get_time()
    }
    tdict1 = {
        "project": PROJECTS["001"],
        "name":"lilei",
        "floor": "2012",
        "time":get_time()
    }
    tdict2 = {
        "project": PROJECTS["001"],
        "name":"lilei",
        "floor": "2013",
        "time":get_time()
    }
    print(d.insert(table_name, tdict))
    print(d.insert(table_name, tdict1))
    print(d.insert(table_name, tdict2))
    # print(d.query(table_name, 'project', 'floor=2012'))
    print(d.query(table_name, '*'))
    # d.delete(table_name, "floor=2012")
    # print(d.query(table_name, '*', 'floor=2012'))

    # print(d.query())