"""
# Enter the sheet number between 0 to 9
# Function returns a dataframe with the price from 2016 to present day
# small_data_flag is set to true is the last 100 trading days quotes are required
"""
from copy import Error
import pandas as pd
import yfinance as yf
import os
from pathlib import Path
import math

class BasketStockData_Backtest:
    def __init__(self):
        self.out_dict = {}

    def generate_dict(self, start = "0000-00-00", end = "0000-00-00", list_of_tickers = [], update_data=True):
        ctr = 1
        Indicator_CSVs = Path(os.getcwd()) / 'BackTestData'

        if update_data:        
            basket_data = yf.download(
            tickers = list_of_tickers,
            start = start,
            end = end,
            interval = '1d',
            group_by = 'ticker',
            auto_adjust = True,
            prepost = False,
            threads = True,
            proxy = None
            )
            basket_data = basket_data.T

            for ticker in list_of_tickers:
                basket_data.loc[(ticker,),].T.to_csv((Indicator_CSVs / f'{ticker}.csv'), sep=',', encoding='utf-8')

        empty_dates_indices = []
        df1 = pd.read_csv(Indicator_CSVs / f"{list_of_tickers[0]}.csv")
        empty_dates_indices = self.getIndexes(df1['High'], 0)

        for ticker in list_of_tickers:
            df1 = pd.read_csv(Indicator_CSVs / f"{ticker}.csv")
            df_out = pd.DataFrame()
            df_out['Open'] = df1['Open']
            df_out['High'] = df1['High']
            df_out['Low'] = df1['Low']
            df_out['Close'] = df1['Close']
            df_out['Volume'] = df1['Volume']
            df_out['Datetime'] = df1['Date']
            df_out['Typical Price'] = ((df_out['High'] + df_out['Low'] + df_out['Close']) / 3).round(2)
            
            df_out = df_out.drop(empty_dates_indices, inplace=False)
            df_out.reset_index(inplace=True, drop=True)

            empty_dates_indices_for_ticker = []
            empty_dates_indices_for_ticker = self.getIndexes(df_out['High'], 0)
            shifted_df = df_out.shift(1)
            for i in empty_dates_indices_for_ticker:
                df_out.at[i,'High'] = shifted_df.loc[i,'High']
                df_out.at[i,'Open'] = shifted_df.loc[i,'Open']
                df_out.at[i,'Low'] = shifted_df.loc[i,'Low']
                df_out.at[i,'Close'] = shifted_df.loc[i,'Close']
                df_out.at[i,'Volume'] = shifted_df.loc[i,'Volume']
                df_out.at[i,'Typical Price'] = shifted_df.loc[i,'Typical Price']
                shifted_df = df_out.shift(1)

            self.out_dict[ticker] = df_out

        return self.out_dict

    def getIndexes(self, npArray, shift):
        listOfPos = list()
        npArray_list = list(npArray)
        for i, price in enumerate(npArray_list):
            if math.isnan(price):
                listOfPos.append(i+shift)
        return listOfPos
    
    def __str__(self):
        return (self.out_dict.to_string())

def main():
    stock_data = BasketStockData_Backtest()
    x = stock_data.generate_dict(start="2020-01-01", end = "2021-01-01", list_of_tickers = ['MSFT', 'GOOG'], update_data=True)
    print(x)
    

if __name__ == '__main__':
    main()





