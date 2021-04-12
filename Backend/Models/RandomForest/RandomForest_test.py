# importing the libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn
import sklearn.metrics as metrics
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import plot_confusion_matrix
from sklearn.model_selection import train_test_split

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

# The training data from the data split is taken for fitting into the model to train
model.fit(x_train, y_train)

# Predicting using the testing data
predicted = model.predict(x_test)

# The accuracy score of the model taken as percentage
acc = model.score(x_test, y_test) * 100

# Printing the accuracy of the model
print(sklearn.metrics.classification_report(y_test, predicted))

labels = ['negative', 'positive']
confusion_matrix(y_test, predicted)

# Printing the confusion matrix
print(confusion_matrix);

titles_options = [("Confusion matrix, without normalization", None),
                  ("Normalized confusion matrix", 'true')]

for title, normalize in titles_options:
    disp = plot_confusion_matrix(model, x_test, y_test, display_labels=labels, cmap=plt.cm.Blues, normalize=normalize)
    disp.ax_.set_title(title)

    print(title)
    print(disp.confusion_matrix)

# Plotting ROC curve
metrics.plot_roc_curve(model, x_test, y_test)
plt.show()
