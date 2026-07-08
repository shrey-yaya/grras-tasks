#!/usr/bin/env python
# coding: utf-8

# #Importing the Dependencies

# In[3]:

"""
Smart Property Valuation System
XGBoost-Based House Price Prediction Model
Author: Modassir Alam
Version: 1.0.0

"""



# pip install xgboost


# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.datasets
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.preprocessing import StandardScaler
from sklearn import metrics


# #Importing the Boston House Price Dataset

# In[20]:

# Load dataset
url = "https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv"
house_price_dataset = pd.read_csv(url)

# Display the first few rows of the dataset
print(house_price_dataset.head())

# Optional: Rename 'medv' to 'Price' for clarity
house_price_dataset.rename(columns={'medv': 'Price'}, inplace=True)
print(house_price_dataset.head())


# In[21]:


house_price_dataset.shape


# In[22]:
# data exploration code to House Price Prediction.py

#check for missing values
house_price_dataset.isnull().sum().sum()


# In[23]:


#statistical measure of the dataset
house_price_dataset.describe()


# In[24]:

#Add correlation analysis and heatmap
correlation = house_price_dataset.corr()


# In[25]:


# construction a heatmap to understand the correlation
plt.figure(figsize=(10,10))
sns.heatmap(correlation,cbar=True,square=True, fmt='.1f', annot=True,annot_kws={'size':8},cmap='Blues')


# #Splitting the data and Target

# In[27]:
#Add data splitting

X= house_price_dataset.drop(['Price'],axis=1)
Y= house_price_dataset['Price']


# In[28]:


print(X)
print(Y)


# #Splitting the data into Training data and Test data

# In[33]:

#Add train-test split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=2)


# In[34]:


print(X.shape,X_train.shape,X_test.shape)


# #Model Training

# #XGBoost Regressor

# In[36]:

#Add model initialization
# loading the model
model = XGBRegressor()


# In[38]:

#Add model training
model.fit(X_train,Y_train)


# #prediction on training data

# In[39]:

#Add training predictions and metrics
#accuracy for prediction on training data
training_data_prediction = model.predict(X_train)


# In[40]:


print(training_data_prediction)


# In[42]:


# R square error
score_1 = metrics.r2_score(Y_train,training_data_prediction)

#Mean Absolute error
score_2= metrics.mean_absolute_error(Y_train,training_data_prediction)

print("R square error: ", score_1)
print("Mean Absolute error: ",score_2)


# #Prediction on Test Data

# In[44]:


#accuracy for prediction on test data
test_data_prediction = model.predict(X_test)


# In[45]:

#Add testing predictions and metrics
# R square error
score_1 = metrics.r2_score(Y_test,test_data_prediction)

#Mean Absolute error
score_2= metrics.mean_absolute_error(Y_test,test_data_prediction)

print("R square error: ", score_1)
print("Mean Absolute error: ",score_2)


# #Visualizing the actual prices and predicted prices 

# In[47]:
#Enhance plots with better colors, labels, and styling

#Add training set visualization

plt.scatter(Y_train,training_data_prediction)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual Price vs Predicted Price")
plt.show()


# In[ ]:




