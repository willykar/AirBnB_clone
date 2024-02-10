AirBnB Command Interpreter
Description
This project aims to develop a command-line interpreter for managing AirBnB objects. The interpreter allows users to perform various operations such as creating new objects, retrieving objects, updating attributes, and more.

Command Interpreter
How to Start
To start the command interpreter, execute the console.py script in the terminal.

bash
Copy code
$ ./console.py
How to Use
Once the command interpreter is running, you will see a prompt (hbnb). You can type commands at this prompt to interact with the AirBnB objects.

Examples
Here are some examples of commands you can use:

To display available commands:

bash
Copy code
(hbnb) help
To create a new object:

bash
Copy code
(hbnb) create User
To display all objects of a specific class:

bash
Copy code
(hbnb) all User
To update attributes of an object:

bash
Copy code
(hbnb) update User 1234 first_name "Bob"
To retrieve an object by ID:

bash
Copy code
(hbnb) show User 1234
To delete an object:

bash
Copy code
(hbnb) destroy User 1234
To quit the command interpreter:

bash
Copy code
(hbnb) quit
