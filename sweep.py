#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import getpass
import io
import re
import os.path, sys, stat
import sys
from password_file import pw


try:
    if sys.argv[2]:
        header_file_name = sys.argv[2]
except IndexError:
    header_file_name = 'holberton.h'
if len(sys.argv) < 2 or "help " in sys.argv[1]:
    print("")
    print("USAGE: python3 sweep.py project_number")
    print("Example: python3 sweep.py 218")
    print("")
    sys.exit(1)

""" Create a session to retrieve the auth token 
    We need to use a session to persist the login info 
    throughout our scraping as we will need to navigate
    to the project page 
"""
seshy = requests.Session()
page = seshy.get('https://intranet.hbtn.io/auth/sign_in', allow_redirects=True)
soup = BeautifulSoup(page.content, 'html.parser')

authtok = soup.find('input', attrs={'name':'authenticity_token'})
authtok = authtok['value']

print('\n')
print(
    "Welcome to the HippoSweeper, Holberton's #1 Project Creator")
print('\n')
project_number = sys.argv[1]

"""Login Information"""
username = '1661@holbertonschool.com'
password = pw

if ("http" not in project_number):
    project_number = ('https://intranet.hbtn.io/projects/' + project_number)

print("Logging into user '{}'".format(username))


""" Using the authenticity token from the get earlier, login to the intranet with the users info """
pload = {'authenticity_token':authtok, 'user[login]':username,'user[password]':password, 'commit':'Log in'}
seshy.post('https://intranet.hbtn.io/auth/sign_in', data = pload)

page = seshy.get(project_number, allow_redirects=False, data = pload)


""" Stuff to make sure the login was successful """
if (page.status_code is 200):
    pass
else:
    print("Login Failed with code {}".format(page.status_code))
    print("Check your username, password and your project URL.")
    sys.exit(1)

soup = BeautifulSoup(page.content, 'html5lib')
prototype_array = []

for item in soup.find_all('li'):
    item = item.text
    if 'GitHub repository:' in item:
        repo_name = item
        repo_name = repo_name[(repo_name.find('Github repository:')) + 20:]
    if 'Directory: ' in item:
        directory_name = item
        directory_name = directory_name[(directory_name.find('Directory: ')) + 11:]
print('You have selected {}'.format(project_number))
print(directory_name)
    #MAKE DIRECTORY: 0\n"
home = os.getenv("HOME")
directory_path = home + '/' + repo_name + '/' + directory_name
if not os.path.exists(directory_path):
    os.makedirs(directory_path)
    print("Creating: {:s}".format(directory_path))
    ##CD INTO DIRECTORY
os.chdir(directory_path)
print("cd into {:s}".format(directory_path))

run_once = 0
file_and_main_array = []
file_name_array = []
main_file_array = []
project_title = soup.find('h1', class_='gap')
project_title = project_title.text
## CREATE README
r = open('README.md', "w")
r.write("# {}\n## Description\n This project is part of {}:\n## Project tasks :wrench:\n".format(project_title, repo_name))

for question_block in soup.find_all('div', class_='clearfix gap'):
    question_description = question_block.p.text
    question_title = question_block.find('h4', class_='task')
    question_title = question_title.text
    question_title = question_title[question_title.find('\n') + 1:]
    question_title = question_title[4:question_title.find('\n'):]
## MAIN FILE NAME AND MAIN FILE CODE FETCH
    for pre in question_block.find_all('pre'):
        code_block = pre.code.text
        if 'cat ' in code_block:
            main_file = code_block
            main_file_name = main_file[(main_file.find('cat ') + 4):main_file.find('\n')]#print(main_file_name)
            ##Isolate main file, from the cat command to the next command
            main_file = main_file[main_file.find(':~/'):]
            main_file = main_file[main_file.find('\n')+1:]
            main_file = main_file[:main_file.find(':~/')]
            main_file = main_file[:main_file.rfind('\n')]
            main_file = main_file + '\n'
        if 'cat ' not in code_block:
            main_file_name = 'none'
        
## FETCH FILE NAME, PROTOTYPE
    for li_block in question_block.find_all('li'):
        li_block = li_block.text
        if 'File:' in li_block:
            file_name = li_block
            file_name = file_name[(file_name.find('file:')) + 7:]
            if file_name[0] is ' ':
                file_name = file_name[1:]
        if 'Prototype:' in li_block:
            prototype = li_block
            prototype = prototype[11:]
            if prototype[-1] is ' ':
                prototype = prototype[:-1]
            prototype_array.append(prototype)
            comment_prototype = prototype[(prototype.find(' ')) + 1:prototype.find('(')]
            variable = prototype[(prototype.find('(')) + 1:prototype.find(')')]
            variables = variable.split(' ')
            for item in variables:
                if 'char' or 'int' in item:
                    variables.remove(item)
            for x in variables:
                if x is not '*':
                    x = x.replace('*', '')
                if ',' in x:
                    x = x.replace(',', '')
