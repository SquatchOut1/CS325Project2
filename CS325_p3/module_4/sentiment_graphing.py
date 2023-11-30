import pandas as pd

def graph_analysis(file_name: str):
    print(pd.read_csv(file_name, sep='\t', header=None, names=['title',]))
