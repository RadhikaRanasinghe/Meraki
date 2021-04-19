import os
import pickle

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import plot_confusion_matrix, classification_report
from sklearn.model_selection import train_test_split


def preprocessing(path):
    data = pd.read_csv(f"data/DetectPD{path}.csv")

    # Preprocessing
    gender = list(data['GENDER'])
    handedness = list(data['RIGH/LEFT-HANDED'])
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
    x = list(
        zip(gender, handedness, age, rms, max_st_ht, min_st_ht, std_st_ht, mrt, max_ht, min_ht, std_ht, n_to_p_st_ht))
    y = list(class_type)

    return x, y


def train_voting_classifier(path):
    estimators = []
    for root, directories, files in os.walk(f"models/DetectPD{path}", topdown=False):
        for name in files:
            model = pickle.load(open(os.path.join(root, name), "rb"))
            estimators.append((name, model))

    x, y = preprocessing(path)

    best_model = None
    best_accuracy = 0
    best_x_test = None
    best_y_test = None

    for i in range(1):
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)

        model = VotingClassifier(estimators=estimators, voting='hard')

        model.fit(x_train, y_train)

        model_accuracy = model.score(x_test, y_test)

        if best_accuracy < model_accuracy:
            best_model = model
            best_accuracy = model_accuracy
            best_x_test = x_test
            best_y_test = y_test

    pickle.dump(best_model, open(f"VotingClassifier{path}.pickle", "wb"))

    # Running predictions using  test data
    predictions = best_model.predict(best_x_test)

    # getting accuracy as percentage
    text = classification_report(best_y_test, predictions) + f"\nVotingClassifier accuracy: {best_accuracy}"

    file = open(f"plots/DetectPD{path}/DetectPD{path}_report.txt", "w")
    file.write(text)
    file.close()

    # Creating confusion matrix
    labels = ['negative', 'positive']

    titles_options = [("Confusion matrix, without normalization", None),
                      ("Normalized confusion matrix", 'true')]
    for title, normalize in titles_options:
        disp = plot_confusion_matrix(best_model, best_x_test, best_y_test, display_labels=labels, cmap=plt.cm.Blues,
                                     normalize=normalize)
        disp.ax_.set_title(title)
        plt.savefig(f"plots/DetectPD{path}/DetectPD{path}_{title}.png".replace(" ", "_").replace(",", ""))
