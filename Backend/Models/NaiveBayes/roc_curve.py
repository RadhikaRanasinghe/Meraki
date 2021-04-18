""" Receiver Operating Characteristic (ROC) """

import numpy as np
import pandas as pd
import sklearn
import pickle
import sklearn.preprocessing
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import plot_confusion_matrix, auc, roc_curve, roc_auc_score
from sklearn.naive_bayes import GaussianNB


def roc_curve():
    """This method plots the ROC curve of the true positives for the Naives Bayes
    classifier model. auc, roc_curve, roc_auc_score is used from metrics is used."""

    # hand_pd = pd.read_csv("Datasets/DetectPD.csv")
    # hand_pd = pd.read_csv("Datasets/DetectPD-ADASYN.csv")
    hand_pd = pd.read_csv("Datasets/DetectPD-RandomOverSampler.csv")
    # hand_pd = pd.read_csv("Datasets/DetectPD-SMOTE.csv")

    # plot graph
    sns.countplot(x="CLASS_TYPE", data=hand_pd)
    plt.show()

    # # drop redundant column - ONLY FOR DetectPD.csv
    # hand_pd.drop("IMAGE_NAME", axis=1, inplace=True)
    # hand_pd.drop("_ID_EXAM", axis=1, inplace=True)

    # # preprocessing columns using label encoders
    le = sklearn.preprocessing.LabelEncoder()
    gender = le.fit_transform(list(hand_pd['GENDER']))
    handedness = le.fit_transform(list(hand_pd['RIGH/LEFT-HANDED']))
    age = list(hand_pd['AGE'])
    rms = list(hand_pd['RMS'])
    max_st_ht = list(hand_pd['MAX_BETWEEN_ST_HT'])
    min_st_ht = list(hand_pd['MIN_BETWEEN_ST_HT'])
    std_st_ht = list(hand_pd['STD_DEVIATION_ST_HT'])
    mrt = list(hand_pd['MRT'])
    max_ht = list(hand_pd['MAX_HT'])
    min_ht = list(hand_pd['MIN_HT'])
    std_ht = list(hand_pd['STD_HT'])
    n_to_p_st_ht = list(hand_pd['CHANGES_FROM_NEGATIVE_TO_POSITIVE_BETWEEN_ST_HT'])
    class_type = list(hand_pd['CLASS_TYPE'])

    # Creating 'x' and 'y'
    X = list(
        zip(gender, handedness, age, rms, max_st_ht, min_st_ht, std_st_ht, mrt, max_ht, min_ht, std_ht, n_to_p_st_ht))
    y = list(class_type)

    X = np.array(X)
    y = np.array(y)

    # Total instances
    print("# Total = " + str(len(hand_pd.index)))
    print(hand_pd.head(10))

    """
        train_test_split() parameters: dependent variable, independent variable, test size as 10% 
        random_state set to None which means train_test_split() will return different result each execution
        if random_state set to integer, train_test_split() will return same result each execution
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=None)

    y_true = []
    for _ in range(len(y_test)):
        if _ == 1:
            y_true.append(0)
        else:
            y_true.append(1)

    # generate a no skill prediction (majority class)
    ns_probs = [0 for _ in range(len(y_test))]

    # ----------------------------------------------------------------------------------------------------------------- #

    # Loading model from pickle file
    pickle_in = open("ROS/ROS_GNB_BestModel_5.pickle", "rb")
    loadedModel = pickle.load(pickle_in)
    new_pred = loadedModel.predict(X_test)
    new_score = metrics.accuracy_score(y_test, new_pred)

    # ----------------------------------------------------------------------------------------------------------------- #

    # ROC curve
    # keep probabilities for the positive outcome only
    lr_probs = loadedModel.predict_proba(X_test)
    lr_probs = lr_probs[:, 1]

    # calculate scores
    ns_auc = roc_auc_score(y_true, ns_probs)
    lr_auc = roc_auc_score(y_true, lr_probs)

    # summarize scores
    print('0: ROC AUC=%.3f' % ns_auc)
    print('1: ROC AUC=%.3f' % lr_auc)

    # calculate roc curves
    ns_fpr, ns_tpr, _ = roc_curve(y_true, ns_probs)
    lr_fpr, lr_tpr, _ = roc_curve(y_true, lr_probs)

    # plot the roc curve for the model
    plt.plot(ns_fpr, ns_tpr, linestyle='--', label='0')
    plt.plot(lr_fpr, lr_tpr, marker='.', label='1')

    # axis labels
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')

    # show the legend
    plt.legend()

    # show the plot
    plt.show()

    # print prediction score
    print(new_score * 100)


roc_curve()

