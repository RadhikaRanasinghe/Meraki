import csv
from collections import Counter

import pandas as pd
import sklearn
from imblearn.over_sampling import RandomOverSampler, SMOTE, ADASYN


def writing(x, y, oversample_type):
    # field names
    fields = ['GENDER', 'RIGH/LEFT-HANDED', 'AGE', 'RMS', 'MAX_BETWEEN_ST_HT', 'MIN_BETWEEN_ST_HT',
              'STD_DEVIATION_ST_HT',
              'MRT', 'MAX_HT', 'MIN_HT', 'STD_HT', 'CHANGES_FROM_NEGATIVE_TO_POSITIVE_BETWEEN_ST_HT', 'CLASS_TYPE']

    # data rows of csv file
    rows = []

    for i in range(len(x)):
        row = list(x[i])
        row.append(int(y[i]))
        rows.append(dict(zip(fields, row)))

    # name of csv file
    filename = "detectpd_csv/DetectPD_" + str(oversample_type) + ".csv"

    # writing to csv file
    with open(filename, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.DictWriter(csvfile, fieldnames=fields)

        # writing the fields
        csvwriter.writeheader()

        # writing the data rows
        csvwriter.writerows(rows)


def preprocessing_columns(path):
    data = pd.read_csv(path)

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


def create_oversampling(source_path):
    x, y = preprocessing_columns(source_path)
    ros = RandomOverSampler()
    X_resampled, y_resampled = ros.fit_resample(x, y)
    print(sorted(Counter(y_resampled).items()))

    writing(X_resampled, y_resampled, "RandomOverSampler")

    X_resampled, y_resampled = SMOTE().fit_resample(x, y)
    print(sorted(Counter(y_resampled).items()))

    writing(X_resampled, y_resampled, "SMOTE")

    X_resampled, y_resampled = ADASYN().fit_resample(x, y)
    print(sorted(Counter(y_resampled).items()))

    writing(X_resampled, y_resampled, "ADASYN")
