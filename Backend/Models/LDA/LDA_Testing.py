import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, plot_confusion_matrix, plot_roc_curve, roc_curve, roc_auc_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, precision_score, f1_score, recall_score
import sklearn.metrics as metrics

pd_data = pd.read_csv('Data/DetectPD_SMOTE_improved.csv')
model = open("DetectPD_SMOTE_Improved/LDA_BestModel_1.pickle", "rb")
clf = pickle.load(model)

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

X = np.array(X)
y = np.array(y)

# splitting data into testing data and training data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

# Adding the split data into classifier
clf.fit(X_train, y_train)

# Running predictions using  test data
predictions = clf.predict(X_test)

# getting accuracy as percentage
accuracy = accuracy_score(y_test, predictions) * 100
print(sklearn.metrics.classification_report(y_test, predictions))
print(accuracy)

# Creating confusion matrix
labels = ['negative', 'positive']
confusion_matrix(y_test, predictions)
print(confusion_matrix);

titles_options = [("Confusion matrix, without normalization", None),
                  ("Normalized confusion matrix", 'true')]
for title, normalize in titles_options:
    disp = plot_confusion_matrix(clf, X_test, y_test, display_labels=labels, cmap=plt.cm.Blues, normalize=normalize)
    disp.ax_.set_title(title)
    plt.savefig(f"DetectPD_SMOTE_Improved/Plots/{title}.png")
    print(title)
    print(disp.confusion_matrix)

# plotting ROC curve
metrics.plot_roc_curve(clf, X_test, y_test)
plt.plot([0, 1], [0, 1], color='darkorange', lw=2, linestyle='--')
plt.savefig("DetectPD_SMOTE_Improved/Plots/roc_curve.png")
plt.show()
