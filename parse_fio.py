import sqlite3

fio_dict = {}
gender_dict = {}
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


def define_gender_by_surname(surname):
    cursor.execute("SELECT gender FROM surnames WHERE surname=?", ([surname.lower()]))
    record = cursor.fetchone()

    if record is None:
        return False
    else:
        if record[0] is None:
            return False
        else:
            return record[0]


def define_gender_by_name(name):
    cursor.execute("SELECT gender FROM names WHERE name=?", ([name.lower()]))
    record = cursor.fetchone()

    if record is None:
        return False
    else:
        if record[0] is None:
            return False
        else:
            return record[0]


def find_fio(value):
    if search_in_midnames(value) is True:
        fio_dict.update({'Midname': value})

    elif search_in_names(value) is True:
        fio_dict.update({'Name': value})

    elif search_in_surnames(value) is True:
        fio_dict.update({'Surname': value})


def define_gender(fio, value):
    gender_by_surname = define_gender_by_surname(value)
    if gender_by_surname is False:
        gender_by_name = define_gender_by_name(value)
        if gender_by_name is False:
            gender_dict.update({'fio': fio, 'gender:': 'u'})
        else:
            gender_dict.update({'fio': fio, 'gender:': gender_by_name})
            return True
    else:
        gender_dict.update({'fio': fio, 'gender:': gender_by_surname})
        return True


def fio_parse(fio):
    fio_lst = fio.split(' ')
    for i in fio_lst:
        find_fio(i)
    return fio_dict


def gender_parse(fio):
    fio_lst = fio.split(' ')
    for i in fio_lst:
        if define_gender(fio, i):
            break
    return gender_dict










