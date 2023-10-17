
#####################################################################################
# Alex Wernex                                                                       #
# Cs325 Project 3                                                                   #
# write_comments.py                                                                 #
# This file simply takes a list of the comments and the filepath of the output file #
# and outputs said file. This function opens the file, then goes throught the list  #
# comment by comment. It then alternates writting the comment and a line separator  #
# to the file.                                                                      #
#####################################################################################

def output_comments(data, toFile):
    pageBreak = f"\n {'-'*200} \n \n"
    outputFile = open(toFile, "w", encoding="utf8")

    for line in data:
        outputFile.write(line)
        outputFile.write(pageBreak)
    outputFile.close()

