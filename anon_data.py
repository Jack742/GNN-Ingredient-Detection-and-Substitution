import pickle
import numpy as np 
import pandas as pd 

data = pd.read_csv('UNBALANCED_palm oil_balanced_data_NEWBRANDS.csv')

data['brand'],_ = pd.factorize(data['brand'])#.apply(lambda x: pd.factorize(x))
data['name'],_ = pd.factorize(data['name'])#.apply(lambda x: pd.factorize(x))

data.to_csv('UNBALANCED_palm oil_balanced_data_NEWBRANDS.csv')