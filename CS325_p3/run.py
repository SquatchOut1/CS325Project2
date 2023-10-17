import os
import argparse
from module_1.HTMLDownload import save_raw_file
from module_2.extract_comments import extract_comments
from module_3.write_comments import output_comments 


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

save_raw_file(url, rawFileName)
comments = extract_comments(rawFileName)
output_comments(comments, processedFileName)

