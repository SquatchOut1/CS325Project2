import argparse
from pathlib import Path

'''
Authors: Zachery Linscott and Alex Wernex
Class: CS 325
Purpose:
    arg_grabber(): 
        Receives is the user's command line argument,
         expecting a filepath, and returns the path.
    valid_file():
        Takes the command line arg the user inputs andensures it's a valid file path.
'''


def valid_file(arg):
    try:

        if (file := Path(arg)).is_file():
            return file
    except FileNotFoundError:
        print("{} is an invalid file path.".format(arg))


def arg_grabber() -> str:
    # establish parsing object, define the program and its use
    parser = argparse.ArgumentParser(prog='run',
                                     description='This program accepts a file argument of subreddit urls '
                                                 'and takes the comments from those url\'s '
                                                 'and places them into a .txt file.')
    parser.add_argument('filename', type=valid_file, help="Enter an appropriate file path")
    args = parser.parse_args()
    return args.filename
