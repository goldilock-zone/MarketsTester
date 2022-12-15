import pandas as pd
class Broker:
    """
    Functions: This mainly takes care of transaction cost and makes an order log
    """
    def __init__(self,*, current_data, buffer_percent, transaction_cost_percent, order_fill_time = 'Typical Price'):
        pass

    def buy(self,*, ticker, amount, existingOrderFlag):
        pass

    def sell(self,*, ticker, amount, existingOrderFlag):
        pass

    def order_log(self):
        out_log = ""
        return out_log

if __name__ == '__main__':
    pass