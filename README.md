# GlobalXAssessment - Name Sorter

## Quick Start
Before starting, install [Python3](https://www.python.org/downloads/) and [Git](https://git-scm.com/downloads)
```sh
$ git clone https://github.com/RichardFi/GlobalXAssessment.git
```
Executing the program in the following way
```sh
$ cd GlobalXAssessment
$ python3 src/name_sorter.py unsorted-names-list.txt
```
Testing the program in the following way
```sh
$ python3 -m unittest discover test
```

## Project Structure

```
GlobalXAssessment
├── src
|   ├── __init__.py
|   ├── file_read.py
|   ├── file_write.py
|   ├── name_sorter.py
|   ├── name.py
|   └── validation.py
├── test
|   ├── test_file_read.py
|   ├── test_file_write.py
|   ├── test_name_sorter.py
|   ├── test_name.py
|   └── test_validation.py
├── .gitignore
├── unsorted-names-lists.txt
└── README.md
```