#print(x) come back to work on variable array
            if ',' in variable:
                variable_one = variable[variable.find(' ') + 1:variable.find(',')]
                variable_two = variable[variable.find(',') + 2:]
                variable_two = variable_two[variable_two.find(' ') + 1:]
                if ',' in variable_two:
                    variable_two = variable_two[:variable_two.find(',')]
                if variable_one[0] is '*':
                    variable_one = variable_one[1:]
                if variable_two[0] is '*':
                    variable_two = variable_two[1:]
                try:
                    if variable_three[0] is '*':
                        variable_three = variable_three[1:]
                except NameError:
                    pass
                    
            if ',' not in variable:
                variable_one = variable[variable.find(' ') + 1:]
                if variable_one[0] is '*':
                    variable_one = variable_one[1:]
 ##ADD TO README
    r = open('README.md', "a")
    try:
        r.write("### [{}](./{}) \n* {}\n".format(question_title, file_name, question_description))
    except NameError:
        pass
    ##MAKE FILES
    twenty_spaces = '                    '
    single_space = ' '
    old_file_symbol = ' ~ '
    if run_once is 0:
        print("--------------------------------------------------------------------------------------")
        print("Project files created:")
        print('--------------------------------------------------------------------------------------')
        run_once = 1
## CREATE PROJECT FILES
    try:
        f = open(file_name, "w")
        file_name_array.append(file_name)
        if (".py" in file_name):
            f.write("#!/usr/bin/python3\n")
        elif (".sh" in file_name):
            f.write("#!/bin/bash\n")
        elif (".c" in file_name):
            f.write("#include \"stdio.h\"\n#include \"stdarg.h\"\n#include \"string.h\"\n#include \"stdlib.h\"\n#include \"{}\"\n".format(header_file_name))
            f.write("/**\n*{} - {}\n".format(comment_prototype, question_description))
            if "," in prototype:
                f.write("*@{}: a variable\n*@{}: a variable\n".format(variable_one, variable_two))
                try:
                    f.write("@{}: a variable\n".format(variable_three))
                except NameError:
                    pass
                f.write("*Return: 0\n")
                f.write('**/\n\n')
                f.write('{}\n'.format(prototype[:-1]))
                f.write('{\n\n}\n')
            else:
                f.write("*@{}: a variable\n".format(variable_one))
                f.write("*Return: 0\n")
                f.write('**/\n\n')
                f.write('{}\n'.format(prototype[:-1]))
                f.write('{\n\n}\n')
        else:
            f.write(" ")
        f.close()
    except NameError:
        file_name = 'None'
        file_name_array.append(file_name)
## CREATE MAIN FILES
    try:
        m = open(main_file_name, "w")
        main_file_array.append(main_file_name)
        m.write(main_file)
        m.close()
    except NameError:
        main_file_name = 'None'
        main_file_array.append(main_file_name)
##PRINT FILES CREATED
fmt = '{:<12}{:<25}{}'

print(fmt.format('Question #', 'Project File', 'Main File'))
for i, (name, grade) in enumerate(zip(file_name_array, main_file_array)):
    print(fmt.format(i, name, grade))
print('--------------------------------------------------------------------------------------')

## CREATE HOLBERTON.H
try:
    if sys.argv[2]:
        h = open(sys.argv[2], "w")
        h.write("#ifndef HOLBERTON_H\n#define HOLBERTON_H")
        print("header file: {}".format(sys.argv[2]))
        for item in prototype_array:
            h.write(item)
            h.write('\n')
        h.write("#endif\n")
except IndexError:
    if "low" in repo_name:
        h = open(header_file_name, "w")
        print("created {}".format(header_file_name))
        h.write("#ifndef HOLBERTON_H\n#define HOLBERTON_H")
        for item in prototype_array:
            h.write(item)
            h.write('\n')
        h.write("#endif\n")
    else:
        pass
## ONLY PRINT IF README EXISTS
print('created README.md')
print('--------------------------------------------------------------------------------------')

print('\n')
print('GOOD LUCK WITH YOUR PROJECT')
print('\n')

print(directory_path)

r = open('README.md', "a")
r.write("## Author\n* **DT Van** - [Dtvangogh](https://github.com/dtvangogh)\n")



