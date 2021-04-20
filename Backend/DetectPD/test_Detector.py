from unittest import TestCase

import cv2

from Detector import Detector
from UserModel import UserModel


class TestDetector(TestCase):
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
        user = UserModel(1, 31, 1, 0, byte_image, 10)
        # Calling the loadFeatures function
        detector.load_features(user)

        # Checking if the User object has been updated properly
        self.assertEqual(detector.get_user().get_handedness(), 0)
        self.assertEqual(detector.get_user().get_gender(), 1)
        self.assertEqual(detector.get_user().get_age(), 31)

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
        user = UserModel(1, 31, 1, 0, byte_image, 10)
        # Calling the loadFeatures function
        detector.load_features(user)
        # Getting the result
        result = detector.process()
        # Checking if the result is correct or not
        self.assertEqual(result, False)
