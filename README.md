## Python-Coding

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


#### Create virtual environment
- First install this : `pip3 install virtualenv`
- Open a folder and go to inside it. And create an envirenoment inside of your folder: `virtualenv env`
- Activate the environment (for GNU/Linux and Mac): `source env/bin/activate`  (for Windows) : `\env\Scripts\activate.bat`
- When your virtual env is active create requirement file for dependencies: `pip freeze > requirements.txt`


  |      Basics                           |     Intermediate                        |     Advanced                      |
  |---------------------------------------|-----------------------------------------|-----------------------------------|
  |  - variables,numbers,strings,lists    |  - exceptions handling                  |  - multithreading                 |
  |  - dictionary , tuple                 |  - classes , objects                    |  - multiprocessing                |
  |  - if,for control blocks              |  - inheritance                          |  - multiprocessing lock & pool    |
  |  - functions                          |  - generators                           |  - unit tests:pytest              |
  |  - read,write files                   |  - list/dict comprehensions             |  - context managers               |
  |  - modules                            |  - sets,command line argparse           |  - ......                         |
  |  - .......                            |  - .......                              |  - ......                         |



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


### Python Debugging With Pdb
- Import : `import pdb;` 
- Insert the following code at the location where you want to break into the debugger:` pdb.set_trace()`


