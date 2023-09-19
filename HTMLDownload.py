

############################
# Alex Wernex              #
# Cs325 Project 1          #
############################

import argparse
import urllib.request



parser = argparse.ArgumentParser()
parser.add_argument(help="URL to download", dest="url", type=str)

arg = parser.parse_args()
url = arg.url

urllib.request.urlretrieve(url, "HTMLOutput.txt")