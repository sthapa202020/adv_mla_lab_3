Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Solution:
from scipy.stats import mode

class NullClassifier:
    """
...     Class used as baseline model for classification problem
...     ...
... 
...     Attributes
...     ----------
...     y : Numpy Array-like
...         Target variable
...     pred_value : Float
...         Value to be used for prediction
...     preds : Numpy Array
...         Predicted array
... 
...     Methods
...     -------
...     fit(y)
...         Store the input target variable and calculate the predicted value to be used
...     predict(y)
...         Generate the predictions
...     fit_predict(y)
...         Perform a fit followed by predict
...     """
... 
... 
...     def __init__(self):
...         self.y = None
...         self.pred_value = None
...         self.preds = None
... 
...     def fit(self, y):
...         self.y = y
...         self.pred_value = mode(y).mode
... 
...     def predict(self, y):
...         self.preds = np.full((len(y), 1), self.pred_value)
...         return self.preds
... 
...     def fit_predict(self, y):
...         self.fit(y)
