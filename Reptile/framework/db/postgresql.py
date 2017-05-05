# -*- coding: utf-8 -*-

__author__ = 'saligia'

import psycopg2
from framework.settings import DbConfigure
from collections import OrderedDict


class Database(object):
    connect = None

    def __init__(self):
        try:
            self.connect = psycopg2.connect(
                database=DbConfigure['DataCenter']['dbname'],
                user=DbConfigure['DataCenter']['username'],
                password=DbConfigure['DataCenter']['password'],
                host=DbConfigure['DataCenter']['host'],
                port=DbConfigure['DataCenter']['port']
            )
        except psycopg2.Error, e:
            print e.message
            exit

    def get_table(self, table_name):
        return Table(self.connect, table_name)

    def fetchall(self, sql, data, size=5000):
        cursor = self.connect.cursor()
        try:
            cursor.execute(sql, tuple(data))
        except psycopg2.Error, e:
            print(e.message)
        if size == 1:
            result = cursor.fetchone()
        else:
            result = cursor.fetchmany(size)
        self.connect.commit()
        cursor.close()
        return result

    def __del__(self):
        self.connect.close()


class Table(object):
    connect = None
    cursor = None
    table_name = None

    def __init__(self, connect, table_name):
        self.connect = connect
        self.cursor = self.connect.cursor()
        self.table_name = table_name

    def __get_insert_sql(self, item):
        item = OrderedDict(item)
        data = []
        fields = []
        values = []
        for field, value in item.items():
            data.append(value)
            values.append('%s')
            fields.append('"' + field + '"')
        fields = ",".join(fields)
        values = ",".join(values)
        sql = 'INSERT INTO "' + self.table_name + '"(' + fields + ') VALUES (' + values + ')'
        return sql, data

    def __get_update_sql(self, item, where):
        item = OrderedDict(item)
        where = OrderedDict(where)
        data = []
        fields = []
        restriction = []
        for field, value in item.items():
            fields.append('"' + field + '"=%s')
            data.append(value)
        for field, value in where.items():
            restriction.append('"' + field + '"=%s')
            data.append(value)
        restriction = " and ".join(restriction)
        fields = ",".join(fields)
        sql = 'UPDATE ' + '"' + self.table_name + '" set ' + fields + ' WHERE ' + restriction
        return sql, data

    def insert(self, item):
        self.__execute(self.__get_insert_sql(item))

    def update(self, item, where):
        self.__execute(self.__get_update_sql(item, where))

    def __execute(self, sql_data):
        try:
            self.cursor.execute(sql_data[0], tuple(sql_data[1]))
        except psycopg2.Error, e:
            print(e.message)

        self.connect.commit()
        self.cursor.close()

    def inserts(self, items):
        self.__executes(items)

    def updates(self, items, where):
        self.__executes(items, where)

    def __executes(self, items, where=None):
        if where is None:
            for item in items:
                sql_data = self.__get_insert_sql(item)
                try:
                    self.cursor.execute(sql_data[0], tuple(sql_data[1]))
                except psycopg2.Error, e:
                    print(e.message)
        elif where is not None:
            for item in items:
                sql_data = self.__get_update_sql(item, where)
                try:
                    self.cursor.execute(sql_data[0], tuple(sql_data[1]))
                except psycopg2.Error, e:
                    print(e.message)

        self.connect.commit()
        self.cursor.close()
