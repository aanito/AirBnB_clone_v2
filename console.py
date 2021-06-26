#!/usr/bin/python3
"""
Class CommandConsole for Airbnb
"""
import cmd
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.user import User
import models
import sys

allowed_class = {"BaseModel": BaseModel, "Place": Place, "State": State,
                 "City": City, "Amenity": Amenity, "Review": Review,
                 "User": User}

class HBNBCommand(cmd.Cmd):
    """
    HBNB Class
    """
    prompt = '(hbnb)'
    __all_117 = 0

    def do_quit(self, line):
        """quit command: exit the program"""
        return True

    def do_EOF(self, line):
        """End of File command: exit the program"""
        return True

    def emptyline(self):
        """overridden to not do nothing"""
        pass

    def precmd(self, line):
        """ Edit given command to allow second type of input"""
        if not sys.stdin.isatty():
            print()
        if '.' in line:
            HBNBCommand.__all_117 = 1
            line = line.replace('.', ' ').replace('(', ' ').replace(')', ' ')
            cmd_argv = line.split()
            cmd_argv[0], cmd_argv[1] = cmd_argv[1], cmd_argv[0]
            line = " ".join(cmd_argv)
        return cmd.Cmd.precmd(self, line)

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id"""
        string = line + "()"
        if len(line) == 0:
            print("** class name missing **")
            return
        try:
            instance = eval(string)
            print(instance.id)
            instance.save()
        except:
            print("** class doesn't exist **")

        """
        if len(line) == 0:
            print("** class name missing **")
            return
        elif line in allowed_class.keys():
            instance =  allowed_class[line]()
        elif line not in allowed_class.keys():
            print("** class doesn't exist **")
            return

        print(instance.id)
        instance.save() 
        """

    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id.
            Ex: $ show BaseModel 1234-1234-1234."""
        cmd_line = line.split()
        if len(cmd_line) == 0:
            print("** class name missing **")
            return
        elif cmd_line[0] not in allowed_class.keys():
            print("** class doesn't exist **")
        elif len(cmd_line) == 1:
            print("** instance id missing **")
        elif len(cmd_line) == 2:
            instance = cmd_line[0] + "." + cmd_line[1]
            if instance in models.storage.all():
                print(models.storage.all()[instance])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234"""
        cmd_line = line.split()
        if len(cmd_line) == 0:
            print("** class name missing **")
            return
        elif cmd_line[0] not in allowed_class.keys():
            print("** class doesn't exist **")
        elif len(cmd_line) == 1:
            print("** instance id missing **")
        elif len(cmd_line) == 2:
            instance = cmd_line[0] + "." + cmd_line[1]
            if instance in models.storage.all():
                del models.storage.all()[instance]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances based or not on the class name.
            Ex: $ all BaseModel or $ all."""
        cmd_line = line.split()
        if cmd_line[0] not in allowed_class.keys():
            print("** class doesn't exist **")
        else:
            # instance = cmd_line[0] + "." + cmd_line[1]
            # if instance in models.storage.all():
            if len(cmd_line) > 1:
                instance = cmd_line[0] + "." + cmd_line[1]
                if instance in models.storage.all():
                    print('["', end="")
                    print(models.storage.all()[instance], end="")
                    print('"]')
            else:
                print('["', end="")
                print(models.storage.all(), end="")
                print('"]')

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or updating attribute
            (save the change into the JSON file).
            - Usage: update <class name> <id> <attribute name> "<attribute value>"
            - Ex: $ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"
            - Only one attribute can be updated at the time"""
        cmd_line = line.split()
        if len(cmd_line[0]) == 0:
            print("** class name missing **")
        elif cmd_line[0] not in allowed_class.keys():
            print("** class doesn't exist **")
        elif len(cmd_line[1]) == 0:
            print("** instance id missing **")
        else:
            instance = cmd_line[0] + "." + cmd_line[1]
            if instance not in models.storage.all():
                print("** no instance found **")
            elif len(cmd_line[2]) == 0:
                print("** attribute name missing **")
            elif len(cmd_line[3]) == 0:
                print("** value missing **")
            else:
                select_obj = models.storage.all().get(instance)
                setattr(select_obj, cmd_line[2], cmd_line[3][1:-1])
                select_obj.save()

    def default(self, line):
        """overriden a command when the command doesn't exist"""
        my_list = line.split('.(,)')
        if len(my_list) >= 2:
            if my_list[1] == "all()":
                self.do_all(my_list[0])
            elif my_list[1] == "count()":
                self.count(my_list[0])

    def do_count(self, line):
        "count instances of the class"

        cmd_line = line.split()

        if cmd_line[0] not in allowed_class:
            return
        else:
            counter = 0
            keys_list = models.storage.all().keys()
            for search in keys_list:
                len_search = len(cmd_line[0])
                if search[:len_search] == cmd_line[0]:
                    counter += 1
                    # print(search)
            print(counter)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
