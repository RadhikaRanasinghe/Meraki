import unittest

import cv2
import numpy as np

import mysql_connection as conn
from TestImageBuilder import TestImageBuilder
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
        result = conn.insert_values_test(20, 1, 1, byte_im)
        self.assertEqual(type(result), int, "Checking output type.")
        self.assertNotEqual(result, 0, "Incorrect database record id.")

        # Testing error handling----------------------------------------------------------------------------------------
        result = conn.insert_values_test("20", 1, 1, byte_im)
        self.assertEqual(0, result, "Incorrect data type - age.")

        result = conn.insert_values_test(20, "1", 1, byte_im)
        self.assertEqual(0, result, "Incorrect data type - gender.")

        result = conn.insert_values_test(20, 1, "1", byte_im)
        self.assertEqual(0, result, "Incorrect data type - handedness.")

        result = conn.insert_values_test(20, 1, 1, "byte_im")
        self.assertEqual(0, result, "Incorrect data type - image.")

    def test_insert_values_test_image(self):
        """
        Method to test insert_values_test_image method in mysql_connection.
        """

        # Initialising a TestImage object.
        test_image = TestImageBuilder() \
            .set_rms(13350.62519480) \
            .set_std_deviation_st_ht(16574.07305706) \
            .set_max_between_st_ht(72295.95503130) \
            .set_min_between_st_ht(0.01570581) \
            .set_mrt(61.45050234) \
            .set_max_ht(263.39086953) \
            .set_min_ht(0.34922811) \
            .set_std_ht(4177.51818530) \
            .set_changes_from_negative_to_positive_between_st_ht(0.20512821) \
            .build()

        # Testing Correct instance--------------------------------------------------------------------------------------
        result = conn.insert_values_test_image(test_image=test_image, image_no=2, result=True)
        self.assertEqual(int, type(result), "Checking output type.")
        self.assertNotEqual(0, result, "Incorrect database record id.")
        self.test_id = result

        # Testing error handling----------------------------------------------------------------------------------------
        result = conn.insert_values_test_image(test_image="test_image", image_no=2, result=True)
        self.assertEqual(0, result, "Incorrect data type - test_image.")

        result = conn.insert_values_test_image(test_image=test_image, image_no="self.test_id", result=True)
        self.assertEqual(0, result, "Incorrect data type - image_no.")

        result = conn.insert_values_test_image(test_image=test_image, image_no=2, result="True")
        self.assertEqual(0, result, "Incorrect data type - result.")

    def test_select_record_test(self):
        """
        Method to test select_record_test in mysql_connection.
        """

        # Loading the Original image from file storage.
        original_image = cv2.imread("sample_images/exam_1.jpg")

        # Loading the image in the database.
        user = conn.select_record_test(1)
        nparr = np.frombuffer(user.get_test_image(), np.uint8)
        database_image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Testing Correct instance--------------------------------------------------------------------------------------
        self.assertEqual(UserModel, type(user), "Database retrieval Data type.")
        self.assertEqual(1, user.get_id(), "Database retrieval value - id.")
        self.assertEqual(20, user.get_age(), "Database retrieval value - age.")
        self.assertEqual(1, user.get_gender(), "Database retrieval value - gender.")
        self.assertEqual(1, user.get_handedness(), "Database retrieval value - handedness.")
        self.assertTrue(
            original_image.shape == database_image.shape and not(np.bitwise_xor(original_image, database_image).any()),
            "Database retrieval value - test_image."
        )
        self.assertEqual(1, user.get_test_image_id(), "Database retrieval value - test_image_id.")

        # Testing error handling----------------------------------------------------------------------------------------
        user = conn.select_record_test("149")
        self.assertEqual(0, user, "Incorrect data type - user_id.")

        user = conn.select_record_test(0)
        self.assertEqual(0, user, "Incorrect database record id.")

    def test_select_test_image_result(self):
        """
        Method to test select_test_image_result in mysql_connection.
        """

        # Testing Correct instance--------------------------------------------------------------------------------------
        result = conn.select_test_image_result(1)
        self.assertEqual(False, result, "Database retrieval value - result.")

        # Testing error handling----------------------------------------------------------------------------------------
        result = conn.select_test_image_result("self.test_image_id")
        self.assertEqual(0, result, "Incorrect data type - test_image_id.")

        result = conn.select_test_image_result(0)
        self.assertEqual(0, result, "Incorrect database record id.")


if __name__ == '__main__':
    unittest.main()
