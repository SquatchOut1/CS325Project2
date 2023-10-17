

def output_comments(data, toFile):
    pageBreak = f"\n {'-'*200} \n \n"
    outputFile = open(toFile, "w", encoding="utf8")

    for line in data:
        outputFile.write(line)
        outputFile.write(pageBreak)
    outputFile.close()

