#!/usr/bin/python3
"""The command interpreter for the Back-End"""

import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Class for the command interpreter"""
    prompt = "(hbnb) "
    allowed_obj = ["BaseModel",
                   "User",
                   "Amenity",
                   "City",
                   "Place",
                   "Review",
                   "State"]

    def do_quit(self, args):
        """Quit command to exit the program\n"""
        raise SystemExit

    def do_EOF(self, args):
        """Handles end of file"""
        return True

    def do_help(self, args):
        """help"""
        cmd.Cmd.do_help(self, args)

    def do_create(self, args):
        """Usage: create <class> <key 1>=<value 2> <key 2>=<value 2> ...
        Create a new class instance with given keys/values and print id."""
        my_list = args.split()
        if not my_list:
            print("** class name missing **")
        elif my_list[0] not in HBNBCommand.allowed_obj:
            print("** class doesn't exist **")
        else:
            new_instance = eval(my_list[0])()
            for item in my_list[1:]:
                key, value = item.split('=')
                setattr(new_instance, key, value.replace('_', ' '))
            new_instance.save()
            print(new_instance.id)

    def do_show(self, args):
        """Prints the string representation of an instance
        based on the class name and id"""
        list_str = args.split()
        if not list_str:
            print("** class name missing **")
        elif list_str[0] not in HBNBCommand.allowed_obj:
            print("** class doesn't exist **")
        elif len(list_str) == 1:
            print("** instance id missing **")
        else:
            objects = storage.all()
            instance = list_str[0] + '.' + list_str[1]
            if instance in objects:
                print(objects[instance])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and
        id (save the change into the JSON file)"""
        list_str = args.split()
        if not list_str:
            print("** class name missing **")
        elif list_str[0] not in HBNBCommand.allowed_obj:
            print("** class doesn't exist **")
        elif len(list_str) == 1:
            print("** instance id missing **")
        else:
            objects = storage.all()
            instance = list_str[0] + '.' + list_str[1]
            if instance in objects:
                del objects[instance]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all instances
        based or not on the class name"""
        list_str = args.split()
        if not args or list_str[0] in HBNBCommand.allowed_obj:
            objects = storage.all()
            class_name = list_str[0] if list_str else None
            instances = [str(obj) for obj in objects.values()
                         if not class_name or
                         obj.__class__.__name__ == class_name]
            print(instances)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)"""
        list_str = args.split()
        if not list_str:
            print("** class name missing **")
        elif list_str[0] not in HBNBCommand.allowed_obj:
            print("** class doesn't exist **")
        elif len(list_str) == 1:
            print("** instance id missing **")
        elif len(list_str) == 2:
            print("** attribute name missing **")
        elif len(list_str) == 3:
            print("** value missing **")
        else:
            objects = storage.all()
            instance = "{}.{}".format(list_str[0], list_str[1])
            if instance in objects:
                obj = objects[instance]
                setattr(obj, list_str[2], list_str[3].replace('_', ' '))
                obj.save()
            else:
                print("** no instance found **")

    def emptyline(self):
        '''empty line
        '''
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
