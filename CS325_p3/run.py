
#####################################################################################
# Alex Wernex (and Zach Linscott for Proj 4)                                        #
# Cs325 Project 3                                                                   #
# run.py                                                                            #
# This is the driver for the project.                                               #
# It runs in the terminal with the url                                              #
# to process as an argument.                                                        #
# First, it takes the names of the files you set                                    #
# and creates the paths to the correct folders on your system.                      #
# Then, it takes the URL from arg and passes to the three modules                   #
# to save the post as a raw HTML file, extract the comments as                      #
# data, and finally, saves those comments to a file.                                #
#####################################################################################




import os
import argparse
from module_1.HTMLDownload import save_raw_file
from module_2.extract_comments import extract_comments
from module_3.write_comments import *
from module_4.comment_polarity import comment_sentiment


rawFileName = 'HTMLOutput.txt'
processedFileName = 'comments.txt'

absolute_path = os.path.dirname(__file__)
relative_raw_path = "Data/raw/" + rawFileName
relative_processed_path = "Data/processed/" + processedFileName
rawFileName = os.path.join(absolute_path, relative_raw_path)
processedFileName = os.path.join(absolute_path, relative_processed_path)

parser = argparse.ArgumentParser()
parser.add_argument(help="URL to download", dest="url", type=str)

arg = parser.parse_args()
url = arg.url

print("Running...")

save_raw_file(url, rawFileName)
print("HTML raw file saved!")
comments = extract_comments(rawFileName)
print("Comments extracted!")
output_comments(comments, processedFileName)
print("Comments saved to file!")

# grab processed/cleaned comments from comments.txt
comment_lst: [] = extract_cleaned_comments(processedFileName)

# analyze comment sentiments individually and store them in a list
sentiments = [comment_sentiment(comment) for comment in comment_lst]

# fist argument is the file name
sentiments_file_write('sentiments', comment_lst, sentiments)


