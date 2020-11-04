
# Importing CSV file into Sqlite Server

import csv
import sqlite3
import glob
import os

# creating tables in db using mutiple csv in the directory
def do_directory(dirname, db):
    for filename in glob.glob(os.path.join(dirname, '*.csv')):
        do_file(filename, db)

# creating table in db using single csv
def do_file(filename, db):
        with open(filename) as f:
            with db:
                data = csv.DictReader(f)
                cols = data.fieldnames
                table=os.path.splitext(os.path.basename(filename))[0]

                sql = 'drop table if exists "{}"'.format(table)
                db.execute(sql)

                sql = 'create table "{table}" ( {cols} )'.format(
                    table=table,
                    cols=','.join('"{}"'.format(col) for col in cols))
                db.execute(sql)

                sql = 'insert into "{table}" values ( {vals} )'.format(
                    table=table,
                    vals=','.join('?' for col in cols))
                db.executemany(sql, (list(map(row.get, cols)) for row in data))

if __name__ == '__main__':
    conn = sqlite3.connect(r'C:\test.db')
    do_directory(r'D:\SQL_SalesAnalysis\DataSet', conn)

"""
    conn = sqlite3.connect(r'C:\test.db')
    do_file(r'D:\SQL_SalesAnalysis\file.csv', conn)

"""    
