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
        """Called when an empty line is entered"""
        pass

    def precmd(self, line):
        """Hook method executed just before the command line is interpreted"""
        # Strip leading and trailing whitespaces from the command line
        return line.strip()

    def postcmd(self, stop, line):
        """Hook method executed just after a command dispatch is finished"""
        # Return False to continue command loop
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()

