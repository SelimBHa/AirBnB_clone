#!/usr/bin/env python3
"""
This module contains the console.py module
"""

import cmd
import os
import re
import sys
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBConsole(cmd.Cmd):
    """Command-line interpreter class"""

    prompt = "(hbnb) "
    AVAILABLE_CLASSES = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Place": Place,
        "Amenity": Amenity,
        "Review": Review
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def default(self, arg):
        """Default method"""
        func_map = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update,
            "create": self.do_create,
            "clear": self.do_clear
        }

        tokens = re.findall(r'\w+', arg)
        command, *args = tokens
        if command in func_map:
            func_map[command](' '.join(args))
        else:
            print("*** Unknown command: {}".format(arg))

    def do_create(self, arg):
        """Creates a new instance of a class"""
        if not arg:
            print("** Class name missing **")
            return

        class_name = arg.split()[0]
        if class_name not in self.AVAILABLE_CLASSES:
            print("** Class doesn't exist **")
            return

        new_instance = self.AVAILABLE_CLASSES[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_clear(self, arg):
        """Clears the screen"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def do_show(self, arg):
        """Displays the string representation of an instance"""
        if not arg:
            print("** Class name missing **")
            return

        tokens = arg.split()
        if tokens[0] not in self.AVAILABLE_CLASSES:
            print("** Class doesn't exist **")
            return
        if len(tokens) < 2:
            print("** Instance id missing **")
            return

        obj_key = "{}.{}".format(tokens[0], tokens[1])
        obj = storage.all().get(obj_key)
        if not obj:
            print("** No instance found **")
        else:
            print(obj)

    # Other methods remain unchanged...

if __name__ == '__main__':
    HBNBConsole().cmdloop()

