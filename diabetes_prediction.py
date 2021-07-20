# -*- coding: utf-8 -*-
"""Diabetes Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x384j0cEAKhvuNXKaUfiIMmqTx2MJtoD

Importing the libraries
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
import joblib

"""Data Collection and Analysis"""

#loading the dataset to a pandas dataframe 

diabetes_data = pd.read_csv('C:/Users/91970/projects/genometrics/diabetes .csv')

diabetes_data.head()

diabetes_data.shape

diabetes_data.describe()

diabetes_data['Outcome'].value_counts()

"""0 --- Non- Diabetic

1 --- Diabetic
"""

diabetes_data.groupby('Outcome').mean()

x=diabetes_data.drop(columns='Outcome',axis=1)
y=diabetes_data['Outcome']
print("X: ",x)
print("----------------------------------")
print("Y: ",y)

"""Data Standardization"""

scaler= StandardScaler()
scaler.fit(x)

standardized_data = scaler.transform(x)

print(standardized_data)

x=standardized_data
y=diabetes_data['Outcome']

print(x)
print(y)

x_train,x_test,y_train,y_test = train_test_split(x,y, test_size=0.2, stratify=y, random_state=2)

print(x.shape, x_train.shape, x_test.shape)

"""Training the model"""

cls=svm.SVC(kernel='linear')

#fitting triaining data to the classifier
cls.fit(x_train,y_train)



filename= 'saved_model.sav'
saved_model=joblib.dump(cls,filename)

#x_train_pred = saved_model.predict(x_train)
#training_data_accuracy = accuracy_score(x_train_pred, y_train)
#print("Accuracy on training data: ", training_data_accuracy)

'''cls=joblib.load('saved_model.sav')
lis=[3,74,68,28,45,29.7,0.293,23]
data_array = np.asarray(lis)
arr= data_array.reshape(1,-1)
ans=cls.predict(arr)
print(ans)'''