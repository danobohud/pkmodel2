# The script uses the solutions generated from the solver to generate plots to view the data
# Plots results for different models in seperate compartments

import numpy as np
from matplotlib import pyplot as pl
import pandas as pd


def process_data(csv): 
    """This function takes a csv file and creates a labelled panda dataframe"""
    df = pd.read_csv('./{}'.format(csv), header=None)
    column_count = len(df.columns)
    colnames = ['Time','Sub','Main']
    for i in range(column_count - 3):
        colnames.append('Peripheral_{}'.format(i))
    df.columns = colnames
    return df

for i in compartments:
    compartment_data = []
    for i in range(len(models)):
        model i = process_data(csv)
    
    plt.show()
    




