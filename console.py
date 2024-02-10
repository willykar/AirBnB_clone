#!/usr/bin/env python3
"""Defines a console module"""

import cmd
import models
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Defines the HBNBCcOMMAND subclass that inherits from cmd.Cmd"""
    prompt = "(hbnb) "
    __valid_classes = {"BaseModel", "User", "State", "City", "Place", "Amenity", "Review"}

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
            print("** class name missing **")
            return
        new_instance = BaseModel()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """ Prints the string representation of an instance based
        on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.__valid_classes:
             print("** class doesn't exist **")
             return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}{}".format(args[0], args[1])
        all_objects = models.storage.all()
        if key not in all_objects:
            print("** no instance found **")
        else:
            print(all_objects[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)"""

        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in HBNBCommand.__valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}{}".format(args[0], args[1])
        all_objects = storage.all()

        if key not in all_objects:
            print("** no instance found **")

        else:
            del all_objects[key]
            storage.save()

    def do_all(self, arg):
        """Prints all string representations of all instances,
        optionally filtered by class"""
        args = arg.split()
        obj_list = []
        if len(args) == 0:
            obj_dict = models.storage.all()
        elif args[0] in HBNBCommand.__valid_classes:
            obj_dict = models.storage.all()
        else:
            print("** class doesn't exist **")
            return False
        for key in obj_dict:
            obj_list.append(str(obj_dict[key]))

        print("[", ", ".join(obj_list), "]")

    def do_update(self, arg):
        """Updates an instance based on the class name and id by
        adding or updating attribute (save the change into the
        JSON file). """
        args = parse(arg)
        objdict = storage.all()

        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in HBNBCommand.__valid_classes:
            print("** class doesn't exist **")
            return False
        if len(args) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(args[0], args[1]) not in objdict.keys():
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
            obj = objdict["{}.{}".format(args[0], args[1])]
            if args[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[args[2]])
                obj.__dict__[args[2]] = valtype(args[3])
            else:
                obj.__dict__[args[2]] = args[3]
        elif type(eval(args[2])) == dict:
            obj = objdict["{}.{}".format(args[0], args[1])]
            for k, v in eval(args[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
