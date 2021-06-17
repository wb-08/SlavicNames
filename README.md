# Slavic Names
This code is necessary for parsing  Slavic names, surnames and midnames. Using the Sqlite database. 

# Installation

git clone https://github.com/wb-08/SlavicNames.git

# Usage


from parse_fio import fio_parse

fio_dct = fio_parse('Смоляк Маргарита Генадьевна')

{'Surname': 'Смоляк', 'Name': 'Маргарита', 'Midname': 'Генадьевна'}

# Features

The database contains:

* 365673 surnames

* 30577 names

* 46717 midnames

# References

* https://github.com/datacoon/russiannames


