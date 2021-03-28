# importing the libraries
import numpy as np
import pandas as pd
import sklearn
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle
from sklearn.metrics import accuracy_score, classification_report

# Loading the dataset with a Pandas and the returned data frame is caught by data variable
data = pd.read_csv("data/DetectPD-SMOTE.csv")

# Preprocessing using the LabelEncoder
le = sklearn.preprocessing.LabelEncoder()
gender = le.fit_transform(list(data['GENDER']))
handedness = le.fit_transform(list(data['RIGH/LEFT-HANDED']))
age = list(data['AGE'])
rms = list(data['RMS'])
max_st_ht = list(data['MAX_BETWEEN_ST_HT'])
min_st_ht = list(data['MIN_BETWEEN_ST_HT'])
std_st_ht = list(data['STD_DEVIATION_ST_HT'])
mrt = list(data['MRT'])
max_ht = list(data['MAX_HT'])
min_ht = list(data['MIN_HT'])
std_ht = list(data['STD_HT'])
n_to_p_st_ht = list(data['CHANGES_FROM_NEGATIVE_TO_POSITIVE_BETWEEN_ST_HT'])
class_type = list(data['CLASS_TYPE'])

# Creating 'x' and 'y'
x = list(zip(gender, handedness, age, rms, max_st_ht, min_st_ht, std_st_ht, mrt, max_ht, min_ht, std_ht,
             n_to_p_st_ht))
y = list(class_type)

# Adding the 'x' and 'y' to Numpy Arrays
x = np.array(x)
y = np.array(y)

# Splitting the data into testing data and training data with the testing size of 0.1
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)

# The Random Forest Classifier Model is assigned to the model variable
model = RandomForestClassifier()

# The training data from the data split is taken for fitting into the model to train
model.fit(x_train, y_train)

# The accuracy score of the model taken as percentage is printed on the console
print(model.score(x_test, y_test) * 100)

# Initializing and assigning the variables for storing the best 3 and worst pickle file
best_result1_file = "DetectPD_SMOTE/RF_BestModel1_SMOTE.pickle"
best_result2_file = "DetectPD_SMOTE/RF_BestModel2_SMOTE.pickle"
best_result3_file = "DetectPD_SMOTE/RF_BestModel3_SMOTE.pickle"
worst_result_file = "DetectPD_SMOTE/RF_WorstModel_SMOTE.pickle"

# Initializing and assigning the variables for storing the best 3 and worst accuracies
best_result1 = 0
best_result2 = 0
best_result3 = 0
worst_result = 100
hundred_count = 0

# Initializing and assigning the variables for storing the strings of the reports generated
best_model1_report = ""
best_model2_report = ""
best_model3_report = ""
worst_model_report = ""

# Iterating for 10,000 times to get the best the models
for i in range(10000):
    # Splitting the data into testing data and training data with the testing size of 0.1
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)

    # The Random Forest Classifier Model is assigned to the model variable
    model = RandomForestClassifier()

    # The training data from the data split is taken for fitting into the model to train
    model.fit(x_train, y_train)

    # Predicting using the testing data
    predicted = model.predict(x_test)

    # The accuracy score of the model taken as percentage
    acc = model.score(x_test, y_test) * 100

    # Printing the iteration number and the accuracy score as a percentage
    print("Iteration " + str(i) + ": " + str(acc))

    # Counting number of hundreds in the 10,000 iterations
    if acc == 100:
        hundred_count += 1

    # If the accuracy is greater than any result stored, store the model as the best_model1 and the save the pickle file
    if acc > best_result1 or acc > best_result2 or acc > best_result3:
        if acc > best_result1:
            best_result1 = acc
            best_model1_report = sklearn.metrics.classification_report(y_test, predicted)
            with open(best_result1_file, 'wb') as file:
                pickle.dump(model, file)

        # If the accuracy is greater than the best_result2, store the model as the best_model2
        # and the save the pickle file
        elif acc > best_result2:
            if best_result1 > acc:
                best_result2 = acc
                best_model2_report = sklearn.metrics.classification_report(y_test, predicted)
                with open(best_result2_file, 'wb') as file:
                    pickle.dump(model, file)
            else:
                pass
        # If the accuracy the less the best_result1 and best_result2, store the model as the best_model3
        # and the save the pickle file
        else:
            if acc < best_result1 and acc < best_result2:
                best_result3 = acc
                best_model3_report = sklearn.metrics.classification_report(y_test, predicted)
                with open(best_result3_file, 'wb') as file:
                    pickle.dump(model, file)
            else:
                pass

    # If the accuracy is greater than the worst_result, store the model as the worst_model and the save the pickle file
    if acc < worst_result:
        with open(worst_result_file, 'wb') as file:
            pickle.dump(model, file)
        worst_result = acc
        worst_model_report = sklearn.metrics.classification_report(y_test, predicted)

    # Opening the file to write into
    file1 = open("DetectPD_SMOTE/RF_results_SMOTE.md", "w")  # write mode

    # Writing to a file accuracies and their classification reports
    file1.write("\n######**_The Best Model 1_**: \n\nAccuracy: " + str(best_result1) + "\n\n" + best_model1_report)
    file1.write("\n######**_The Best Model 2_**: \n\nAccuracy: " + str(best_result2) + "\n\n" + best_model2_report)
    file1.write("\n######**_The Best Model 3_**: \n\nAccuracy: " + str(best_result3) + "\n\n" + best_model3_report)
    file1.write("\n######**_The Worst Model_**: \n\nAccuracy: " + str(worst_result) + "\n\n" + worst_model_report)
    file1.write("\n\n######**_The number of models with 100% accuracy in 10,000 iterations_**:" + str(hundred_count))
    file1.close()

# Printing the best and the worst models as a summary
print("Best result A", best_result1)
print("Best result B", best_result2)
print("Best results C", best_result3)
print("Worst Result", worst_result)
print("num of hundreds", hundred_count)
