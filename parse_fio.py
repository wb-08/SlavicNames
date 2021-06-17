import sqlite3

fio_dict = {}
conn = sqlite3.connect('db/fio.db')
cursor = conn.cursor()


def search_in_surnames(surname):
    cursor.execute("SELECT surname FROM surnames WHERE surname=?", ([surname.lower()]))
    record = cursor.fetchone()

    if record is None:
        return False
    else:
        return True


def search_in_names(name):
    cursor.execute("SELECT name FROM names WHERE name=?", ([name.lower()]))
    record = cursor.fetchone()

    if record is None:
        return False
    else:
        return True


def search_in_midnames(midname):
    cursor.execute("SELECT midname FROM midnames WHERE midname=?", ([midname.lower()]))
    record = cursor.fetchone()

    if record is None:
        return False
    else:
        return True


def find_fio(value):
    if search_in_midnames(value) is True:
        fio_dict.update({'Midname': value})

    elif search_in_names(value) is True:
        fio_dict.update({'Name': value})

    elif search_in_surnames(value) is True:
        fio_dict.update({'Surname': value})


def parse_fio(fio):
    fio_lst = fio.split(' ')
    for i in fio_lst:
        find_fio(i)
    return fio_dict




