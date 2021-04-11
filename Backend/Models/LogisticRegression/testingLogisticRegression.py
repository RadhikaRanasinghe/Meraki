import pickle

import inline as inline
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math
from matplotlib import pyplot
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, plot_confusion_matrix, plot_roc_curve, roc_curve, roc_auc_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, precision_score, f1_score, recall_score
import sklearn.metrics as metrics
from sklearn.metrics import classification_report

pd_data = pd.read_csv("DetectPD.csv")
model = open("DetectPD/LogR_BestModel_1.pickle", "rb")
logModel = pickle.load(model)
# preprocessing the dataset using the LabelEncoder
le = sklearn.preprocessing.LabelEncoder()
gender = le.fit_transform(list(pd_data['GENDER']))
handedness = le.fit_transform(list(pd_data['RIGH/LEFT-HANDED']))
age = list(pd_data['AGE'])
rms = list(pd_data['RMS'])
max_st_ht = list(pd_data['MAX_BETWEEN_ST_HT'])
min_st_ht = list(pd_data['MIN_BETWEEN_ST_HT'])
std_st_ht = list(pd_data['STD_DEVIATION_ST_HT'])
mrt = list(pd_data['MRT'])
max_ht = list(pd_data['MAX_HT'])
min_ht = list(pd_data['MIN_HT'])
std_ht = list(pd_data['STD_HT'])
n_to_p_st_ht = list(pd_data['CHANGES_FROM_NEGATIVE_TO_POSITIVE_BETWEEN_ST_HT'])
class_type = list(pd_data['CLASS_TYPE'])

# Creating 'x' and 'y'
X = list(zip(gender, handedness, age, rms, max_st_ht, min_st_ht, std_st_ht, mrt, max_ht, min_ht, std_ht,
             n_to_p_st_ht))
y = list(class_type)

# Adding the 'x' and 'y' to Numpy Arrays
X = np.array(X)
y = np.array(y)

# Splitting the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

# Predicting using the model
predictions = logModel.predict(X_test)

# Getting the confusion matrix
con_matrix = confusion_matrix(y_test, predictions)

# Plotting the confusion matrix
plot_confusion_matrix(logModel, X_test, y_test)

# Plotting hte roc curve
metrics.plot_roc_curve(logModel, X_test, y_test)

# printing hte classification report
print(classification_report(y_test, predictions))

# Displaying the plotted graphs
plt.show()
