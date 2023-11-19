import argparse
from pathlib import Path


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
