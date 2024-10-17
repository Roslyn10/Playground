#!/usr/bin/python3

import cmd

import Cmd


class MyCmd(cmd.Cmd):
    prompt = '(hbnb '  # Set the prompt for the command line

    def do_hello(self, line):
        """Say hello"""
        print("Hello!")

    def do_nothing(self, line):
        """Does nothing"""
        print("/n")

    def do_quit(self, line):
        """Exit the program"""
        return True

if __name__ == "__main__":
    MyCmd().cmdloop()  # Start the command loop
