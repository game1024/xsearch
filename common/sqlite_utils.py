import sqlite3
import json
import sys

class SQLiteDB:
    def __init__(self, path):
        self.conn = sqlite3.connect(path, detect_types=sqlite3.PARSE_DECLTYPES)

    def select(self, query):
        cursor = self.conn.cursor()
        cursor = cursor.execute(query)
        self.conn.commit()
        return cursor


    def create(self, query):
        cursor = self.conn.cursor()
        cursor = cursor.execute(query)
        self.conn.commit()
        return cursor


    def insert(self, query, values):
        cursor = self.conn.cursor()
        cursor = cursor.execute(query, values)
        self.conn.commit()
        return cursor

    def insert_batch(self, query, many_values):
        cursor = self.conn.cursor()
        cursor = cursor.executemany(query, many_values)
        self.conn.commit()
        return cursor

if __name__ == '__main__':
    db = SQLiteDB('demo.db')
    db.create('''
        CREATE TABLE IF NOT EXISTS response_details (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        a_response TEXT NOT NULL,
        b_response TEXT NOT NULL
        )
    ''')

    json = json.dumps({
        'data':{
            'items': [
                         {
                             'id': '00000000',
                             'name': '商品名称',
                             'L1_category_name': '一级类目名称',
                             'L2_category_name': '二级类目名称',
                             'L3_category_name': '三级类目名称',
                             'ext_map': {
                                 'score': 0.9123,
                                 'dumps': 'search.xxxx.yyyy.zzzz'
                             }
                         }
                     ]*20
        },
        'traceId': '00000000000000000',
        'code':200
    }, ensure_ascii=False)

    # values = (json,json)
    # batch = []
    # for i in range(100):
    #     batch = [values]*100
    #
    #     db.insert_batch('''
    #     INSERT INTO response_details (a_response, b_response)
    #     VALUES (?, ?)
    #     ''', batch)
    #
    #     i+=1

    #sys.stdout.reconfigure(encoding='utf-8')
    cursor = db.select('''SELECT * FROM response_details''')


    for row in cursor:
        print(row[1])