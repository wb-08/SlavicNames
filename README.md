# Slavic Names
This code is necessary for parsing Slavic names, surnames , midnames and define gender. Using the Sqlite database. 

# Installation

git clone https://github.com/wb-08/SlavicNames.git

# Usage


```python

from parse_fio import fio_parse, gender_parse
fio_dct = fio_parse('Моргунова Александра Андреевна')
>> {'Surname': 'Моргунова', 'Name': 'Александра', 'Midname': 'Андреевна'}
gender_dct = gender_parse('Моргунова Александра Андреевна')
>> {'fio': 'Моргунова Александра Андреевна', 'gender:': 'f'}
```


# Features

1.Using the Sqlite database

2.The database contains:

* 365673 surnames

* 30577 names

* 46717 midnames


# References

* https://github.com/datacoon/russiannames


