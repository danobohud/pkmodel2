# The script uses the solutions generated from the solver to generate plots to view the data
# Plots results for different models in seperate compartments
# To implement the script use plot_model(input) where input is a list of lists in the following form:
# input = [['./param_2.json', './test_data_sc.csv'], ['./param_1.json', './test_data_ib.csv']]

from matplotlib import pyplot as plt
import pandas as pd
import json

input = [['./param_2.json', './test_data_sc.csv'], ['./param_1.json', './test_data_ib.csv']] #This is where the JSON output would go -- Working on this sti

def json_file_to_dictionary(json_file):
    with open(json_file, 'r') as JSON:
        input_dict = json.load(JSON)
    return input_dict

def csv_file_to_panda_data_frame(csv_file): #Input must include compartments list 
    """This function takes a csv file and creates a labelled panda dataframe"""
    df = pd.read_csv(csv_file, header=None)
    # column_count = len(df.columns)
    colnames = ['Time']
    colnames.extend(define_compartment_names(input))  
    df.columns = colnames
    return df

def define_compartment_names(input):
    '''
    This function reads the first JSON file in the 'list of lists' and returns 
    the number of compartments that there will be in this comparison.
    '''
    json_file = input[0][0]
    with open(json_file, 'r') as JSON:
        input_dict = json.load(JSON)
    compartments = ['Sub', 'Main']
    for i in input_dict['compartments']:
        if i[2] not in ['Sub', 'Main']:
            compartments.append(i[2])
    return compartments

def define_model_names(input):
    models = []
    for i in input:
        models.append(json_file_to_dictionary(i[0])['model_type']) #Is there a better way to differentiate models (type and also parameters)
    return models

def plot_model(input):
    compartments = define_compartment_names(input)
    models = define_model_names(input)

    fig, axs = plt.subplots(len(compartments), 1)
    for i in input:
        # json_file = i[0]
        csv_file = i[1] 

        # if len(input) == 1:
        #     model = models
        # else:
        #     model = models[i]

        df = csv_file_to_panda_data_frame(csv_file)

        for j in range(len(compartments)):
            compartment = compartments[j]
            axs[j].plot(df['Time'].tolist(), df['{}'.format(compartment)].tolist())
            axs[j].set_title("{} Compartment".format(compartment))

    plt.legend(models)
    plt.tight_layout()
    plt.show()
    # fig.savefig()

plot_model(input)

