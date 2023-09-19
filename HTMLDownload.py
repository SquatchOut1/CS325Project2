

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

print(url)

urllib.request.urlretrieve('https://www.reddit.com/r/mtg/comments/16msc6b/finished_a_game_at_130000_and_still_won_it/', "test.txt")