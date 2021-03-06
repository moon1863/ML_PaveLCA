# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 23:36:18 2020

@author: Windows
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing the datatset
dataset=pd.read_csv('Initial_construction_asphalt_layer_final_version.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,9].values

##Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:,0]=labelencoder_X.fit_transform(X[:,0]) #different label assigned 
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()  #different column for diff. label 
                                             #and bin.val inject & make numarry

#Splittting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

#feature scaling 
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_Y = StandardScaler()
X_train_scaled=sc_X.fit_transform(X_train)
y_train_scaled=sc_Y.fit_transform(y_train.reshape(-1,1))

#fitting SVR ro the dataset
from sklearn import svm
regressor = svm.SVR(kernel = 'linear')
regressor.fit(X_train_scaled,y_train_scaled)

#predicting a new result
y_pred = sc_Y.inverse_transform(regressor.predict(sc_X.transform(X_test)))

#wight vectors
regressor.coef_