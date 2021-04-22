import matplotlib.pyplot as plt
import sklearn
import sklearn.metrics as metrics
from sklearn.metrics import plot_confusion_matrix, accuracy_score

import methods

path = ""

# dataset_type = ""
# dataset_type = "_SMOTE"
# dataset_type = "_RandomOverSampler"
# dataset_type = "_ADASYN"
dataset_type = "_SMOTE_improved"

clf, data = methods.find_highest_accuracy_model(path, dataset_type)

print(data.keys())

# Adding the split data into classifier
clf.fit(data['x_train'], data['y_train'])

# Running predictions using  test data
predictions = clf.predict(data['x_test'])

# getting accuracy as percentage
accuracy = accuracy_score(data['y_test'], predictions) * 100
message = sklearn.metrics.classification_report(data['y_test'], predictions) + f"\nAccuracy: {accuracy}"

file = open(f"diagrams/DetectPD{dataset_type}/DetectPD{dataset_type}_Results.txt", "w")
file.write(message)
file.close()

# Creating confusion matrix
labels = ['negative', 'positive']

titles_options = [("Confusion matrix, without normalization", None),
                  ("Normalized confusion matrix", 'true')]
for title, normalize in titles_options:
    disp = plot_confusion_matrix(clf, data['x_test'], data['y_test'], display_labels=labels, cmap=plt.cm.Blues,
                                 normalize=normalize)
    disp.ax_.set_title(title)
    plt.savefig(f"diagrams/DetectPD{dataset_type}/DetectPD{dataset_type}_{title}.png".replace(" ", "_").replace(",", ""))

# plotting ROC curve
metrics.plot_roc_curve(clf, data['x_test'], data['y_test'])
plt.plot([0, 1], [0, 1], color='darkorange', lw=2, linestyle='--')
plt.savefig(f"diagrams/DetectPD{dataset_type}/DetectPD{dataset_type}_roc_curve.png")
