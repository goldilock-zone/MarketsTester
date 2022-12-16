import talib as TA
import numpy as np
from DataGetter.DataGetter import BasketStockData_Backtest
from TimeSeriesManipulators.priceFunctions import priceFunctions

stock_data = BasketStockData_Backtest()
x = stock_data.generate_dict(start="2020-01-01", end = "2021-01-01", list_of_tickers = ['MSFT', 'GOOG'], update_data=True)
    
funcs = priceFunctions(input_df = x['MSFT'], training_period = 250, fill_time = 'Open')
# funcs.ROC(lookback = 6, graphing = True)
# funcs.correlation_HL(lookback = 6, graphing = True)
# funcs.linregAngle(lookback = 6, graphing = True)
# funcs.linregSlope(lookback = 6, graphing = True)
# funcs.stddev(lookback = 6, graphing = True)
# funcs.variance(lookback = 6, graphing = True)

funcs.kurtosis(lookback = 20, graphing = True)