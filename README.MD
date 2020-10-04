## HIPPOSWEEPER
### Get Started
```
git clone https://github.com/dtvangogh/hipposweeper_2020
cd hipposweeper_2020
./install.sh
```
include your password in the password_file and add your username on line 38 of sweep.py \
To run:
```
python3 vagrant_sweep.py 217  
```

### Description
A python script that creates repositories, directories, project files, and main.c/main.py files, and very pretty README files (README creation will be released in a few days)
This script doesn't just create files...it fills the file with an include header line, comment bullets, and the prototype.Adding an argument after the project number controls the name of the header file. This controls the name of the header file in each C file, too.
Example: python3 sweep.py 217 exampleHeader.h
### Example Usage
```
$ python3 vagrant_sweep.py 217


Welcome to the HippoSweeper, Holberton's #1 Project Creator


Logging into user '1661@holbertonschool.com'
You have selected https://intranet.hbtn.io/projects/217
0x06-pointers_arrays_strings
Creating: /Users/qpv2/holbertonschool-low_level_programming/0x06-pointers_arrays_strings
cd into /Users/qpv2/holbertonschool-low_level_programming/0x06-pointers_arrays_strings
--------------------------------------------------------------------------------------
Project files created:
--------------------------------------------------------------------------------------
Question #  Project File             Main File
0           0-strcat.c               0-main.c
1           1-strncat.c              1-main.c
2           2-strncpy.c              2-main.c
3           3-strcmp.c               3-main.c
4           4-rev_array.c            4-main.c
5           5-string_toupper.c       5-main.c
6           6-cap_string.c           6-main.c
7           7-leet.c                 7-main.c
8           8-rot13.c                8-main.c
9           100-print_number.c       100-main.c
10          101-magic.c              100-main.c
11          102-infinite_add.c       102-main.c
12          103-print_buffer.c       103-main.c
--------------------------------------------------------------------------------------
created holberton.h
created README.md
--------------------------------------------------------------------------------------


GOOD LUCK WITH YOUR PROJECT
```

### Prerequisites
```
./install.sh
```
sudo apt-get install python3\
sudo apt-get install python3-pip\
sudo pip3 install beautifulsoup4\
sudo pip3 install html5lib\
sudo pip install requests\	
sudo pip install lxml
```
```

### File Contents
This repository contains the following files:

|   **File**   |   **Description**   |
| -------------- | --------------------- |
|sweep.py | the main file. Run by using python3 sweep.py |
|password_file.py | this is where you should store your password. Enter your password for password = 'insertPasswordHere'

### Usage and Installation
Clone the repository, compile with compilation flags, listed below, then run the executable.
```
$ git clone https://github.com/dtvangogh/hipposweeper_2020
```
For username enter your own username. Find this line at line 38 of the sweep.py file. Put your password in password_file.py
```
"""Login Information"""
username = '1661@holbertonschool.com'
password = pw
```
### Compilation
This code was compiled this way:
` $ python3 sweep.py 243 `
1st Argument will choice what project you want. Project number is in the URL. Always a 3 digit number
` $ python3 sweep.py 243 2nd_argument `
2nd argument will control the name of your header file, some projects have different header file names


### Authors
[DT Van](github.com/dtvangogh)

