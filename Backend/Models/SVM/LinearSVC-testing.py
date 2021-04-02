# importing the libraries
import pandas as pd
import sklearn
from sklearn.preprocessing import LabelEncoder
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import svm, metrics
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pickle
from sklearn.svm import LinearSVC
import matplotlib.pyplot as plt
from sklearn.metrics import plot_confusion_matrix

# reading the csv file
pd_data = pd.read_csv('DetectPD-SMOTE.csv')

# pre processing using Label Encoder
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

# Creating the numpy arrays
X = np.array(X)
y = np.array(y)

# initializing variables
lowestAccuracy = 0
highestAccuracy = 0
lowModel = 0
highModel = 0
highCount = 0

for x in range(100):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)
    clf = LinearSVC(penalty='l2', C=1.0, random_state=None, dual=False, max_iter=10000)
    clf.fit(X_train, y_train)  # fitting  the training data into the model
    y_predict = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_predict) * 100  # getting accuracy as percentage
    if x == 0:  # first iteration
        lowModel = clf
        highModel = clf
        lowestAccuracy = accuracy
        highestAccuracy = accuracy
    else:
        # Creating a low model
        if accuracy < lowestAccuracy:
            lowestAccuracy = accuracy
            lowModel = clf
            print("low model")
            print(metrics.classification_report(y_test, y_predict))

        # Creating a high model
        elif accuracy > highestAccuracy:
            highCount = highCount + 1
            highestAccuracy = accuracy
            highModel = clf
            print("high model", highCount)
            print(metrics.classification_report(y_test, y_predict))
            # writing the high model into the pickle file
            with open('SVM_BestModel_%s.pickle' % highCount, 'wb') as high:
                pickle.dump(highModel, high, protocol=pickle.HIGHEST_PROTOCOL)

# writing the lowest model into the pickle file
with open('SVM_WorstModel.pickle', 'wb') as low:
    pickle.dump(lowModel, low, protocol=pickle.HIGHEST_PROTOCOL)
    print('success')

# Creating the labels
labels = ['negative', 'positive']

confusion_matrix(y_test, y_predict)
print(confusion_matrix)

# Plot non-normalized confusion matrix
titles_options = [("Confusion matrix, without normalization", None),
                  ("Normalized confusion matrix", 'true')]

for title, normalize in titles_options:
    disp = plot_confusion_matrix(clf, X_test, y_test, display_labels=labels, cmap=plt.cm.Blues, normalize=normalize)
    disp.ax_.set_title(title)

    print(title)
    print(disp.confusion_matrix)

plt.show()
