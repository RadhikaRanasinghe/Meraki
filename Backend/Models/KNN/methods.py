import pickle

import pandas as pd

import sklearn
from sklearn.neighbors import KNeighborsClassifier


def print_results(path):
    # Printing results

    f = open("KNN_results.md", "w")
    text = "## All Records\n"
    header = "# KNN Results\n\n## Summarization\n\n"
    highest_best = {'name': "name", 'best': 0, 'worst': 100, 'difference': 100}
    lowest_worst = {'name': "name", 'best': 0, 'worst': 100, 'difference': 100}
    lowest_deference = {'name': "name", 'best': 0, 'worst': 100, 'difference': 100}

    for neighbors in range(3, 10, 2):
        for test_size in range(1, 5, 1):
            loaded_best_model = pickle.load(open(
                str(path) + "models/KNN_BestModel_n(" + str(neighbors) + ")_size(" + str(test_size / 10) + ").pickle",
                "rb"))
            loaded_best_data = pickle.load(
                open(path + "models/KNN_BestData_n(" + str(neighbors) + ")_size(" + str(test_size / 10) + ").pickle",
                     "rb"))
            best_model = loaded_best_model.fit(loaded_best_data['x_train'], loaded_best_data['y_train'])
            best_acc = best_model.score(loaded_best_data['x_test'], loaded_best_data['y_test'])

            loaded_worst_model = pickle.load(
                open(path + "models/KNN_WorstModel_n(" + str(neighbors) + ")_size(" + str(test_size / 10) + ").pickle",
                     "rb"))
            loaded_worst_data = pickle.load(
                open(path + "models/KNN_WorstData_n(" + str(neighbors) + ")_size(" + str(test_size / 10) + ").pickle",
                     "rb"))
            worst_model = loaded_worst_model.fit(loaded_worst_data['x_train'], loaded_worst_data['y_train'])
            worst_acc = worst_model.score(loaded_worst_data['x_test'], loaded_worst_data['y_test'])

            deference = best_acc * 100 - worst_acc * 100

            name = "### neighbors: " + str(neighbors) + ", test size: " + str(test_size / 10)

            msg = "\n" + name + "\n\n\tBest\t\t: " + str(best_acc * 100) + "\n\tWorst\t\t: " +\
                  str(worst_acc * 100) + "\n\tDeference\t: " + str(deference) + "\n "

            print(msg.replace('#', ""))

            if highest_best['best'] < best_acc:
                highest_best = {'name': name, 'best': best_acc, 'worst': worst_acc, 'difference': deference}
            if lowest_worst['worst'] > worst_acc:
                lowest_worst = {'name': name, 'best': best_acc, 'worst': worst_acc, 'difference': deference}
            if lowest_deference['difference'] > deference:
                lowest_deference = {'name': name, 'best': best_acc, 'worst': worst_acc, 'difference': deference}

            text += msg

    header += "### The Highest Best\n\n>#" + str(highest_best['name']) + "\n>> - **Best\t\t: "\
              + str(highest_best['best']*100) + "**\n>> - worst\t\t: " + str(highest_best['worst']*100)\
              + "\n>> - deference\t: " + str(highest_best['difference']) + "\n\n"

    header += "### The Lowest Worst\n\n>#" + str(lowest_worst['name']) + "\n>> - Best\t\t: "\
              + str(lowest_worst['best']*100) + "\n>> - **worst\t: " + str(lowest_worst['worst']*100)\
              + "**\n>> - deference\t: " + str(lowest_worst['difference']) + "\n\n"

    header += "### The Lowest difference\n\n>#" + str(lowest_deference['name']) + "\n>> - Best\t\t\t: "\
              + str(lowest_deference['best']*100) + "\n>> - worst\t\t\t: " + str(lowest_deference['worst']*100)\
              + "\n>> - **deference\t: " + str(lowest_deference['difference']) + "**\n\n"

    f.write(header + text)
    f.close()


