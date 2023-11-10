
#####################################################################################
# Alex Wernex (and Zach Linscott for Proj4)                                         #
# Cs325 Project 3                                                                   #
# write_comments.py                                                                 #
# This file simply takes a list of the comments and the filepath of the output file #
# and outputs said file. This function opens the file, then goes throught the list  #
# comment by comment. It then alternates writting the comment and a line separator  #
# to the file.                                                                      #
#                                                                                   #
# Added by Zach:                                                                    #
# extract_cleaned_comments(): simply reads the comments from a file and puts them   #
# in a list.                                                                        #
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


# reads  the processed comments from comments.txt and returns them in a list
def extract_cleaned_comments(file_name: str) -> []:
    with open(file_name, 'r', encoding='utf-8') as f:
        lst = [line.strip() for line in f]

    return lst


# writes the comment and sentiment of the comment to a new file.
def sentiments_file_write(file_name: str, comments: [], comment_sentiments: []):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(len(comments)):
            comments[i] = comments[i].replace(",", "")
            f.write("{},".format(comments[i]) +
                    "{}\n".format(comment_sentiments[i]))
