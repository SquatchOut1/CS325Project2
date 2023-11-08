
#####################################################################################
# Alex Wernex (and Zach Linscott for Proj4)                                         #
# Cs325 Project 3                                                                   #
# extract_comments.py                                                               #
# This file simply takes the filepath of the raw HTML file                          #
# and outputs a list of the comments form the post. This function opens the file,   #
# parses through the file with BeautifulSoup looking for a class id associated with #
# comments. Then it excracts just the text from the post and returns it as a list.  #
#####################################################################################

from bs4 import BeautifulSoup

def extract_comments(filename):
    htmlFile = open(filename, encoding='utf8')
    output = []
    html = BeautifulSoup(htmlFile, 'html.parser')

    commentHtml = html.find_all(class_ = "entry unvoted")

    for elem in commentHtml:
        comments = elem.find_all(class_ = 'md')
        for comment in comments:
            output.append(comment.text)
    return output
