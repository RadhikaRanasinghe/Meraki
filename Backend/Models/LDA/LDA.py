import pandas as pd
import sklearn
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.preprocessing import LabelEncoder
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pickle

pd_data = pd.read_csv('Data/DetectPD.csv')

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

lowestAccuracy = 0
highestAccuracy = 0

lowModel = 0
highModel = 0

X = np.array(X)
y = np.array(y)

count = 1
for x in range(10000):

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)
    clf = LinearDiscriminantAnalysis()
    clf.fit(X_train, y_train)
    predictions = clf.predict(X_test)

    accuracy = accuracy_score(y_test, predictions) * 100

    if x == 0:
        lowModel = clf
        highModel = clf
        lowestAccuracy = accuracy
        highestAccuracy = accuracy
    else:
        if accuracy < lowestAccuracy:
            lowestAccuracy = accuracy
            lowModel = clf
            print("==========Low=========")
            print(sklearn.metrics.classification_report(y_test, predictions))
            print(accuracy)
            with open('LDA_low_result' + str(accuracy) + '.pickle', 'wb') as handle:
                pickle.dump(lowModel, handle, protocol=pickle.HIGHEST_PROTOCOL)
                print('success')

        elif accuracy > highestAccuracy:
            print("==========High=========")
            print(sklearn.metrics.classification_report(y_test, predictions))
            print(accuracy)
            highestAccuracy = accuracy
            highModel = clf
            with open('LDA_high_result' + str(accuracy) + '.pickle', 'wb') as handle:
                pickle.dump(highModel, handle, protocol=pickle.HIGHEST_PROTOCOL)
                print('success')

