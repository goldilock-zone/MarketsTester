import talib as TA
import numpy as np
from talib import MA_Type

close = np.random.random(100)
output = TA.BBANDS(close, matype=MA_Type.T3)

print(output)
