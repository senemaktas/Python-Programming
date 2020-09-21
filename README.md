## Python-Coding
**It includes coding of various algorithms and examples,tricks with Python programming language.**

### To run Python programs on the Linux terminal:
- Open termnal `CTRL+ALT+T`
- Update the packages list: `sudo apt update`
- Install Python3 : `sudo apt-get install python3`
- Create a folder on computer to use for Python programs, such as `~/pythonpractice`
- Type `cd ~/pythonpractice` to change directory to your pythonpractice folder.
- Open text editor and create the python file for example: `nano hello.py` or `gedit hello.py` and save program in that folder.
- Make sure the first line of file has, add #! and the path of the Python interpreter `#!/usr/bin/env python`.
- Make the script executable by `chmod +x  <filename>.py`.
- And run it as `./<filename>.py`.For example: `./hello.py` . 
- `python <filename>.py` for Python 2.x  `python3 <filename>.py` for Python 3.x


### There are examples with Flask, which is the Python Web Framework:
- Install Flask : `pip3 install Flask`
- Import : `from flask import Flask`
- install SQLAlchemy the Database Toolkit for Python: `pip3 install flask-sqlalchemy`
- Import : `from flask_sqlalchemy import SQLAlchemy`


***Project layout should look like this:*** <br/>
Project_name/ <br/>
├── templates/<br/>
│   └── base.html<br/>
└── static/<br/>
│    └── style.css     
-https://flask.palletsprojects.com/en/1.1.x/tutorial/layout/


### Basics                           
- variables,numbers,strings,lists
- dictionary , tuple
- if,for control blocks
- functions
- read,write files
- modules
- .......

### intermediate
- exceptions handling
- classes , objects
- inheritance
- generators
- list/dict comprehensions
- sets,command line argparse
- .......

### advanced
- multithreading
- multiprocessing
- multiprocessing lock & pool
- unit tests:pytest
- context managers
- ......
