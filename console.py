#!/usr/bin/python3
'''
    Implementing the console for the HBnB project.
'''
import cmd
from models.base_model import BaseModel


class HBNDCommand(cmd.Cmd):
    '''
        Contains the entry point of the command interpreter.
    '''

    prompt = ("(hbnb) ")

    def do_quit(self, args):
        '''
            Quit command to exit the program.
        '''
        exit(0)

    def do_EOF(self, args):
        '''
            Exits after receiving the EOF signal.
        '''
        self.emptyline()
        exit(0)

    def do_create(self, args):
        '''
            Create a new instance of class BaseModel and saves it
            to the JSON file.
        '''
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            args = args.split(" ")
            new_instance = eval(args[0])()
            new_instance.save()

        except:
            print("** class doesn't exist **")

if __name__ == "__main__":
    HBNDCommand().cmdloop()
