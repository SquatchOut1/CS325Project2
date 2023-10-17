
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