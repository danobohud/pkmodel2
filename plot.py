# The script uses the solutions generated from the solver to generate plots to view the data
# Plots results for different models in seperate compartments

from matplotlib import pyplot as plt
import pandas as pd
import json

with open('./param.json', 'r') as JSON:
    input_dict = json.load(JSON)
print(input_dict)
compartments = ['Sub', 'Main']
for i in input_dict['compartments']:
    if i[2] not in ['Sub', 'Main']:
        compartments.append(i[2])

models = input_dict['model_type']
print(models)

def process_data(csv): #Input must include compartments list 
    """This function takes a csv file and creates a labelled panda dataframe"""
    df = pd.read_csv(csv, header=None)
    column_count = len(df.columns)
    colnames = ['Time']
    colnames.extend(compartments)  
    df.columns = colnames
    return df

# def plot_model():
fig, axs = plt.subplots(len(compartments), 1)
for i in range(len(models)):
    #Define which model csv you want --> timestamp?
    if len(models) > 1:
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
#     fig.savefig()

