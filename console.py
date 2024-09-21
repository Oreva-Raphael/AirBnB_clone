#!/usr/bin/python3
"""Model for instantiating the console"""

import cmd

class HBNBCommand(cmd.Cmd):
    """command line console"""
    prompt = "(hbnb)"

    def do_quit(self, line):
        """Quit to exit the program"""
        return True

    def do_EOF(self, line):
        """Implement the end of line fundtion\n"""
        return True

    def help_quit(self):
        """Provide helpful doc on quit command"""
        print("quit: Quit the program just like exit")

    def help_exit(self):
        print("exit: exit the program, just like quit")

    def emptyline(self):
        """called when an empty line is entered as an argument"""
        pass

    do_exit = do_quit

if __name__ == '__main__':
    HBNBCommand().cmdloop()