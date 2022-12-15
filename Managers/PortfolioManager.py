import math
import numpy as np
import pandas as pd
from Portfolio import Portfolio as pf

    #Effective Data Structure Format of model dictionary
    # {
    #     Model1_ID: {
    #         Position1_ID: position_object
    #         .
    #         .
    #         .
    #         PositionN_ID: position_object
    #     },
    #     .
    #     .
    #     .
    #     ModelN_ID: {
    #         Position1_ID: position_object
    #         .
    #         .
    #         .
    #         PositionN_ID: position_object
    #     },

    # }

    #The idea is, the portfolio object contains another portfolio

class PortfolioManager:
    
    def __init__(self):
        self.model_dictionary = {}
        self.cash = 0
        self.cas = 0 #Current Account Size
        self.n_rebal_day = 0
        self.rebal_period = 30
        
    #setup and output
    def dataRequest(self):
        pass

    def loggingOutput(self):
        pass

    def max_training_period(self):
        pass

    #functions
    def initializePortfolio(self,*, list_of_models: list, current_account_size):
        self.cas = current_account_size


    def time_update(self):
        pass
    
    def rebalance(self):
        pass

    def cashManager(self):
        pass

    def leverageManager(self):
        """ 
        Functions: Uses the leverage function of the model object
        """
        pass

    def update(self):
        """
        Functions:
            1. Checks for exits - interface with BackTester and creates new position object, update exits list
            2. Checks for entries - interface with BackTester and creates new position object, update entries list
            3. Updates the data of each position based on data
            4. Updates the model_dictionary
        """

if __name__ == "__main__":
    pass