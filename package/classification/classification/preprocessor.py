import typing as t 
import pandas as pd 
import numpy as np 
from sklearn.base import BaseEstimator, TransformerMixin

class NumericImputer(BaseEstimator, TransformerMixin):
    def __init__(self, variable: t.List[str]=None) -> None: 
        if not isinstance(variable, list):
            self.variable = [variable]
        else:
            self.variable = variable

    def fit(self, X: pd.DataFrame, y:pd.Series =None) -> 'NumericImputer': 
        self.imputer_dict = {}
        for feature in self.variable: 
            self.imputer_dict[feature] = X[feature].median()[0]
        return self
    
    def transform(self, X:pd.DataFrame) -> pd.DataFrame:
        X = X.copy()
        for feature in self.variable:
            X[feature] = X[feature].fillna(self.imputer_dict[feature], inplace = True)
        return X

class LogTransformation(BaseEstimator, TransformerMixin): 
    def __init__(self, variable:t.List[str]= None) ->None: 
        if not isinstance(variable, list):
            self.variable = [variable]
        else: 
            self.variable = variable
    
    def fit(self, X:pd.DataFrame, y:pd.Series = None) -> 'LogTransfromation': 
        return x

    def transform(self, X:pd.DataFrame) -> pd.DataFrame: 
        X = X.copy()
        if not (X[self.variable]> 0).all().all(): 
            vars = self.variable[(X[self.variable]<0).any()]
            raise InvalidModelInputError(
                f'variable contains zero or negative values'
                f"can't apply log transformation"
            )
        for feature in self.variable: 
            X[feature] = np.log(X[feature])
        return X
        
