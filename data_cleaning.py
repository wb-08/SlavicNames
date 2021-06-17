import sqlite3
import re


# нет одинаковых записей в names, surnames и midnames:
# SELECT fio, COUNT(*) as cnt FROM (SELECT midname as fio from midnames
# UNION
# SELECT name as fio FROM names
# UNION
# SELECT surname as fio FROM surnames) GROUP BY fio HAVING cnt>1

def remove_duplicates(table_name, group_row):
    cursor.execute("DELETE FROM {0} WHERE id NOT IN (SELECT id FROM {1} GROUP BY {2})".format(table_name, table_name, group_row))
    conn.commit()


def has_cyrillic(text):
    all_letters = [letter for letter in text]
    cyrillic_letters = [letter for letter in text if bool(re.search(r'[а-яА-Яё^c\s-]', letter))]
    return bool(all_letters == cyrillic_letters)


def remove_latin_records(table_name):
    cursor.execute("SELECT * FROM {0}".format(table_name))
    records = cursor.fetchall()
    for record in records:
        have_cyrillic_letters = has_cyrillic(record[1])
        if have_cyrillic_letters is False:
            cursor.execute("DELETE FROM {0} WHERE id=?".format(table_name), [(record[0])])
        conn.commit()


if __name__ == '__main__':
    conn = sqlite3.connect('db/fio.db')
    cursor = conn.cursor()
    # remove_duplicates('surnames', 'surname')
    # remove_duplicates('names', 'name')
    # remove_duplicates('midnames', 'midname')
    # remove_latin_records('names')
    # remove_latin_records('surnames')
    # remove_latin_records('midnames')