import pandas as pd
import sklearn
from sklearn.datasets import make_classification
import csv
from collections import Counter
from sklearn.svm import LinearSVC

import writing


def preprocessing_columns(path):

    data = pd.read_csv(path + "data/DetectPD.csv")

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
    y = list(zip(class_type))

    return x, y

X, y = preprocessing_columns("")


from imblearn.over_sampling import RandomOverSampler
ros = RandomOverSampler()
X_resampled, y_resampled = ros.fit_resample(X, y)
print(sorted(Counter(y_resampled).items()))


writing.writing(X_resampled, y_resampled, "RandomOverSampler")


from imblearn.over_sampling import SMOTE, ADASYN
X_resampled, y_resampled = SMOTE().fit_resample(X, y)
print(sorted(Counter(y_resampled).items()))

writing.writing(X_resampled, y_resampled, "SMOTE")

clf_smote = LinearSVC().fit(X_resampled, y_resampled)
X_resampled, y_resampled = ADASYN().fit_resample(X, y)
print(sorted(Counter(y_resampled).items()))

writing.writing(X_resampled, y_resampled, "ADASYN")


# clf_adasyn = LinearSVC().fit(X_resampled, y_resampled)
