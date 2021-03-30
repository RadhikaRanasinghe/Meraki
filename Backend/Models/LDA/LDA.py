# importing the libraries
import pandas as pd
import sklearn
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.preprocessing import LabelEncoder
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pickle

# Loading the dataset with Pandas
pd_data = pd.read_csv('Data/DetectPD.csv')

# Preprocessing the dataset
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


# initialing variables for getting best models
lowestAccuracy = 0
highestAccuracy = 0

lowModel = 0
highModel = 0

# adding 'X' and 'Y' to Numpy array
X = np.array(X)
y = np.array(y)

# Iterating the model 10,000 times using for loop
count = 1
for x in range(10000):
    # splitting data into testing data and training data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

    # Assigning linear discriminant analysis classifier  to variable
    clf = LinearDiscriminantAnalysis()
    # Adding the split data into classifier
    clf.fit(X_train, y_train)

    # Running predictions using  test data
    predictions = clf.predict(X_test)

    # getting accuracy as percentage
    accuracy = accuracy_score(y_test, predictions) * 100

# saving the data into pickle files
    if x == 0:
        lowModel = clf
        highModel = clf
        lowestAccuracy = accuracy
        highestAccuracy = accuracy
    else:
        # saving the lowest accuracy model
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
            # saving the highest accuracy model
            print("==========High=========")
            print(sklearn.metrics.classification_report(y_test, predictions))
            print(accuracy)
            highestAccuracy = accuracy
            highModel = clf
            with open('LDA_high_result' + str(accuracy) + '.pickle', 'wb') as handle:
                pickle.dump(highModel, handle, protocol=pickle.HIGHEST_PROTOCOL)
                print('success')

