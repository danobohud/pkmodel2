# The script uses the solutions generated from the solver to generate plots to view the data
# Plots results for different models in seperate compartments

from matplotlib import pyplot as plt
import pandas as pd

class Visualiser:
    def __init__(self, JSON_input):
        self.input_dict = read_JSON #Fill this in 
        self.compartments = ['Sub', 'Main']
        for i in self.input_dict['compartments']:
            if i[2] not in ['Sub', 'Main']:
                self.compartments.append(i[2])
        self.models = self.input_dict['model_type']
        ##How do we identify each data creation point??

    def process_data(self, csv): #Input must include compartments list 
        """This function takes a csv file and creates a labelled panda dataframe"""
        df = pd.read_csv(csv, header=None)
        column_count = len(df.columns)
        colnames = ['Time']
        colnames.extend(self.compartments)  
        df.columns = colnames
        return df

    def plot_model(self):
        fig, axs = plt.subplots(len(compartments), 1)
        for i in range(len(self.models)):
            #Define which model csv you want --> timestamp?
            model = self.models[i]
            df = process_data('./test_data_{}.csv'.format(model)) #csv path needs to be defined before
            for j in range(len(self.compartments)):
                compartment = self.compartments[j]
                axs[j].plot(df['Time'].tolist(), df['{}'.format(compartment)].tolist())
                axs[j].set_title("{} Compartment".format(compartment))
        plt.legend(self.models)
        plt.tight_layout()
        plt.show()
        # fig.savefig()

