import numpy as np 
import matplotlib.pyplot as plt
import csv
# import the dictionary
# import the data file(s)

model = str('both')

# Single model to be visualised
if model != 'both': 
    # Open the file in 'r' mode, not 'rb'
    csvFile = open('test_data.csv')
    # Create array from data with columns as data lists (e.g. time first column)
    dataArray = np.loadtxt(csvFile, delimiter=",")
    # Obtain number of columns
    num_rows, num_cols = dataArray.shape

    # Set up sub plot 
    fig, axs = plt.subplots(1, num_cols - 1)
    # Plot time - sub data
    axs[0,].plot(dataArray[:,0], dataArray[:,1])
    axs[0].set_title('Sub Compartment Plot')
    # Plot time - main data 
    axs[1].plot(dataArray[:,0], dataArray[:,2])
    axs[1].set_title('Main Compartment Plot')
    # Iterate over remaining columns to  plot time - peripheral compartment data
    for i in range(2,num_cols - 1): 
        axs[i].plot(dataArray[:,0], dataArray[:,i])
        axs[i].set_title('Subcompartment ' + str(i) + ' Plot')

    plt.show()


# Two models to be overlayed
else: 
    # Open the files in 'r' mode, not 'rb'
    csvFile1 = open('test_data.csv')
    csvFile2 = open('test_data2.csv')
    # Create array from data with columns as data lists (e.g. time first column)
    dataArray1 = np.loadtxt(csvFile1, delimiter=",")
    dataArray2 = np.loadtxt(csvFile2, delimiter=",")
    # Obtain number of columns
    num_rows1, num_cols1 = dataArray1.shape
    num_rows2, num_cols2 = dataArray2.shape

     
    fig, axs = plt.subplots(1, num_cols1 - 1)
    # Plot time - sub data
    axs[0].plot(dataArray1[:,0], dataArray1[:,1])
    axs[0].plot(dataArray1[:,0], dataArray2[:,1])
    axs[0].set_title('Sub Compartment Plot')
    # Plot time - main data 
    axs[1].plot(dataArray1[:,0], dataArray1[:,2])
    axs[1].plot(dataArray1[:,0], dataArray2[:,2])
    axs[1].set_title('Main Compartment Plot')
    # Iterate over remaining columns to  plot peripheral compartment data
    for i in range(2,num_cols1 - 1): 
        axs[i].plot(dataArray1[:,0], dataArray1[:,i])
        axs[i].plot(dataArray1[:,0], dataArray2[:,i])
        axs[i].set_title('Subcompartment ' + str(i) + ' Plot')

    plt.show()






