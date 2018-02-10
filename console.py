#!/usr/bin/python3
'''
    Implementing the console for the HBnB project.
'''
import cmd
from models.engine.file_storage import FileStorage
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
            print(new_instance.id)

        except:
            print("** class doesn't exist **")

    def do_show(self, args):
        '''
            Print the string representation of an instance baed on
            the class name and id given as args.
        '''
        args = args.split(" ")
        storage = FileStorage()
        storage.reload()
        obj_dict = storage.all()
        key = args[0] + "." + args[1]
        value = obj_dict[key]
        print(value)

if __name__ == "__main__":
    HBNDCommand().cmdloop()
