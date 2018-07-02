#coding:utf-8
import xgboost as xgb
import sklearn
from sklearn.model_selection import train_test_split
import numpy as np
from matplotlib.dates import datestr2num
import pandas as pd

data_path='/Users/mac/Downloads/tap4fun竞赛数据/tap_fun_train.csv'
pop_column=['user_id','register_time']

with open(data_path) as f:
    data=pd.read_csv(f)

for key in pop_column:
    data.pop(key)

train_data,test_data=train_test_split(data.iloc[:,:],test_size=0.001)



