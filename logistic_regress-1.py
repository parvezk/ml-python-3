import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn import linear_model, datasets
from sklearn.cross_validation import train_test_split

data = pd.read_csv('train.csv', header=0)
print(data.shape)
print(list(data.columns))