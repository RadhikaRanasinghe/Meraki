import sklearn
from sklearn.model_selection import train_test_split

import pickle
import pandas as pd
import numpy as np
from sklearn.ensemble import VotingClassifier
from sklearn import preprocessing


def loading_pickle(load_location):
    with open(load_location, 'rb') as file:
        loaded_pickle_file = pickle.load(file)
    return loaded_pickle_file


# clf_log_reg = loading_pickle("Models/LogisticRegression/highModel.pickle")
#
# clf_lda = loading_pickle("Models/LDA/LDA_highModel.pickle")
#
# clf_gnb = loading_pickle("Models/NaiveBayes/naive_bayes.pickle")


clf_lda = loading_pickle("Models/LDA_result.pickle")
clf_log_r = loading_pickle("Models/LogR_first.pickle")
clf_svm = loading_pickle("Models/SVM.pickle")

data = pd.read_csv("Dataset/DetectPD.csv")

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

x = np.array(x)
y = np.array(y)

# ensemble_clf = VotingClassifier(estimators=[('knn1', clf_knn1),
#                                             ('knn2', clf_knn2),
#                                             ('knn3', clf_knn3)],
#                                 voting='soft', weights=[69, 67, 74], flatten_transform=True)

ensemble_clf = VotingClassifier(estimators=[('lda', clf_lda),
                                            ('logr', clf_log_r),
                                            ('svm', clf_svm)
                                            ],
                                voting='hard')

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)

ensemble_clf.fit(x, y)

ensemble_accu = ensemble_clf.score(x_test, y_test)
print(ensemble_accu * 100)

best_result1_file = "VC_BestModel1.pickle"
best_result2_file = "VC_BestModel2.pickle"
best_result3_file = "VC_BestModel3.pickle"
worst_result_file = "VC_WorstModel.pickle"

best_result1 = 0
best_result2 = 0
best_result3 = 0
worst_result = 100
acc = 0
hundred_count = 0

# for i in range(10000):
#     x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)
#     model = VotingClassifier(estimators=[('knn1', clf_knn1),
#                                          ('knn5', clf_knn5),
#                                          ('knn9', clf_knn9),
#                                          ('knn13', clf_knn13),
#                                          ('knn14', clf_knn14)
#                                          ],
#                              voting='hard')
#     model.fit(x_train, y_train)
#     predicted = model.predict(x_test)
#
#     acc = model.score(x_test, y_test) * 100
#     print(model.score(x_test, y_test) * 100)
#
#     if acc == 100:
#         hundred_count += 1
#
#     if acc < worst_result:
#         with open(worst_result_file, 'wb') as file:
#             pickle.dump(model, file)
#         worst_result = acc
#
#     if acc > best_result1 or acc > best_result2 or acc > best_result3:
#         if acc > best_result1:
#             best_result1 = acc
#             with open(best_result1_file, 'wb') as file:
#                 pickle.dump(model, file)
#
#         elif acc > best_result2:
#             best_result2 = acc
#             with open(best_result2_file, 'wb') as file:
#                 pickle.dump(model, file)
#
#         else:
#             best_result3 = acc
#             with open(best_result3_file, 'wb') as file:
#                 pickle.dump(model, file)
#
# print("Best result A", best_result1, "Best result B", best_result2, "Best results C", best_result3)
# print("Worst Result", worst_result)
# print("num of hundreds", hundred_count)
#
with open('log_r_and_lda_svm.pickle', 'wb') as file:
    pickle.dump(ensemble_clf, file)
