import io
import os
import pickle

from PIL import Image, ImageFile

from TestImageBuilder import TestImageBuilder
from User import User
from UserModel import UserModel

ImageFile.LOAD_TRUNCATED_IMAGES = True


class Detector:
    __user: User = None

    def load_features(self, image_no: UserModel):
        img = Image.open(io.BytesIO(image_no.get_test_image()))
        img.save('images/image' + str(image_no.get_id()) + '.jpg')

        # TODO: Run the C++ file.

        # temp testing
        img.save('images/image' + str(image_no.get_id()) + '_pen.jpg')
        img.save('images/image' + str(image_no.get_id()) + '_template.jpg')

        f = open(f"results/RMS{image_no.get_id()}.txt", "w")
        if image_no.get_id() % 2 == 0:
            f.write("1, 3176.216064, 0.000672, 7098.378906, 46569.03516, 21.280848, 224.197754, 0.156795, 802.821106, 0.216138")
        else:
            f.write("2, 4648.249512, 0.02644, 6156.082031, 32504.22266, 19.206491, 191.923462, 0, 678.250366, 0.144092")
        f.close()

        img.close()
        os.remove('images/image' + str(image_no.get_id()) + '.jpg')
        os.remove('images/image' + str(image_no.get_id()) + '_pen.jpg')
        os.remove('images/image' + str(image_no.get_id()) + '_template.jpg')

        feature_file = open("results/RMS" + str(image_no.get_id()) + ".txt", "r")
        features = feature_file.read()
        feature_file.close()
        features = features.split(", ")

        test_image = TestImageBuilder() \
            .set_rms(float(features[1])) \
            .set_std_deviation_st_ht(float(features[2])) \
            .set_max_between_st_ht(float(features[3])) \
            .set_min_between_st_ht(features[4]) \
            .set_mrt(float(features[5])) \
            .set_max_ht(float(features[6])) \
            .set_min_ht(features[7]) \
            .set_std_ht(float(features[8])) \
            .set_changes_from_negative_to_positive_between_st_ht(float(features[9]))\
            .build()

        self.__user = User(
            test_image=test_image,
            age=image_no.get_age(),
            gender=image_no.get_gender(),
            handedness=image_no.get_handedness())
        os.remove("results/RMS" + str(image_no.get_id()) + ".txt")

    def process(self) -> bool:
        result: bool = True

        with open('models/ensemble_classifier.pickle', 'rb') as file:
            ensemble_classifier = pickle.load(file)

        x = [[self.__user.get_gender(), self.__user.get_handedness(), self.__user.get_age(),
              self.__user.get_test_image().get_rms(), self.__user.get_test_image().get_max_ht(),
              self.__user.get_test_image().get_min_ht(), self.__user.get_test_image().get_std_deviation_st_ht(),
              self.__user.get_test_image().get_mrt(), self.__user.get_test_image().get_max_ht(),
              self.__user.get_test_image().get_min_ht(), self.__user.get_test_image().get_std_ht(),
              self.__user.get_test_image().get_changes_from_negative_to_positive_between_st_ht()]]

        y_pred = ensemble_classifier.predict(x)

        if y_pred == 2:
            result = True
        elif y_pred == 1:
            result = False

        return result

    def get_user(self) -> User:
        return self.__user

    def set_user(self, user: User):
        self.__user = user
