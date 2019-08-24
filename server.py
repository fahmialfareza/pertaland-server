from flask import Flask, request, abort
import json
import pandas as pd
import pylab as pl
import numpy as np
import scipy.optimize as opt
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
# %matplotlib inline
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.metrics import f1_score
import sys
import random

app = Flask("Pertaland")

@app.route('/', methods=['GET'])
def spbu():
    cell_df = pd.read_csv("spbu.csv")
    cell_df = cell_df.drop(['No'], axis=1)

    cell_df = cell_df.append({'RoadDensity' : random.randint(900, 2000) , 'GasStation' : random.randint(0, 5), 'Industry' : random.randint(0, 5), 'Home' : random.randint(50, 1000), 'Class' : 0}, ignore_index=True)

    feature_df = cell_df[['RoadDensity', 'GasStation', 'Industry', 'Home']]

    #train_feature_df = feature_df[0:100]
    #train_cell_df = cell_df[0:100]

    #train_cell_df

    X = preprocessing.StandardScaler().fit(feature_df).transform(feature_df.astype(float))
    y = cell_df['Class'].values

    length = X.shape
    length = length[0]

    X_train = X[0:(length-1)]
    y_train = y[0:(length-1)]

    X_test = X[(length-1):length]
    y_test = y[(length-1):length]

    clf = svm.SVC(kernel='rbf', gamma='auto')
    clf.fit(X_train, y_train)
    yhat = clf.predict(X_test)

    yhat = yhat[0]

    if yhat == 1:
        yhat = True
    else:
        yhat = False

    x = {}
    x['spbu'] = yhat

    y = json.dumps(x)

    return y

app.run(port=7777)
