# -------------------------#
# ---Program by MiVainer---#

import sqlite3

def update_sqlite_table():
    try:
        sqlite_connection = sqlite3.connect('db.sqlite3')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_insert_query = """INSERT INTO skills_category (id, name) VALUES (8, 'Conteiner')"""
        cursor.execute(sqlite_insert_query)
        sqlite_connection.commit()
        print('Запись успешно внесена в таблицу skills_category')
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

update_sqlite_table()