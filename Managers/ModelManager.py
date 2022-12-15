import math
import numpy as np
import pandas as pd

class ModelManager:
    
    def __init__(self):
        self.models_dict = {} 
        #Format of Position dictionary
        # {
        #    Model1_ID: Model Object
        #    .
        #    .
        #    .
        #    ModelN_ID: Model Object
        # }

    def getModelsDict(self):
            pass

    def getModelObj(self, modelID: str):
            pass
            
    def getPnL(self): #Automatically detect if we are dealing with an individual Model or the Whole Portfolio
            pass
    
    def _tests(self):
        pass

if __name__ == '__main__':
    pass
