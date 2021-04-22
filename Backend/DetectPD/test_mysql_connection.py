import unittest

import cv2

import mysql_connection as conn
from UserModel import UserModel


class MysqlConnectionTest(unittest.TestCase):
    """
    Class to test mysql_connection.
    """

    def test_insert_values_test(self):
        """
        Method to test insert_values_test method in mysql_connection.
        """

        # Loading the image and converting it to a byte string.
        im = cv2.imread("sample_images/exam_1.jpg")
        is_success, im_buf_arr = cv2.imencode(".jpg", im)
        byte_im = im_buf_arr.tobytes()

        # Testing Correct instance--------------------------------------------------------------------------------------
        result = conn.insert_values_test(age=20, gender=1, handedness=1, image=byte_im)
        self.assertEqual(type(result), int, "Checking output type.")
        self.assertNotEqual(result, 0, "Incorrect database record id.")

        # Testing error handling - Incorrect data type------------------------------------------------------------------
        # Incorrect data type for 'age'.
        result = conn.insert_values_test(age="20", gender=1, handedness=1, image=byte_im)
        self.assertEqual(0, result, "Incorrect data type - age.")

        # Incorrect data type for 'gender'.
        result = conn.insert_values_test(age=20, gender="1", handedness=1, image=byte_im)
        self.assertEqual(0, result, "Incorrect data type - gender.")

        # Incorrect data type for 'handedness'.
        result = conn.insert_values_test(age=20, gender=1, handedness="1", image=byte_im)
        self.assertEqual(0, result, "Incorrect data type - handedness.")

        # Incorrect data type for 'image'.
        result = conn.insert_values_test(age=20, gender=1, handedness=1, image="byte_im")
        self.assertEqual(0, result, "Incorrect data type - image.")

    def test_insert_result_test_image(self):
        """
        Method to test insert_values_test_image method in mysql_connection.
        """

        # Testing Correct instance--------------------------------------------------------------------------------------
        result = conn.insert_result_test_image(image_no=1, result=True)
        self.assertEqual(bool, type(result), "Checking output type.")

        # Testing error handling- Incorrect data type-------------------------------------------------------------------
        # Incorrect data type for 'test_image'.
        result = conn.insert_result_test_image(image_no=1, result=True)
        self.assertEqual(0, result, "Incorrect data type - test_image.")

        # Incorrect data type for 'image_no'.
        result = conn.insert_result_test_image(image_no="1", result=True)
        self.assertEqual(0, result, "Incorrect data type - image_no.")

        # Incorrect data type for 'result'.
        result = conn.insert_result_test_image(image_no=1, result="True")
        self.assertEqual(0, result, "Incorrect data type - result.")

    def test_select_record_test(self):
        """
        Method to test select_record_test in mysql_connection.
        """

        # Testing Correct instance--------------------------------------------------------------------------------------
        user = conn.select_record_test(user_id=1)

        self.assertEqual(UserModel, type(user), "Database retrieval Data type.")
        self.assertEqual(1, user.get_id(), "Database retrieval value - id.")
        self.assertEqual(20, user.get_age(), "Database retrieval value - age.")
        self.assertEqual(1, user.get_gender(), "Database retrieval value - gender.")
        self.assertEqual(1, user.get_handedness(), "Database retrieval value - handedness.")

        # Testing error handling- Incorrect data type-------------------------------------------------------------------
        # Incorrect data type for 'user_id'.
        user = conn.select_record_test(user_id="149")
        self.assertEqual(0, user, "Incorrect data type - user_id.")

        # Testing error handling - Incorrect database record id---------------------------------------------------------
        # A record with a primary key 0 can not exist.
        user = conn.select_record_test(user_id=0)
        self.assertEqual(0, user, "Incorrect database record id.")

    def test_select_test_image_result(self):
        """
        Method to test select_test_image_result in mysql_connection.
        """

        # Testing Correct instance--------------------------------------------------------------------------------------
        result = conn.select_test_image_result(test_image_id=1)
        self.assertEqual(False, result, "Database retrieval value - result.")

        # Testing error handling - Incorrect data type------------------------------------------------------------------
        # Incorrect data type for 'test_image_id'.
        result = conn.select_test_image_result(test_image_id="self.test_image_id")
        self.assertEqual(0, result, "Incorrect data type - test_image_id.")

        # Testing error handling - Incorrect database record id---------------------------------------------------------
        # A record with a primary key 0 can not exist.
        result = conn.select_test_image_result(test_image_id=0)
        self.assertEqual(0, result, "Incorrect database record id.")


if __name__ == '__main__':
    unittest.main()
