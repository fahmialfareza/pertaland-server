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
import spbu
import hotel
import minimarket

app = Flask("Pertaland")

@app.route('/pertaland', methods=['GET'])
def pertaland():
    data = {}
    data['spbu'] = spbu.spbu()
    data['hotel'] = hotel.hotel()
    data['minimarket'] = minimarket.minimarket()

    print(data)

    return data

app.run(host='0.0.0.0', port=7777)
