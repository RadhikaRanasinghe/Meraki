import numpy as np
import pandas as pd
import sklearn
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle
from sklearn.metrics import accuracy_score, classification_report

data = pd.read_csv("data/DetectPD-SMOTE.csv")

# Preprocessing
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

x = np.array(x)
y = np.array(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)

model = RandomForestClassifier()
model.fit(x_train, y_train)
print(model.score(x_test, y_test) * 100)

best_result1_file = "DetectPD_SMOTE/RF_BestModel1_SMOTE.pickle"
best_result2_file = "DetectPD_SMOTE/RF_BestModel2_SMOTE.pickle"
best_result3_file = "DetectPD_SMOTE/RF_BestModel3_SMOTE.pickle"
worst_result_file = "DetectPD_SMOTE/RF_WorstModel_SMOTE.pickle"

best_result1 = 0
best_result2 = 0
best_result3 = 0
worst_result = 100
hundred_count = 0

best_model1 = 0
best_model1_report = ""
best_model2 = 0
best_model2_report = ""
best_model3 = 0
best_model3_report = ""
worst_model = 0
worst_model_report = ""

for i in range(10000):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)
    model = RandomForestClassifier()
    model.fit(x_train, y_train)
    predicted = model.predict(x_test)

    acc = model.score(x_test, y_test) * 100

    print("Iteration " + str(i) + ": " + str(acc))

    if acc == 100:
        hundred_count += 1

    if acc > best_result1 or acc > best_result2 or acc > best_result3:
        if acc > best_result1:
            best_result1 = acc
            best_model1_report = sklearn.metrics.classification_report(y_test, predicted)
            with open(best_result1_file, 'wb') as file:
                pickle.dump(model, file)

        elif acc > best_result2:
            if best_result1 > acc:
                best_result2 = acc
                best_model2_report = sklearn.metrics.classification_report(y_test, predicted)
                with open(best_result2_file, 'wb') as file:
                    pickle.dump(model, file)
            else:
                pass

        else:
            if acc < best_result1 and acc < best_result2:
                best_result3 = acc
                best_model3_report = sklearn.metrics.classification_report(y_test, predicted)
                with open(best_result3_file, 'wb') as file:
                    pickle.dump(model, file)
            else:
                pass

    if acc < worst_result:
        with open(worst_result_file, 'wb') as file:
            pickle.dump(model, file)
        worst_result = acc
        worst_model_report = sklearn.metrics.classification_report(y_test, predicted)

    file1 = open("DetectPD_SMOTE/RF_results_SMOTE.md", "w")  # write mode
    file1.write("\n######**_The Best Model 1_**: \n\nAccuracy: " + str(best_result1) + "\n\n" + best_model1_report)
    file1.write("\n######**_The Best Model 2_**: \n\nAccuracy: " + str(best_result2) + "\n\n" + best_model2_report)
    file1.write("\n######**_The Best Model 3_**: \n\nAccuracy: " + str(best_result3) + "\n\n" + best_model3_report)
    file1.write("\n######**_The Worst Model_**: \n\nAccuracy: " + str(worst_result) + "\n\n" + worst_model_report)
    file1.write("\n\n######**_The number of models with 100% accuracy in 10,000 iterations_**:" + str(hundred_count))
    file1.close()

print("Best result A", best_result1)
print("Best result B", best_result2)
print("Best results C", best_result3)
print("Worst Result", worst_result)
print("num of hundreds", hundred_count)
