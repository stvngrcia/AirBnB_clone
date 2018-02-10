#!/usr/bin/python3
'''
    Implementing the console for the HBnB project.
'''
import cmd


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


if __name__ == "__main__":
    HBNDCommand().cmdloop()
