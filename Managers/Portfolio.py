import math
import numpy as np
import pandas as pd

class Portfolio:
    
    def __init__(self):
        self.position_dictionary = {} 
        #Format of Position dictionary
        # {
        #    Position1_ID/Model_ID: position_object/Portfolio Object made of position object belonging to the model
        #    .
        #    .
        #    .
        #    PositionN_ID: position_object/Portfolio Object made of position object belonging to the model
        # }

    def getPositionDict(self):
            pass

    def updatePositionDict(self):
            pass

    def getPosition(self, ID): #ID can be that of position or model
            pass
            
    def getPnL(self): #Automatically detect if we are dealing with an individual Model or the Whole Portfolio
            pass
    
    def _tests(self):
        pass

if __name__ == '__main__':
    pass
