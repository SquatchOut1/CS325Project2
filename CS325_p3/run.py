#####################################################################################
# Alex Wernex and Zach Linscott for Proj 4                                          #
# Cs325 Project 4                                                                   #
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
from module_1.arg_parsing import arg_grabber
from module_1.HTMLDownload import save_raw_file
from module_2.extract_comments import *
from module_3.file_reading_writing import *
from module_4.comment_polarity import comment_sentiment
from module_4.sentiment_graphing import *


# points to file in need of reading
file_arg = arg_grabber()
with open(file_arg) as file:
    urls = [url.rstrip() for url in file]

print("Running...")
absolute_path = os.path.dirname(__file__)

# # make matplotlib interactive, stops terminal from hanging
# plt.interactive(True)

counter = 1
for url in urls:

    # file naming for each url
    rawFileName = 'HTMLOutput' + str(counter) + '.txt'
    relative_raw_path = "Data/raw/" + rawFileName
    rawFileName = os.path.join(absolute_path, relative_raw_path)
    processedFileName = 'comments' + str(counter) + '.txt'
    relative_processed_path = "Data/processed/" + processedFileName
    processedFileName = os.path.join(absolute_path, relative_processed_path)
    sentimentFileName = 'sentiments' + str(counter) + '.txt'
    relative_sentiment_path = "Data/sentiments/" + sentimentFileName
    sentimentFileName = os.path.join(absolute_path, relative_sentiment_path)

    # save the raw data to a file
    save_raw_file(url, rawFileName)
    print("HTML raw data saved to file {}!".format(rawFileName))

    # extract cleaned comments from raw data
    comments = extract_comments(rawFileName)
    print("Comments extracted!")

    # save the comments to a file
    output_comments(comments, processedFileName)
    print("Comments saved to file {}!".format(processedFileName))

    # grab processed/cleaned comments from comments.txt
    comment_lst: [] = extract_file_lines(processedFileName)

    # analyze comment sentiments individually and store them in a list
    print("Analyzing the sentiment of each comment...")
    sentiments = [comment_sentiment(comment) for comment in comment_lst]

    # fist argument is the file name
    print("Comments and the sentiment of each comment saved in CSV format in {}!".format(sentimentFileName))
    sentiments_file_write(sentimentFileName, comment_lst, sentiments)

    # read sentiment file and convert to df
    # would be faster to just read from the sentiments list but whatever.
    sentiments_df = csv_to_df(sentimentFileName, n_lines := 50)
    plot_sentiments(sentiments_df, sentimentFileName, fig_num=counter)
    counter += 1

plt.show()
print("Done!")

