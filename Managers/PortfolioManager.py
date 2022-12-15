import math
import numpy as np
import pandas as pd

class PortfolioManager:
    
    def __init__(self):
        self.model_dictionary = {}
        self.cash = 0
        self.current_account_size = 0
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
    def time_update(self):
        pass
    
    def rebalance(self):
        pass

    def cashManager(self):
        pass