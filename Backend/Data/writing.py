import csv
from collections import Counter

import pandas as pd
from imblearn.over_sampling import RandomOverSampler, SMOTE, ADASYN


def combine_personal_datasets():
    amiru = pd.read_csv("detectpd_csv/personal/DetectPD_amiru.csv")
    bawantha = pd.read_csv("detectpd_csv/personal/DetectPD_bawantha.csv")
    chanaka = pd.read_csv("detectpd_csv/personal/DetectPD_chanaka.csv")
    charindu = pd.read_csv("detectpd_csv/personal/DetectPD_charindu.csv")
    malith = pd.read_csv("detectpd_csv/personal/DetectPD_malith.csv")
    radhika = pd.read_csv("detectpd_csv/personal/DetectPD_radhika.csv")

    detectpd = amiru.append(bawantha).append(chanaka).append(charindu).append(malith).append(radhika)

    x, y = preprocessing_columns(detectpd, True)

    writing(x, y, "", False)


def writing(x, y, oversample_type, is_dataset_creation):
    # field names
    if is_dataset_creation:
        fields = ['IMAGE_NAME', 'GENDER', 'RIGH/LEFT-HANDED', 'AGE', 'RMS', 'MAX_BETWEEN_ST_HT', 'MIN_BETWEEN_ST_HT',
                  'STD_DEVIATION_ST_HT',
                  'MRT', 'MAX_HT', 'MIN_HT', 'STD_HT', 'CHANGES_FROM_NEGATIVE_TO_POSITIVE_BETWEEN_ST_HT', 'CLASS_TYPE']
    else:
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
    if is_dataset_creation:
        filename = "detectpd_csv/personal/DetectPD" + str(oversample_type) + ".csv"
    else:
        filename = "detectpd_csv/DetectPD" + str(oversample_type) + ".csv"

    # writing to csv file
    with open(filename, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.DictWriter(csvfile, fieldnames=fields)

        # writing the fields
        csvwriter.writeheader()

        # writing the data rows
        csvwriter.writerows(rows)


def preprocessing_columns(data, is_dataset_creation):
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
    x = list(zip(gender, handedness, age, rms, max_st_ht, min_st_ht, std_st_ht, mrt, max_ht, min_ht, std_ht,
                 n_to_p_st_ht))

    if is_dataset_creation:
        y = list(class_type)
    else:
        y = list(zip(class_type))

    return x, y


def create_oversampling(source_path):
    data = pd.read_csv(source_path)
    x, y = preprocessing_columns(data, False)

    ros = RandomOverSampler()
    X_resampled, y_resampled = ros.fit_resample(x, y)
    print(sorted(Counter(y_resampled).items()))
    writing(X_resampled, y_resampled, "_RandomOverSampler", False)

    X_resampled, y_resampled = SMOTE().fit_resample(x, y)
    print(sorted(Counter(y_resampled).items()))
    writing(X_resampled, y_resampled, "_SMOTE", False)

    X_resampled, y_resampled = ADASYN().fit_resample(x, y)
    print(sorted(Counter(y_resampled).items()))
    writing(X_resampled, y_resampled, "_ADASYN", False)
