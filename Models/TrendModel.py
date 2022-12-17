import math
import numpy as np
import pandas as pd
from TimeSeriesManipulators.priceFunctions import priceFunctions
from Managers.constantsManager import Names
from statistics import mean

class MediumTrendModel:
    def __init__(self):
        self.modelID = "MediumTrend"
        self.leverage = 0 #default leverage amount is set to 0
        self.training_period = self.getTrainingPeriod()
        self.fill_time = 'Open'

    def getTrainingPeriod(self):
        return 200

    def leverage(self):
        """
        Functions: 
            1. Interfaces with the leverageManager function of portfolio manager
            2. Analyzes each stocks situation and gives leverage amount
        """
        return self.leverage

    def test(self, input_dict):

        for ticker, data in input_dict.items():
            pfObj = priceFunctions(data, self.getTrainingPeriod(), fill_time = Names.CLOSE)
            averageSkew = mean(pfObj.skew(20))
            averageKurtosis = mean(pfObj.kurtosis(20))
            averageSgn = mean(pfObj.EMAsgn(40))
            print(ticker, averageSgn, averageSkew, averageKurtosis)

    def analyze(self, input_df) -> float:
        """
        Functions: Analyzes data for one security
        """


    def run(self) -> pd.DataFrame:
        """
        Functions: Use the analyze function above to get opportunity list
        """
    
    def _tests(self):
        pass

if __name__ == '__main__':
    pass