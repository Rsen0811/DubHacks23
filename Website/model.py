import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

import joblib


df = pd.read_csv("ed.csv")
#df.dropna(how = "any", inplace = True)
df.fillna(3, inplace = True)



train, test = train_test_split(df, test_size=1)

X = pd.DataFrame(train, columns = ["Internet", "PC", "Reading", "Dancing", "Musical Instruments", "Writing", "Passive Sport", "Active Sport", "Fun Socializing", "Pets", "Smoking", "Alcohol", "Healthy Eating", "Socially Aware", "Anti-Procrastination", "Writing Planner", "Workaholism", "Planning Ahead", "Friend Count", "Punctuality", "Assertiveness", "Num HobbiesIntrests", "Internet Usage" ])
y = pd.DataFrame(train, columns = ["Regret Score", "Hypochondria Score", "Mood Swings Score", "Anger Score", "Emotional Negativity Score", "Happiness Score", "Energy Score", "Loneliness Score"])



X2 = pd.DataFrame(test, columns = ["Internet", "PC", "Reading", "Dancing", "Musical Instruments", "Writing", "Passive Sport", "Active Sport", "Fun Socializing", "Pets", "Smoking", "Alcohol", "Healthy Eating", "Socially Aware", "Anti-Procrastination", "Writing Planner", "Workaholism", "Planning Ahead", "Friend Count", "Punctuality", "Assertiveness", "Num HobbiesIntrests", "Internet Usage" ])
y2 = pd.DataFrame(test, columns = ["Regret Score", "Hypochondria Score", "Mood Swings Score", "Anger Score", "Emotional Negativity Score", "Happiness Score", "Energy Score", "Loneliness Score"])


m1 = KNeighborsClassifier(n_neighbors=10, weights='distance', algorithm = "ball_tree")
m2 = KNeighborsClassifier(n_neighbors=10, weights='distance', algorithm = "ball_tree")
m3 = KNeighborsClassifier(n_neighbors=10, weights='distance', algorithm = "brute")
m4 = KNeighborsClassifier(n_neighbors=10, weights='distance', algorithm = "brute")
m5 = KNeighborsClassifier(n_neighbors=10, weights='distance', algorithm = "ball_tree")
m6 = KNeighborsClassifier(n_neighbors=10, weights='distance', algorithm = "brute")
m7 = KNeighborsClassifier(n_neighbors=10, weights='distance', algorithm = "kd_tree")
m8 = KNeighborsClassifier(n_neighbors=10, weights='distance', algorithm = "brute")

m1.fit(X,y["Regret Score"])
#print(m1.score(X2, y2["Regret Score"]))
m2.fit(X,y["Hypochondria Score"])
#print(m2.score(X2, y2["Hypochondria Score"]))
m3.fit(X,y["Mood Swings Score"])
#print(m3.score(X2, y2["Mood Swings Score"]))
m4.fit(X,y["Anger Score"])
#print(m4.score(X2, y2["Anger Score"]))
m5.fit(X,y["Emotional Negativity Score"])
#print(m5.score(X2, y2["Emotional Negativity Score"]))
m6.fit(X,y["Happiness Score"])
#print(m6.score(X2, y2["Happiness Score"]))
m7.fit(X,y["Energy Score"])
#print(m7.score(X2, y2["Energy Score"]))
m8.fit(X,y["Loneliness Score"])
#print(m8.score(X2, y2["Loneliness Score"]))

joblib.dump(m1, "m1.pkl")
joblib.dump(m2, "m2.pkl")
joblib.dump(m3, "m3.pkl")
joblib.dump(m4, "m4.pkl")
joblib.dump(m5, "m5.pkl")
joblib.dump(m6, "m6.pkl")
joblib.dump(m7, "m7.pkl")
joblib.dump(m8, "m8.pkl")





