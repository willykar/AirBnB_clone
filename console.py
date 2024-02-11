#!/usr/bin/env python3
"""Defines a console module"""


import cmd
import models
from models.base_model import BaseModel
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
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """ Prints the string representation of an instance based
        on the class name and id"""
        args = arg.split()
        class_name = args[0]
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            class_name = args[0]
            if class_name not in HBNBCommand.__valid_classes:
                print("** class doesn't exist **")
            else:
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

        if len(args) > 0 and args[0] not in HBNBCommand.__valid_classes:
            print("** class doesn't exist **")
        else:
            valid_objs = []
            for obj in all_obj.values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    valid_objs.append(obj.__str__())
                elif len(args) == 0:
                    valid_objs.append(obj.__str__())
            print(valid_objs)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by
        adding or updating attribute (save the change into the
        JSON file). """
        try:
            if not arg:
                raise SyntaxError()
            my_list = split(arg, " ")
            if my_list[0] not in HBNBCommand.__valid_classes:
                raise NameError()
            if len(my_list) < 2:
                raise IndexError()
            objects = storage.all()
            key = my_list[0] + '.' + my_list[1]
            if key not in objects:
                raise KeyError()
            if len(my_list) < 3:
                raise AttributeError()
            if len(my_list) < 4:
                raise ValueError()
            v = objects[key]
            try:
                v.__dict__[my_list[2]] = eval(my_list[3])
            except Exception:
                v.__dict__[my_list[2]] = my_list[3]
                v.save()

        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
        except AttributeError:
            print("** attribute name missing **")
        except ValueError:
            print("** value missing **")

    def count(self, arg):
        """
        A method to count the number of instances of a class
        """
        counter = 0
        try:
            my_list = split(arg, " ")
            if my_list[0] not in HBNBCommand.__valid_classes:
                raise NameError()
            objects = storage.all()
            for key in objects:
                name = key.split('.')
                if name[0] == my_list[0]:
                    counter += 1
            print(counter)
        except NameError:
            print("** class doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
