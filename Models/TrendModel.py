import math
import numpy as np
import pandas as pd

class TrendModel:
    def __init__(self):
        self.modelID = ""
        self.leverage = 0 #default leverage amount is set to 0
        pass

    def getTrainingPeriod(self):
        pass

    def leverage(self):
        """
        Functions: 
            1. Interfaces with the leverageManager function of portfolio manager
            2. Analyzes each stocks situation and gives leverage amount
        """
        return self.leverage

    def analyze(self) -> float:
        """
        Functions: Analyzes data for one security
        """
        pass

    def run(self) -> pd.DataFrame:
        """
        Functions: Use the analyze function above to get opportunity list
        """
    
    def _tests(self):
        pass

if __name__ == '__main__':
    pass