import pandas as pd

def read_in_data(file_path):
##    data = pd.read_csv(file_path, delimiter='\t', quoting=3, header=0)
    data = pd.read_csv(file_path, delimiter='\t')

    return data
