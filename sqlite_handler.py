# -*- coding: utf-8 -*-

"""
    Created by : Joe
"""

import sqlite3
import os.path


def main():
    print('Bars_Brest - sqlite_handler.py')


def check_db():
    if not os.path.isfile('bars.db'):
        create_db()


def insert_data(name, address, lat, lng, phone, website, gmaps_id, icon_url, types):
    try:
        db = sqlite3.connect('bars.db')

        cursor = db.cursor()
        cursor.execute('''  INSERT INTO bars(name, address, lat, lng, phone, website, gmaps_id, icon_url, types)
                            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                       (name, address, lat, lng, phone, website, gmaps_id, icon_url, types))
        print("Data added successfully");

        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()


def create_db():
    try:
        db = sqlite3.connect('bars.db')
        print("Database opened successfully")

        db.execute(''' CREATE TABLE BARS (
                       ID               INTEGER PRIMARY KEY AUTOINCREMENT,
                       NAME             TEXT    NOT NULL,
                       ADDRESS          TEXT,
                       LAT              REAl,
                       LNG              REAL,
                       PHONE            TEXT,
                       WEBSITE          TEXT,
                       GMAPS_ID         TEXT,
                       ICON_URL         TEXT,
                       TYPES            TEXT
                       );''')
        print("Table created successfully");
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()


if __name__ == '__main__':
    main()


