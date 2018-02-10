#!/usr/bin/python3
'''
    Implementing the console for the HBnB project.
'''
import cmd
import json
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
        if len(args) == 1:
            print("** class name missing **")
            return
        if len(args) == 2:
            print("** instance id missing **")
            return
        storage = FileStorage()
        storage.reload()
        obj_dict = storage.all()
        st_obj_dict = str(obj_dict)
        if args[0] not in st_obj_dict:
            print("** class doesn't exist **")
            return
        key = args[0] + "." + args[1]
        key = args[0] + "." + args[1]
        try:
            value = obj_dict[key]
            print(value)
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, args):
        '''
            Deletes an instance based on the class name and id.
        '''
        args = args.split(" ")
        if len(args) == 1 and len(args[0]) == 0 :
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        class_name = args[0]
        class_id = args[1]
        storage = FileStorage()
        storage.reload()
        obj_dict = storage.all()
        st_obj_dict = str(obj_dict)
        if class_name not in st_obj_dict:
            print("** class doesn't exist **")
            return

        key = class_name + "." + class_id
        try:
            del obj_dict[key]
        except KeyError:
            print("** no instance found **")
        storage.save()


if __name__ == "__main__":
    HBNDCommand().cmdloop()
