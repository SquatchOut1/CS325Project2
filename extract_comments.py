

############################
# Alex Wernex              #
# Cs325 Project 1          #
############################

from bs4 import BeautifulSoup
import argparse

outputFilePath = "C:\\Users\\alexw\\Documents\\School\\cs325\\CS325Project2\\comments.txt"
output = []
outputFile = open(outputFilePath, "w", encoding="utf8")
pageBreak = f"\n {'-'*200} \n \n"

parser = argparse.ArgumentParser()
parser.add_argument(help="File to ectract from", dest="fileName", type=str)

arg = parser.parse_args()
fileName = arg.fileName

htmlFile = open(fileName, encoding='utf8')

html = BeautifulSoup(htmlFile, 'html.parser')

commentHtml = html.find_all(class_ = "entry unvoted")

for elem in commentHtml:
    comments = elem.find_all(class_ = 'md')
    for comment in comments:
        output.append(comment.text)
for line in output:
    outputFile.write(line)
    outputFile.write(pageBreak)
outputFile.close()
htmlFile.close()