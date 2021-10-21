# The script uses the solutions generated from the solver to generate plots to view the data
# Plots results for different models in seperate compartments

from matplotlib import pyplot as plt
import pandas as pd
import json


input = [['./param_2.json', './test_data_sc.csv'], ['./param_1.json', './test_data_ib.csv']] #This is where the JSON output would go -- Working on this sti

input_json = input[0][0]
with open(input_json, 'r') as JSON:
    input_dict = json.load(JSON)
compartments = ['Sub', 'Main']
for i in input_dict['compartments']:
    if i[2] not in ['Sub', 'Main']:
        compartments.append(i[2])

def process_data(csv): #Input must include compartments list 
    """This function takes a csv file and creates a labelled panda dataframe"""
    df = pd.read_csv(csv, header=None)
    column_count = len(df.columns)
    colnames = ['Time']
    colnames.extend(compartments)  
    df.columns = colnames
    return df

# # def plot_model():
fig, axs = plt.subplots(len(compartments), 1)
for i in input:
    input_json = i[0]
    csv = i[1]
    with open(input_json, 'r') as JSON:
        input_dict = json.load(JSON)
    compartments = ['Sub', 'Main']
    for i in input_dict['compartments']:
        if i[2] not in ['Sub', 'Main']:
            compartments.append(i[2])

    models = input_dict['model_type']
    if len(input) > 1:
        model = models
    else:
        model = models[i]

    df = process_data('./test_data_{}.csv'.format(model))
    for j in range(len(compartments)):
        compartment = compartments[j]
        axs[j].plot(df['Time'].tolist(), df['{}'.format(compartment)].tolist())
        axs[j].set_title("{} Compartment".format(compartment))
plt.legend(models)
plt.tight_layout()
plt.show()
    # fig.savefig()

