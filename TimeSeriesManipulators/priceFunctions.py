import math
import talib as TA
import scipy 
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as scst

class priceFunctions:
    OPEN = 'Open'
    HIGH = 'High'
    LOW = 'Low'
    CLOSE = 'Close'
    VOLUME = 'Volume'

    def __init__(self, input_df, training_period, fill_time):

        self.training_period = training_period
        self.input_df = input_df[-training_period:]

        self.open_array = np.array(self.input_df[self.OPEN])
        self.high_array = np.array(self.input_df[self.HIGH])
        self.low_array = np.array(self.input_df[self.LOW])
        self.close_array = np.array(self.input_df[self.CLOSE])
        self.volume_array = np.array(self.input_df[self.VOLUME])
        
        self.fill_time = fill_time

        #cache
        self.typprice = []
        self.avgprice = []

    #Housekeeping
    def validation(self):
        pass

    def parameterIterator(self):
        pass

    def graphing(self, list_of_arrays: list):
        """ 
        Format of input:
        list of arrays = [[header1, array1], [header2, array2], ......]
        """

        fig, ax_tuple = plt.subplots(len(list_of_arrays), 1)

        for index, ax in enumerate(ax_tuple):
            ax.plot(list_of_arrays[index][1])
            ax.set_xlabel('Time')
            ax.set_ylabel(list_of_arrays[index][0])

        plt.show()

    #Price Transforms
    def typical_price(self):
        if self.typprice == []:
            self.typprice = TA.TYPPRICE(self.high_array, self.low_array, self.close_array)
        return self.typprice

    def avgprice(self):
        if self.avgprice == []:
            self.avgprice = TA.AVGPRICE(self.open_array, self.high_array, self.low_array, self.close_array)
        return self.avgprice

    #Trend functions
    def EMA(self, lookback, input_array = [], graphing = False):
        #Exponential Moving Average
        if input_array == []:
            input_array = self.typical_price()

        ema = TA.EMA(input_array, timeperiod = lookback)

        if graphing:
            self.graphing([
                ['EMA', ema],
                ['Price', input_array]
                ])

        return ema
    
    def SMA(self, lookback, input_array = [], graphing = False):
        #Simple Moving Average
        if input_array == []:
            input_array = self.typical_price()

        sma = TA.MA(input_array, timeperiod = lookback)

        if graphing:
            self.graphing([
                ['SMA', sma],
                ['Price', input_array]
                ])
                
        return sma

    def CCI(self, lookback, graphing = False):
        #Commodity Channel Index
        cci = TA.CCI(self.high_array, self.low_array, self.close_array, timeperiod = lookback)

        if graphing:
            self.graphing([
                ['CCI', cci],
                ['Price', self.typical_price()]
                ])
                
        return cci
        
    #Volume functions
    def OBV(self, graphing = False):
        #On Balance Volume
        obv = TA.OBV(self.close_array, self.volume_array)

        if graphing:
            self.graphing([
                ['OBV', obv],
                ['Price', self.typical_price()]
                ])
                
        return obv

    def PPO(self, fastperiod, slowperiod, graphing = False):
        #Percentage Price Oscillator
        
        PPO = TA.PPO(self.close_array, fastperiod = fastperiod, slowperiod=slowperiod, matype=0)

        if graphing:
            self.graphing([
                ['PPO', PPO],
                ['Price', self.typical_price()]
                ])
                
        return PPO
    
    #Volatility functions
    def NATR(self, lookback, graphing = False):
        #Normalized Average True Range
        natr = TA.NATR(self.high_array, self.low_array, self.close_array, timeperiod=lookback)
        if graphing:
            self.graphing([
                ['NATR', natr],
                ['Price', self.typical_price()]
                ])
        
        return natr

    def ROC(self, lookback, graphing = False):
        #Rate of change
        roc = TA.ROC(self.close_array, timeperiod=lookback)
        if graphing:
            self.graphing([
                ['ROC', roc],
                ['Price', self.typical_price()]
                ])
                
        return roc

    #Statistical functions
    def returnDistribution(self, graphing = False):
        pass
    
    def correlation_HL(self, lookback, graphing = False):
        corr = TA.CORREL(self.high_array, self.low_array, timeperiod=lookback)
        if graphing:
            self.graphing([
                ['HL_Corr', corr],
                ['Price', self.typical_price()]
                ])
                
        return corr


    def linregAngle(self, lookback, graphing = False):
        lra = TA.LINEARREG_ANGLE(self.close_array, timeperiod=lookback)
        if graphing:
            self.graphing([
                ['LinReg Angle', lra],
                ['Price', self.typical_price()]
                ])
                
        return lra

    def linregSlope(self, lookback, graphing = False):
        lrs = TA.LINEARREG_SLOPE(self.close_array, timeperiod=lookback)
        if graphing:
            self.graphing([
                ['LinReg Slope', lrs],
                ['Price', self.typical_price()]
                ])
                
        return lrs

    def stddev(self, lookback, graphing = False):
        std = TA.STDDEV(self.close_array, timeperiod=lookback, nbdev=1)
        if graphing:
            self.graphing([
                ['STD', std],
                ['Price', self.typical_price()]
                ])
                
        return std

    def variance(self, lookback, graphing = False):
        var = TA.VAR(self.close_array, timeperiod=lookback, nbdev=1)
        if graphing:
            self.graphing([
                ['VAR', var],
                ['Price', self.typical_price()]
                ])
                
        return var

    def skew(self, lookback, graphing = False):
        arr = self.typical_price()
        out = [0 for i in range(lookback)]
        for i in range(len(arr) - lookback):
            temp_arr = arr[i: i + lookback]
            skew_val = scst.skew(temp_arr)
            out.append(skew_val)
        
        if graphing:
            self.graphing([
                ['LagSkew', out],
                ['Price', self.typical_price()]
                ])
                
        return out

    def kurtosis(self, lookback, graphing = False):
        arr = self.typical_price()
        out = [0 for i in range(lookback)]
        for i in range(len(arr) - lookback):
            temp_arr = arr[i: i + lookback]
            skew_val = scst.kurtosis(temp_arr)
            out.append(skew_val)
        
        if graphing:
            self.graphing([
                ['LagSkew', out],
                ['Price', self.typical_price()]
                ])
                
        return out

if __name__ == "__main__":
    pass
