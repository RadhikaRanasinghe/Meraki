import numpy as np
import pandas as pd
import sklearn
import pickle
import sklearn.preprocessing
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB


def naive_bayes_classifier():
    """ Method used to create and train Machine Learning model using Naive Bayes classifier.
    This method utilizes four datasets to train the models."""

    # four datasets used to train the models
    hand_pd = pd.read_csv("Datasets/DetectPD.csv")
    # hand_pd = pd.read_csv("Datasets/DetectPD-ADASYN.csv")
    # hand_pd = pd.read_csv("Datasets/DetectPD-RandomOverSampler.csv")
    # hand_pd = pd.read_csv("Datasets/DetectPD-SMOTE.csv")
    hand_pd.head(10)

    # plot graph
    sns.countplot(x="CLASS_TYPE", data=hand_pd)
    plt.show()

    # drop redundant column - ONLY FOR DetectPD.csv
    hand_pd.drop("IMAGE_NAME", axis=1, inplace=True)
    hand_pd.drop("_ID_EXAM", axis=1, inplace=True)

    # preprocessing columns
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

    # Naive Bayes Classifier
    lowestModel = 0
    highestModel = 0
    lowestScore = 0
    highestScore = 0
    highCount = 0

    # fit model in 10,000 iterations
    for i in range(10000):
        """
            train_test_split() parameters: dependent variable, independent variable, test size as 10% 
            random_state set to None which means train_test_split() will return different result each execution
            if random_state set to integer, train_test_split() will return same result each execution
        """
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=None) # train_test_split with test size as 0.1 and train size as 0.9

        model = GaussianNB()  # Gaussian Naive Bayes function

        model.fit(X_train, y_train)  # fit model - train the model

        predicted = model.predict(X_test)  # Y_pred

        score = metrics.accuracy_score(y_test, predicted)
        print(score * 100)

        # first iteration
        if i == 0:
            lowestModel = model
            highestModel = model
            lowestScore = score
            highestScore = score
        else:
            if score < lowestScore:
                lowestScore = score
                lowestModel = model # assign the low accuracy model

                print(metrics.classification_report(y_test, predicted))
                print(metrics.confusion_matrix(y_test, predicted))

            elif score > highestScore:
                highestScore = score
                highestModel = model # assign the high accuracy model
                highCount += 1

                print(metrics.classification_report(y_test, predicted))
                print(metrics.confusion_matrix(y_test, predicted))

                # Saving models as pickle files
                with open("GNB_BestModel_%s.pickle" % highCount, "wb") as bestModel:
                    pickle.dump(highestModel, bestModel)

    # Saving models as pickle files
    with open("GNB_WorstModel.pickle", "wb") as worstModel:
        pickle.dump(lowestModel, worstModel)


naive_bayes_classifier()
