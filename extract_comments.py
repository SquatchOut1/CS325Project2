

############################
# Alex Wernex              #
# Cs325 Project 1          #
############################

from bs4 import BeautifulSoup
import argparse


parser = argparse.ArgumentParser()
parser.add_argument(help="File to ectract from", dest="fileName", type=str)

arg = parser.parse_args()
fileName = arg.fileName

file = open(fileName)

html = BeautifulSoup(file, 'html.parser')

print(html)