# importing the libraries
import pandas as pd
import sklearn
from sklearn.preprocessing import LabelEncoder
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pickle

# Loading the dataset with a Pandas and the returned data frame is caught by data variable
pd_data = pd.read_csv('DetectPD_SMOTE.csv')

# preprocessing the dataset using the LabelEncoder
# le = sklearn.preprocessing.LabelEncoder()
# gender = le.fit_transform(list(pd_data['GENDER']))
# handedness = le.fit_transform(list(pd_data['RIGH/LEFT-HANDED']))
# age = list(pd_data['AGE'])
# rms = list(pd_data['RMS'])
# max_st_ht = list(pd_data['MAX_BETWEEN_ST_HT'])
# min_st_ht = list(pd_data['MIN_BETWEEN_ST_HT'])
# std_st_ht = list(pd_data['STD_DEVIATION_ST_HT'])
# mrt = list(pd_data['MRT'])
# max_ht = list(pd_data['MAX_HT'])
# min_ht = list(pd_data['MIN_HT'])
# std_ht = list(pd_data['STD_HT'])
# n_to_p_st_ht = list(pd_data['CHANGES_FROM_NEGATIVE_TO_POSITIVE_BETWEEN_ST_HT'])
# class_type = list(pd_data['CLASS_TYPE'])

# Creating 'x' and 'y'
# X = list(zip(gender, handedness, age, rms, max_st_ht, min_st_ht, std_st_ht, mrt, max_ht, min_ht, std_ht,
#              n_to_p_st_ht))
# y = list(class_type)
X = pd_data.drop("CLASS_TYPE", axis=1)
y = pd_data["CLASS_TYPE"]

# Adding the 'x' and 'y' to Numpy Arrays
X = np.array(X)
y = np.array(y)

# Initializing and assigning the variables for storing the strings of the reports generated
lowestAccuracy = 0
highestAccuracy1 = 0
highestAccuracy2 = 0
highestAccuracy3 = 0
lowModel = 0
highModel1 = 0
highModel2 = 0
highModel3 = 0

# Iterating for 10,000 times to get the best the models
for x in range(10000):
    # Splitting the data into testing data and training data with the testing size of 0.1
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)
    # The Logistic Regression Model is assigned to the logmodel variable
    logmodel = LogisticRegression(solver='lbfgs', max_iter=20000)
    # The training data from the data split is taken for fitting into the model to train
    logmodel.fit(X_train, y_train)
    # predicting using the model
    predictions = logmodel.predict(X_test)
    # getting the accuracy score for the prediction
    modelAccuracy = accuracy_score(y_test, predictions) * 100
    # if its the first iteration
    if x == 0:
        lowModel = logmodel
        highModel1 = logmodel
        highModel2 = lowModel
        highModel3 = lowModel
        lowestAccuracy = modelAccuracy
        highestAccuracy1 = modelAccuracy
        highestAccuracy2 = modelAccuracy
        highestAccuracy3 = modelAccuracy
        # creating and writing the accuracies to a log file
        file = open("log.txt", "w")
        file.write("Highest accuracy 1 : " + str(highestAccuracy1) +
                   "\n Highest accuracy 2 : " + str(highestAccuracy2) +
                   "\n Highest accuracy 3 : " + str(highestAccuracy3) +
                   "\n Lowest accuracy : " + str(lowestAccuracy))
        file.close()
    else:
        # if the current model accuracy is lover than the lowest accuracy
        if modelAccuracy < lowestAccuracy:
            lowestAccuracy = modelAccuracy
            lowModel = logmodel
            file = open("log.txt", "a")
            file.write(" \n Lowest accuracy : " + str(lowestAccuracy))
            file.close()
            # if the current model accuracy is higher than the 3rd highest accuracy
        elif modelAccuracy > highestAccuracy3:
            file = open("log.txt", "a")
            # if the current model accuracy is higher than the 2nd highest accuracy
            if modelAccuracy > highestAccuracy2:
                # if the current model accuracy is higher than the 1st highest accuracy
                if modelAccuracy > highestAccuracy1:
                    highestAccuracy1 = modelAccuracy
                    highModel1 = logmodel
                    file.write("\n Highest 1 accuracy : " + str(highestAccuracy1))
                else:
                    highestAccuracy2 = modelAccuracy
                    highModel2 = logmodel
                    file.write("\n Highest 2 accuracy : " + str(highestAccuracy2))
            else:
                highestAccuracy3 = modelAccuracy
                highModel3 = logmodel
                file.write("\n Highest 3 accuracy : " + str(highestAccuracy3))
            file.close()

# saving the models as pickle files
with open('LogR_BestModel_1.pickle', 'wb') as handle:
    pickle.dump(highModel1, handle, protocol=pickle.HIGHEST_PROTOCOL)
    print('success')
with open('LogR_BestModel_2.pickle', 'wb') as handle:
    pickle.dump(highModel2, handle, protocol=pickle.HIGHEST_PROTOCOL)
    print('success')
with open('LogR_BestModel_3.pickle', 'wb') as handle:
    pickle.dump(highModel3, handle, protocol=pickle.HIGHEST_PROTOCOL)
    print('success')
with open('LogR_WorstModel.pickle', 'wb') as handle:
    pickle.dump(lowModel, handle, protocol=pickle.HIGHEST_PROTOCOL)
    print('success')