def initialise_save(path, x, y):
    # Initializing all save
    for neighbors in range(3, 10, 2):
        for ts in range(1, 5, 1):
            test_size = ts / 10

            x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=test_size)
            model = KNeighborsClassifier(n_neighbors=neighbors)
            model.fit(x_train, y_train)
            acc = model.score(x_test, y_test)

            data = {'x_train': x_train, 'x_test': x_test, 'y_train': y_train, 'y_test': y_test}

            # print("first best saved")
            pickle.dump(data,
                        open(path + "models/KNN_BestData_n(" + str(neighbors) + ")_size(" + str(test_size) + ").pickle",
                             "wb"))
            pickle.dump(model,
                        open(path + "models/KNN_BestModel_n(" + str(neighbors) + ")_size(" + str(test_size) + ").pickle",
                             "wb"))

            # print("first worst saved")
            pickle.dump(data,
                        open(path + "models/KNN_WorstData_n(" + str(neighbors) + ")_size(" + str(test_size) + ").pickle",
                             "wb"))
            pickle.dump(model, open(
                path + "models/KNN_WorstModel_n(" + str(neighbors) + ")_size(" + str(test_size) + ").pickle", "wb"))


def building_models(path, x, y):
    # Running every model for 10,000 itterrations
    for neighbors in range(3, 10, 2):
        for ts in range(1, 5, 1):
            for _ in range(10000):

                test_size = ts / 10

                x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=test_size)
                model = KNeighborsClassifier(n_neighbors=neighbors)
                model.fit(x_train, y_train)
                acc = model.score(x_test, y_test)
                spec = (neighbors, test_size, _, acc * 100)

                loaded_best_model = pickle.load(open(
                    str(path) + "models/KNN_BestModel_n(" + str(neighbors) + ")_size(" + str(test_size) + ").pickle",
                    "rb"))
                loaded_best_data = pickle.load(
                    open(path + "models/KNN_BestData_n(" + str(neighbors) + ")_size(" + str(test_size) + ").pickle",
                         "rb"))
                best_model = loaded_best_model.fit(loaded_best_data['x_train'], loaded_best_data['y_train'])
                best_acc = best_model.score(loaded_best_data['x_test'], loaded_best_data['y_test'])

                loaded_worst_model = pickle.load(
                    open(path + "models/KNN_WorstModel_n(" + str(neighbors) + ")_size(" + str(test_size) + ").pickle",
                         "rb"))
                loaded_worst_data = pickle.load(
                    open(path + "models/KNN_WorstData_n(" + str(neighbors) + ")_size(" + str(test_size) + ").pickle",
                         "rb"))
                worst_model = loaded_worst_model.fit(loaded_worst_data['x_train'], loaded_worst_data['y_train'])
                worst_acc = worst_model.score(loaded_worst_data['x_test'], loaded_worst_data['y_test'])

                if acc > best_acc:
                    print("best saved", spec)
                    data = {'x_train': x_train, 'x_test': x_test, 'y_train': y_train, 'y_test': y_test}
                    pickle.dump(data, open(
                        path + "models/KNN_BestData_n(" + str(neighbors) + ")_size(" + str(test_size) + ").pickle",
                        "wb"))
                    pickle.dump(model, open(
                        path + "models/KNN_BestModel_n(" + str(neighbors) + ")_size(" + str(test_size) + ").pickle",
                        "wb"))
                if acc < worst_acc:
                    print("worst saved", spec)
                    data = {'x_train': x_train, 'x_test': x_test, 'y_train': y_train, 'y_test': y_test}
                    pickle.dump(data, open(
                        path + "models/KNN_WorstData_n(" + str(neighbors) + ")_size(" + str(test_size) + ").pickle",
                        "wb"))
                    pickle.dump(model, open(
                        path + "models/KNN_WorstModel_n(" + str(neighbors) + ")_size(" + str(test_size) + ").pickle",
                        "wb"))


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
    y = list(class_type)

    return x, y


