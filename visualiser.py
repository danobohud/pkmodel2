import numpy as np 
import matplotlib.pyplot as plt
import csv
import json

"""
JSON Format

return {
        'model_type': model_type,
        'compound': compound,
        'dose':dose,
        'len_assay':len_assay,
        'len_interval':len_interval,
        'clearance':clearance,
        'compartments':compartments,
        'vis':vis
        }
"""

# Load single JSON file and return data for plotting
def single_plot_data(json_file, csv_file):
    '''
    read parameters and data from models to generate a list
    list structure is [parameters, data_array, num_rows, num_columns]
    '''
    # Empty list to be returned
    plot_values = []
    # Open JSON file
    file = open(json_file)
    # Return JSON file as dictionary
    param_dict = json.load(file)
    plot_values[0] = param_dict
    # Open the file in 'r' mode, not 'rb'
    csv = open(csv_file)
    # Create array from data with columns as data lists (e.g. time first column)
    data_array = np.loadtxt(csv, delimiter=",")
    plot_values[1] = data_array
    # Obtain number of columns
    num_rows, num_cols = data_array.shape
    plot_values[2] = num_rows
    plot_values[3] = num_columns
    
    return plot_values

# Run is list formatted as [[json1, csv1], [json2, csv2]...] 
def collate_data(run):
    '''
    collate the lists returned by single_plot to return a list of lists for all simulations in a run
    '''
    # Create collated list
    collated_list = []
    # Append data from each simulation
    for i in run:
        collated_list.append(single_plot(i[0], i[1]))
    return collated_list

# Plot data from collated data structure
def multiplot(collated_list):
    '''
    plot overlayed simulation data from multiple runs
    '''
    # Iterate over simulations to obtain maximum compartment number
    comp_list = []
    for i in collated_list:
        comp_list.append(i[4])

    compartments = max(comp_list)

    # Set up sub plot 
    fig, axs = plt.subplots(1, compartments - 1)

    # Iterate over simulation data
    for j in range(compartments):
        for i in collated_list:
            axs[j].plot(collated_list[0][1][:,0],collated_list[i][1][:,j+1])
            axs[j].set_title(str(collated_list[0][j]))

    tight.plt()
    plt.show()
