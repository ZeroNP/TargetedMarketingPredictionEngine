# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 14:05:21 2020

@author: Shreyas
"""
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

dataset = pd.read_csv('banking.csv')
dataset = dataset.dropna()

#grouping
dataset['education'] = np.where(dataset['education']=='basic.9y','Basic',dataset['education'])
dataset['education'] = np.where(dataset['education']=='basic.6y','Basic',dataset['education'])
dataset['education'] = np.where(dataset['education']=='basic.4y','Basic',dataset['education'])

#view observations
observations = dataset.groupby('y').mean()

cat_vars = ['job','marital','education','default','housing','loan','contact','month','day_of_week','poutcome']
for var in cat_vars:
    cat_list = 'var'+'_'+var
    cat_list = pd.get_dummies(dataset[var], prefix=var)
    data1=dataset.join(cat_list)
    dataset=data1cat_vars=['job','marital','education','default','housing','loan','contact','month','day_of_week','poutcome']
data_vars=dataset.columns.values.tolist()
to_keep=[i for i in data_vars if i not in cat_vars]