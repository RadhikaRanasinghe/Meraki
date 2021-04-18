import os

import cv2
import pandas as pd

import writing
from extractFeats import extractFeats
from extractPen import extractPen

AMIRU = 'amiru'
BAWANTHA = 'bawantha'
CHANAKA = 'chanaka'
CHARINDU = 'charindu'
MALITH = 'malith'
RADHIKA = 'radhika'


def convert(user):

    isUserCorrect = True

    gender = []
    handedness = []
    age = []
    class_type = []
    image_name = []
    rms = []
    max_st_ht = []
    min_st_ht = []
    std_st_ht = []
    mrt = []
    max_ht = []
    min_ht = []
    std_ht = []
    n_to_p_st_ht = []

    count = 0

    path = 'handpd_images/' + user

    if user == AMIRU or user == CHANAKA:
        data = pd.read_csv("handpd_csv/NewMeander.csv")
        for root, directories, files in os.walk(path, topdown=False):
            for name in files:
                print(os.path.join(root, name))
                image_name.append(name)

                img = cv2.imread(os.path.join(root, name))
                print("\tImage Loaded.")
                img = cv2.resize(img, (600, 600))
                print("\tImage Resized.")

                img_pen = extractPen(img)
                print("\tPen Created.")
                print("\tFeature extraction started.")
                test_image = extractFeats(img, img_pen)
                print("\tFeature extraction completed.")

                rms.append(test_image.get_rms())
                max_st_ht.append(test_image.get_max_between_st_ht())
                min_st_ht.append(test_image.get_min_between_st_ht())
                std_st_ht.append(test_image.get_std_deviation_st_ht())
                mrt.append(test_image.get_mrt())
                max_ht.append(test_image.get_max_ht())
                min_ht.append(test_image.get_min_ht())
                std_ht.append(test_image.get_std_ht())
                n_to_p_st_ht.append(test_image.get_changes_from_negative_to_positive_between_st_ht())

                print("\tImage Details finding started.")
                for index, row in data.iterrows():
                    if row[1][row[1].find("-") + 1:row[1].find(".")] == name[name.find("-") + 1:name.find(".")]:
                        if row['GENDER'] == "M":
                            gender.append(1)
                        elif row['GENDER'] == "F":
                            gender.append(2)
                        else:
                            print("ERROR - Unidentified Gender. Contact Charindu :(")

                        if row['RIGH/LEFT-HANDED'] == "R":
                            handedness.append(1)
                        elif row['RIGH/LEFT-HANDED'] == "L":
                            handedness.append(2)
                        else:
                            print("ERROR - Unidentified Handedness. Contact Charindu :(")

                        age.append(row['AGE'])
                        class_type.append(row['CLASS_TYPE'])

                        count += 1
                        print("\tImage Details found.")
                        break

    elif user == BAWANTHA or user == CHARINDU or user == MALITH or user == RADHIKA:
        data = pd.read_csv("handpd_csv/Meander_HandPD.csv")
        for root, directories, files in os.walk(path, topdown=False):
            for name in files:
                print(os.path.join(root, name))
                image_name.append(name)

                img = cv2.imread(os.path.join(root, name))
                print("\tImage Loaded.")
                img = cv2.resize(img, (600, 600))
                print("\tImage Resized.")

                img_pen = extractPen(img)
                print("\tPen Created.")
                print("\tFeature extraction started.")
                test_image = extractFeats(img, img_pen)
                print("\tFeature extraction completed.")

                rms.append(test_image.get_rms())
                max_st_ht.append(test_image.get_max_between_st_ht())
                min_st_ht.append(test_image.get_min_between_st_ht())
                std_st_ht.append(test_image.get_std_deviation_st_ht())
                mrt.append(test_image.get_mrt())
                max_ht.append(test_image.get_max_ht())
                min_ht.append(test_image.get_min_ht())
                std_ht.append(test_image.get_std_ht())
                n_to_p_st_ht.append(test_image.get_changes_from_negative_to_positive_between_st_ht())

                print("\tImage Details finding started.")
                for index, row in data.iterrows():
                    if row[1][:4] == name[:4]:
                        if row['GENDER'] == "M":
                            gender.append(1)
                        elif row['GENDER'] == "F":
                            gender.append(2)
                        else:
                            print("ERROR - Unidentified Gender. Contact Charindu :(")

                        if row['RIGH/LEFT-HANDED'] == "R":
                            handedness.append(1)
                        elif row['RIGH/LEFT-HANDED'] == "L":
                            handedness.append(2)
                        else:
                            print("ERROR - Unidentified Handedness. Contact Charindu :(")

                        age.append(row['AGE'])
                        class_type.append(row['CLASS_TYPE'])

                        count += 1
                        print("\tImage Details found.")
                        print("IMAGE NO: " + str(count))
                        break
    else:
        isUserCorrect = False
        print("Invalid User, Ask Charindu why he thinks your parents are blood related -_-")

    if isUserCorrect:
        print("Combining the data...")
        x = list(zip(image_name, gender, handedness, age, rms, max_st_ht, min_st_ht, std_st_ht, mrt, max_ht,
                     min_ht, std_ht, n_to_p_st_ht))
        y = list(class_type)

        if user == AMIRU or user == CHANAKA:
            if count == len(x) == len(y) == 132:
                print("Combined successful.")
            else:
                print("ERROR - Expected 132 rows, " + str(count) + " found. Contact Charindu :(")
        else:
            if count == len(x) == len(y) == 92:
                print("Combined successful.")
            else:
                print("ERROR - Expected 92 rows, " + str(count) + " found. Contact Charindu :(")

        print("writing csv file...")
        writing.writing(x, y, "_" + user, True)
        print("csv file complete. Contact Charindu :)")
