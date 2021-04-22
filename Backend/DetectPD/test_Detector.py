import unittest

import cv2

from Detector import Detector
from UserModel import UserModel


class TestDetector(unittest.TestCase):
    """
    This class unit tests the Detector class
    """

    def test_load_features(self):
        """
        This function is used to test if the User object is updated properly
        """

        # Creating an Detector object
        detector = Detector()
        im = cv2.imread('sample_images/exam_1.jpg')
        is_success, im_buf_arr = cv2.imencode(".jpg", im)
        byte_image = im_buf_arr.tobytes()

        # Creating the UserModel object
        user = UserModel(5, 31, 1, 1, byte_image, 10)

        # Calling the loadFeatures function
        detector.load_features(user)

        # Checking if the User object has been updated properly
        self.assertEqual(1, detector.get_user().get_handedness(), "Incorrect value - handedness")
        self.assertEqual(1, detector.get_user().get_gender(), "Incorrect value - gender")
        self.assertEqual(31, detector.get_user().get_age(), "Incorrect value - age")

    def test_process(self):
        """
        This function is used to test if prediction returned is correct or not
        """

        # Creating an Detector object
        detector = Detector()
        im = cv2.imread('sample_images/exam_1.jpg')
        is_success, im_buf_arr = cv2.imencode(".jpg", im)
        byte_image = im_buf_arr.tobytes()

        # Creating the UserModel object
        user = UserModel(5, 31, 1, 0, byte_image, 10)

        # Calling the loadFeatures function
        detector.load_features(user)

        # Getting the result
        result = detector.process()

        # Checking if the result is correct or not
        self.assertEqual(bool, type(result), "Testing result type.")


if __name__ == '__main__':
    unittest.main()
