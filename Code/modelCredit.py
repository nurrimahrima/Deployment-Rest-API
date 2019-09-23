
# coding: utf-8

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression
from sklearn.ensemble import RandomForestClassifier

df=pd.read_csv('training.csv')
df.head()

#drop the unused variable from dataset
df2 = df.drop('ID', axis = 1)
df2.head()

# ## 4. MACHINE LEARNING MODEL
test=pd.read_csv('testing.csv',sep=';')
test.head()

#drop the unused variable from dataset
test2=test.drop('ID',axis=1)

#Define x and y variable for modeling
x=df2.drop(columns=['TARGET'])
y = df2["TARGET"]
y[0:5]

x_trainset, x_testset, y_trainset, y_testset = train_test_split(x, y, test_size=0.3, random_state=3)

Tree = DecisionTreeClassifier(criterion="gini", max_depth = 10) #it shows the default parameters
Tree.fit(x_trainset,y_trainset)
predTree = Tree.predict(x_testset)
print("Decision Tree's Accuracy: ", metrics.accuracy_score(y_testset, predTree))
predTree_test = Tree.predict(test2)
# ### The Result of Testing Data Prediction
test2['TARGET']=predTree_test

import pickle
#saving model to disk
pickle.dump(Tree, open('DecisionTree.pkl','wb'))
#load model to compare the result
model=pickle.load(open('DecisionTree.pkl','rb'))
print(Tree.predict([[400000, 1, 1, 2, 35, 1, 2, 0, 33720, 29480, 33720, 15000, 15000, 12000]]))


