#!/usr/bin/python3
"""
Contains the entry point of the command interpreter
"""


import cmd
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    This class represents the command interpreter for the HBNB application.
    """
    prompt = "(hbnb) "
    valid_classes = [
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review",
    ]
    def do_quit(self, arg) -> bool:
        """
        This method is used to handle the 'quit' command in the
        HBNB application.
        """
        return True

    def do_EOF(self, arg) -> bool:
        """
        This method is used to handle the 'quit' command in the
        HBNB application.
        """
        return True

    def emptyline(self) -> None:
        """Do nothing on an empty line"""
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file),
        and prints the id.
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            new_obj = eval(arg)()
            new_obj.save()
            print(new_obj.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based
        on the class name and id.
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + '.' + args[1]
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an intance based on the class name and id (save the change
        into the JSON file)
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + '.' + args[1]
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the
        class name
        """
        if not arg:
            print([str(instance) for instance in storage.all().values()])
            return
        elif arg not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return
        print(
                [
                str(instance) for key, instance in storage.all().items()
                if key.split('.')[0] == arg
            ]
        )

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + '.' + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = storage.all()[key]
        setattr(obj, args[2], args[3].strip('"'))
        obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()