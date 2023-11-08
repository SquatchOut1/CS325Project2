
#####################################################################################
# Alex Wernex (and Zach Linscott for Proj4)                                         #
# Cs325 Project 3                                                                   #
# write_comments.py                                                                 #
# This file simply takes a list of the comments and the filepath of the output file #
# and outputs said file. This function opens the file, then goes throught the list  #
# comment by comment. It then alternates writting the comment and a line separator  #
# to the file.                                                                      #
#####################################################################################

def output_comments(data, toFile):
    # pageBreak = f"\n"
    outputFile = open(toFile, "w", encoding="utf8")
    counter = 0
    for line in data:
        outputFile.write(line)
        # outputFile.write(pageBreak)
        counter += 1
        if counter == 50:
            break
    outputFile.close()

