# Python program to demonstrate
# writing to CSV


import csv


def writing(X, y, type):
    # field names
    fields = ['GENDER', 'RIGH/LEFT-HANDED', 'AGE', 'RMS', 'MAX_BETWEEN_ST_HT', 'MIN_BETWEEN_ST_HT', 'STD_DEVIATION_ST_HT',
              'MRT', 'MAX_HT', 'MIN_HT', 'STD_HT', 'CHANGES_FROM_NEGATIVE_TO_POSITIVE_BETWEEN_ST_HT', 'CLASS_TYPE']

    # data rows of csv file
    rows = []

    for i in range(len(X)):
        row = list(X[i])
        row.append(int(y[i]))
        rows.append(dict(zip(fields, row)))

    # name of csv file
    filename = "DetectPD-" + str(type) + ".csv"

    # writing to csv file
    with open(filename, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.DictWriter(csvfile, fieldnames=fields)

        # writing the fields
        csvwriter.writeheader()

        # writing the data rows
        csvwriter.writerows(rows)
