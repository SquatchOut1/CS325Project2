

############################
# Alex Wernex              #
# Cs325 Project 1          #
############################

import argparse
import urllib.request

filepath = "C:/Users/alexw/Documents/School/cs325/CS325Project1/HTMLOutput.txt"


parser = argparse.ArgumentParser()
parser.add_argument(help="URL to download", dest="url", type=str)

arg = parser.parse_args()
url = arg.url

urllib.request.urlretrieve(url, filepath)