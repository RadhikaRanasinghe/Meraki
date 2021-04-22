import pickle
import pickle

import matplotlib.pyplot as plt
import sklearn.metrics as metrics
from sklearn.metrics import plot_confusion_matrix
from sklearn.model_selection import train_test_split

import methods

path = ""

dataset_type = ""
# dataset_type = "_SMOTE"
# dataset_type = "_RandomOverSampler"
# dataset_type = "_ADASYN"
# dataset_type = "_SMOTE_improved"

# pd_data = pd.read_csv('Data/DetectPD.csv')
clf = methods.find_highest_accuracy_model(path, dataset_type)


X, y = methods.preprocessing_columns(path, dataset_type)

# splitting data into testing data and training data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

# Adding the split data into classifier
clf.fit(X_train, y_train)

# Running predictions using  test data
predictions = clf.predict(X_test)

# Creating confusion matrix
labels = ['negative', 'positive']

titles_options = [("Confusion matrix, without normalization", None),
                  ("Normalized confusion matrix", 'true')]
for title, normalize in titles_options:
    disp = plot_confusion_matrix(clf, X_test, y_test, display_labels=labels, cmap=plt.cm.Blues, normalize=normalize)
    disp.ax_.set_title(title)
    plt.savefig(f"plots/DetectPD{dataset_type}/DetectPD{dataset_type}_{title}.png".replace(" ", "_").replace(",", ""))
    # print(title)
    # print(disp.confusion_matrix)

# plotting ROC curve
metrics.plot_roc_curve(clf, X_test, y_test)
plt.savefig(f"plots/DetectPD{dataset_type}/DetectPD{dataset_type}_roc_curve.png")
