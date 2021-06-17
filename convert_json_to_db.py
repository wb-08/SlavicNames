import sqlite3
import json


def convert_to_json_format(input_file_name, output_file_name):
    with open(input_file_name, 'r') as file:
        lines = file.readlines()
        first = lines[0]
        last = lines[-1]
        for line in lines:
            if line == last:
                new_line = line + ']'
            elif line == first:
                new_line = '[' + line + ','
            else:
                new_line = line.replace('\n', ',\n')
            writing_file = open(output_file_name, "a")
            writing_file.write(new_line)


def read_json(file_name):
    with open(file_name) as file:
        data = json.loads(file.read())
        return data


def parse_midnames(file_name):
    data = read_json(file_name)
    for i in range(len(data)):
        midname = data[i]['text'].lower()
        try:
            ethnicity = data[i]['ethnic'][0]
        except KeyError:
            ethnicity = None
        cursor.execute("insert into midnames (midname, ethnicity) values (?, ?)",
                       (midname, ethnicity))
    conn.commit()


def parse_names(file_name):
    data = read_json(file_name)
    for i in range(len(data)):
        name = data[i]['text'].lower()
        try:
            ethnicity = data[i]['ethnic'][0]
        except KeyError:
            ethnicity = None
        try:
            gender = data[i]['gender']
        except KeyError:
            gender = None
        cursor.execute("insert into names (name, ethnicity, gender) values (?, ?, ?)",
                       (name, ethnicity, gender))
    conn.commit()


def parse_surnames(file_name):
    data = read_json(file_name)
    for i in range(len(data)):
        surname = data[i]['text'].lower()
        try:
            ethnicity = data[i]['ethnic'][0]
        except KeyError:
            ethnicity = None
        try:
            gender = data[i]['gender']
        except KeyError:
            gender = None
        cursor.execute("insert into surnames (surname, ethnicity, gender) values (?, ?, ?)",
                       (surname, ethnicity, gender))

        try:
            f_surname = data[i]['f_form'].lower()
            gender_f = 'f'
            try:
                ethnicity_f = data[i]['ethnic'][0]
            except KeyError:
                ethnicity_f = None

            cursor.execute("insert into surnames (surname, ethnicity, gender) values (?, ?, ?)",
                           (f_surname, ethnicity_f, gender_f))
        except KeyError:
            pass

        try:
            m_surname = data[i]['m_form'].lower()
            gender_m = 'm'
            try:
                ethnicity_m = data[i]['ethnic'][0]
            except KeyError:
                ethnicity_m = None

            cursor.execute("insert into surnames (surname, ethnicity, gender) values (?, ?, ?)",
                           (m_surname, ethnicity_m, gender_m))
        except KeyError:
            pass

    conn.commit()


if __name__ == '__main__':
    conn = sqlite3.connect('db/fio.db')
    cursor = conn.cursor()
    # input_file_name_lst = ['dump/names/fullnames.json', 'dump/names/midnames.json',
    #                        'dump/names/names.json', 'dump/names/surnames.json']
    #
    # output_file_name_lst = ['dump/names/fullnames_1.json', 'dump/names/midnames_1.json',
    #                         'dump/names/names_1.json', 'dump/names/surnames_1.json']
    #
    # for i in range(len(input_file_name_lst)):
    #     convert_to_json_format(input_file_name_lst[i], output_file_name_lst[i])

    # parse_midnames('dump/names/midnames_1.json')
    # parse_names('dump/names/names_1.json')
    # parse_surnames('dump/names/surnames_1.json')
