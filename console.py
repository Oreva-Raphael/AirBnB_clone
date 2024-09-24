#!/usr/bin/python3
"""Model for instantiating the console"""

import cmd
import models
import shlex
from models.base_model import BaseModel
from models import storage

valid_classes = {'BaseModel': BaseModel}


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

    def do_create(self, arg):
        """Create a new instance of BaseModel and save it to JSON file
        usage: create <class_name>"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in valid_classes:
            print("** class doesn't exist **")
            return False
        else:
            new_instance = valid_classes[args[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """show string reperesentation of an instance
        based on the class name and id ex: show BaseModel 1234-1234-1234"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in valid_classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id
        save changes to JSON file"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        if args[0] in valid_classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Print all string representation of all instance based on
        or not on the class name"""
        args = shlex.split(arg)
        result = []
        if len(args) == 0:
            obj_items = models.storage.all()
        elif args[0] in valid_classes:
            obj_items = models.stroage.all(valid_classes[args[0]])
        else:
            print("** class doesn't exist **")
            return False
        for item in obj_items:
            result.append(str(obj_items[item]))
        print(result)

    def do_update(self, arg):
        """updates and instance based on the class name and id"""
        args = shlex.split(arg)
        args_len = len(args)
        if args_len == 0:
            return False
        if args[0] in valid_classes:
            if args_len > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    if args_len > 2:
                        if args_len > 3:
                            name = models.storage.all()[key]
                            setattr(name, args[2], args[3])
                            name.save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
