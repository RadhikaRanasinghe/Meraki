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


def naive_bayes_roc():
    # hand_pd = pd.read_csv("Datasets/DetectPD.csv")
    # hand_pd = pd.read_csv("Datasets/DetectPD-ADASYN.csv")
    hand_pd = pd.read_csv("Backend/Data/detectpd_csv/DetectPD_RandomOverSampler.csv")
    # hand_pd = pd.read_csv("Datasets/DetectPD-SMOTE.csv")

    # preprocessing columns
    gender = list(hand_pd['GENDER'])
    handedness = (list(hand_pd['RIGH/LEFT-HANDED']))
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

    """
        train_test_split() parameters: dependent variable, independent variable, test size as 10% 
        random_state set to None which means train_test_split() will return different result each execution
        if random_state set to integer, train_test_split() will return same result each execution
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=None)

# ----------------------------------------------------------------------------------------------------------------- #
    # Loading model from pickle file
    pickle_in = open("Backend/Models/NaiveBayes/DetectPD-RandomOverSampler/ROS_BestModel_5.pickle", "rb")
    loadedModel = pickle.load(pickle_in)

    # plot ROC curve
    metrics.plot_roc_curve(loadedModel, X_test, y_test)
    plt.show()
# ----------------------------------------------------------------------------------------------------------------- #


naive_bayes_roc()

