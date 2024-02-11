#!/usr/bin/env python3
"""Defines a console module"""


import cmd
import shlex
import models
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """Defines the HBNBCcOMMAND subclass that inherits from cmd.Cmd"""
    prompt = "(hbnb) "
    __valid_classes = {"BaseModel", "User", "State", "City",
                       "Place", "Amenity", "Review"}

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Method to exit the program"""
        print("")
        return True

    def emptyline(self):
        """shouldn’t execute anything when an empy line is entered"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the
        JSONfile) and prints the id"""
        if not arg:
            print("** class name missing **")
            return

        class_name = arg.split()[0]

        if class_name not in HBNBCommand.__valid_classes:
            print("** class doesn't exist **")
            return
        new_instance = BaseModel()
        print(new_instance.id)
        models.storage.save()

    def do_show(self, arg):
        """ Prints the string representation of an instance based
        on the class name and id"""
        args = arg.split()
        all_objects = models.storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__valid_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in all_objects:
            print("** no instance found **")
        else:
            key = "{}.{}".format(args[0], args[1])
            print(all_objects[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)"""

        args = arg.split()
        all_objects = models.storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__valid_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("**instance id missing **")
        elif f"{args[0]}.{args[1]}" not in all_objects.keys():
            print("** no instance found **")
        else:
            key = f"{args[0]}.{args[1]}"
            del all_objects[key]
            models.storage.save()

    def do_all(self, arg):
        """Prints all string representations of all
        instances,optionally filtered by class"""
        args = arg.split()
        all_obj = models.storage.all()
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in HBNBCommand.__valid_classes:
            print("** class doesn't exist **")
            return

        class_instances = [str(obj) for obj in all_obj.values() if obj.__class__.__name__ == class_name]
        print(class_instances)


    def do_update(self, arg):
        """Updates an instance based on the class name and id by
        adding or updating attribute (save the change into the
        JSON file)"""
        args = shlex.split(arg)
        valid_obj = models.storage.all()

        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in HBNBCommand.__valid_classes:
            print("** class doesn't exist **")
            return False
        if len(args) == 1:
            print("** instance id missing **")
            return False
        if f"{args[0]}.{args[1]}" not in valid_obj.keys():
            print("** no instance found **")
            return False
        if len(args) == 2:
            print("** attribute name missing **")
            return False
        if len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(args) == 4:
            obj = valid_obj["{}.{}".format(args[0], args[1])]
            if args[2] in obj.__class__.__dict__.keys():
                value_type = type(obj.__class__.__dict__[args[2]])
                obj.__dict__[args[2]] = value_type(args[3])
            else:
                obj.__dict__[args[2]] = args[3]
        elif type(eval(args[2])) == dict:
            obj = valid_obj["{}.{}".format(args[0], args[1])]
            for key, value in eval(args[2]).items():
                if (key in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[key]) in {str, int,
                                                              float}):
                    value_type = type(obj.__class__.__dict__[key])
                    obj.__dict__[key] = value_type(value)
                else:
                    obj.__dict__[key] = value
        models.storage.save()

    def do_count(self, arg):
        """
        A method to count the number of instances of a class
        """
        args = arg.split()
        count = 0
        for obj in models.storage.all().values():
            if args[0] == obj.__class__.__name__:
                count += 1
        print(count)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
