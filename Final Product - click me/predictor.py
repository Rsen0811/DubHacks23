import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

import joblib

m1 = joblib.load("models/m1.pkl")
m2 = joblib.load("models/m2.pkl")
m3 = joblib.load("models/m3.pkl")
m4 = joblib.load("models/m4.pkl")
m5 = joblib.load("models/m5.pkl")
m6 = joblib.load("models/m6.pkl")
m7 = joblib.load("models/m7.pkl")
m8 = joblib.load("models/m8.pkl")

def predictor(questionAns):
    return [int(x) for x in [m1.predict([questionAns])[0], m2.predict([questionAns])[0], m3.predict([questionAns])[0], m4.predict([questionAns])[0], m5.predict([questionAns])[0], m6.predict([questionAns])[0], m7.predict([questionAns])[0], m8.predict([questionAns])[0]]]
#print(predictor([1, 2, 3, 1, 2, 3, 1, 2, 2, 3, 3, 3, 3, 3, 3, 4, 3, 4, 3, 4, 3, 2, 1]))



    
