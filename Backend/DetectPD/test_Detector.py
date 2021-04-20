import cv2
from unittest import TestCase
from mysql_connection import select_record_test
from Detector import Detector
from UserModel import UserModel
from User import User


class TestDetector(TestCase):
    # __user = select_record_test(10)

    # detector = Detector()

    def test_load_features(self):
        
        detector = Detector()
        im = cv2.imread('images/exam_1_pen.jpg')
        is_success, im_buf_arr = cv2.imencode(".jpg", im)
        byte_image = im_buf_arr.tobytes()
        user = UserModel(1, 31, 1, 0, byte_image, 10)
        detector.load_features(user)

        self.assertEqual(detector.get_user().get_handedness(), 0)
        self.assertEqual(detector.get_user().get_gender(), 1)
        self.assertEqual(detector.get_user().get_age(), 31)

 