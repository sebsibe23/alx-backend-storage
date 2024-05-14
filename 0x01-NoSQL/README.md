NoSQL
This project focuses on learning and working with NoSQL databases, specifically MongoDB. The objective is to gain a solid understanding of NoSQL concepts, the differences between SQL and NoSQL, and how to work with MongoDB using Python.

Learning Objectives
By the end of this project, you should be able to explain the following topics to anyone without the help of Google:

What NoSQL means
The difference between SQL and NoSQL
ACID (Atomicity, Consistency, Isolation, Durability)
Document storage in NoSQL
Different types of NoSQL databases
Benefits of using a NoSQL database
Querying information from a NoSQL database
Inserting, updating, and deleting information in a NoSQL database
How to use MongoDB
Requirements
MongoDB Command File
All files should be interpreted/compiled on Ubuntu 18.04 LTS using MongoDB version 4.2.
All files should end with a new line.
The first line of all files should be a comment: // my comment.
A README.md file at the root of the project folder is mandatory.
The length of the files will be tested using wc.
Python Scripts
All files should be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7 and PyMongo version 3.10.
All files should end with a new line.
The first line of all files should be exactly #!/usr/bin/env python3.
A README.md file at the root of the project folder is mandatory.
Your code should use the pycodestyle style (version 2.5.*).
The length of the files will be tested using wc.
All your modules should have documentation (run python3 -c 'print(__import__("my_module").__doc__)').
All your functions should have documentation (run python3 -c 'print(__import__("my_module").my_function.__doc__)').
Your code should not be executed when imported (use if __name__ == "__main__":).
Installation Instructions
To install MongoDB 4.2 on Ubuntu 18.04, follow these steps:

Run the following command to import the MongoDB public key:
$ wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
Add the MongoDB repository to the sources list:

$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list
Update the package list:

$ sudo apt-get update
Install MongoDB:

$ sudo apt-get install -y mongodb-org
Check the status of the MongoDB service:

$ sudo service mongod status
If it shows "mongod start/running," MongoDB is successfully installed.

Verify the MongoDB shell version:

$ mongo --version
Install PyMongo using pip:

$ pip3 install pymongo
Verify the PyMongo version:

$ python3
>>> import pymongo
>>> pymongo.__version__
'3.10.1'
If you encounter an issue related to the data directory not found (Data directory /data/db not found., terminating), create the directory manually:

$ sudo mkdir -p /data/db
If the /etc/init.d/mongod file is missing, you can use the provided example file.
Running MongoDB in a Container
If you prefer to use a container to run MongoDB, follow these steps:

Use the "container-on-demand" service to run MongoDB with Ubuntu 18.04.
Connect to the container via SSH or the WebTerminal.
Start MongoDB before working with it:

$ service mongod start
You can use the provided 0-list_databases file to check the databases in the MongoDB container:

$ cat 0-list_databases | mongo
