#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 12:20:33 2020

@author: sjsingh
"""

import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, train_test_split

import warnings
warnings.filterwarnings('ignore')

brainwave_df = pd.read_csv('/home/sjsingh/Desktop/Smart EEG/emotions.csv')
label_df = brainwave_df['label']
brainwave_df.drop('label', axis = 1, inplace=True)
 
def Accuracy():
    pl_random_forest = Pipeline(steps=[('random_forest', RandomForestClassifier())])
    scores = cross_val_score(pl_random_forest, brainwave_df, label_df, cv=10,scoring='accuracy')
    print('Accuracy for RandomForest : ', scores.mean())
    


def predict(data):
    clf=RandomForestClassifier(n_estimators=100)
    clf.fit(brainwave_df,label_df)
    
    predict_df = pd.DataFrame(data)
    y_pred=clf.predict(predict_df)
    
    a=0
    count=0
    while a<len(y_pred)-1 :
        if y_pred[a] == 'NEGATIVE':
            if y_pred[a+1] == 'POSITIVE':
                count+=1
        elif y_pred[a] == 'POSITIVE':
            if y_pred[a+1] == 'NEGATIVE':
                count+=1
        a+=1
        
        
    return 'Rate of change of emotion is : {}% over {} seconds'.format(int(count*100/predict_df.shape[0]),predict_df.shape[0])
    
if __name__ == '__main__':
    predict(pd.read_csv('/home/sjsingh/Desktop/Smart EEG/test - test.csv'))
    
