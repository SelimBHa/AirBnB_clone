#!/usr/bin/env python3
"""
This module contains the console.py module
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Command-line interpreter class"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Handles EOF"""
        print()  # Print newline
        return True

    def emptyline(self):
        """This doesn't do anything when no command is passed"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

