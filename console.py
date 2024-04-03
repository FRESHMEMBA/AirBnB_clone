#!/usr/bin/python3
"""
Contains the entry point of the command interpreter
"""


import cmd


class HBNBCommand(cmd.Cmd):
    """
    This class represents the command interpreter for the HBNB application.
    """
    prompt = "(hbnb) "

    def do_quit(self, arg) -> bool:
        """
        This method is used to handle the 'quit' command in the
        HBNB application.
            
        Parameters:
            arg (str): The argument passed with the 'quit' command.
                
        Returns:
            bool: True, indicating that the command has been
            successfully executed.
        """
        return True

    def do_EOF(self, arg) -> bool:
        """
        This method is used to handle the 'quit' command in the
        HBNB application.
            
        Parameters:
            arg (str): The argument passed with the 'quit' command.
                
        Returns:
            bool: True, indicating that the command has been
            successfully executed.
        """
        return True

    def emptyline(self) -> None:
        """Do nothing on an empty line"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()