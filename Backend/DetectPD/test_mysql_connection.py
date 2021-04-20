import unittest

import cv2

import mysql_connection as conn
from TestImageBuilder import TestImageBuilder
from UserModel import UserModel


class MysqlConnectionTest(unittest.TestCase):
    test_id = None
    test_image_id = None

    def test_insert_values_test(self):
        im = cv2.imread("sample_images/exam_1.jpg")

        is_success, im_buf_arr = cv2.imencode(".jpg", im)
        byte_im = im_buf_arr.tobytes()

        result = conn.insert_values_test(20, 1, 1, byte_im)
        self.assertEqual(type(result), int, "Checking output type.")
        self.assertNotEqual(result, 0, "Incorrect database record id.")
        self.test_id = result

        result = conn.insert_values_test("20", 1, 1, byte_im)
        self.assertEqual(0, result, "Incorrect data type - age.")

        result = conn.insert_values_test(20, "1", 1, byte_im)
        self.assertEqual(0, result, "Incorrect data type - gender.")

        result = conn.insert_values_test(20, 1, "1", byte_im)
        self.assertEqual(0, result, "Incorrect data type - handedness.")

        result = conn.insert_values_test(20, 1, 1, "byte_im")
        self.assertEqual(0, result, "Incorrect data type - image.")

    def test_insert_values_test_image(self):
        test_image = TestImageBuilder() \
            .set_rms(3176.216064) \
            .set_std_deviation_st_ht(0.000672) \
            .set_max_between_st_ht(7098.378906) \
            .set_min_between_st_ht(46569.03516) \
            .set_mrt(21.280848) \
            .set_max_ht(224.197754) \
            .set_min_ht(0.156795) \
            .set_std_ht(802.821106) \
            .set_changes_from_negative_to_positive_between_st_ht(0.216138) \
            .build()

        result = conn.insert_values_test_image(test_image=test_image, image_no=self.test_id, result=True)
        self.assertEqual(int, type(result), "Checking output type.")
        self.assertNotEqual(0, result, "Incorrect database record id.")
        self.test_id = result

        result = conn.insert_values_test_image(test_image="test_image", image_no=self.test_id, result=True)
        self.assertEqual(0, result, "Incorrect data type - test_image.")

        result = conn.insert_values_test_image(test_image=test_image, image_no="self.test_id", result=True)
        self.assertEqual(0, result, "Incorrect data type - image_no.")

        result = conn.insert_values_test_image(test_image=test_image, image_no=self.test_id, result="True")
        self.assertEqual(0, result, "Incorrect data type - result.")

    def test_select_record_test(self):
        im = cv2.imread("sample_images/exam_1.jpg")

        is_success, im_buf_arr = cv2.imencode(".jpg", im)
        byte_im = im_buf_arr.tobytes()

        user = conn.select_record_test(self.test_id)

        self.assertEqual(UserModel, type(user), "Database retrieval Data type.")
        self.assertEqual(user.get_id(), self.test_id, "Database retrieval value - id.")
        self.assertEqual(user.get_age(), 20, "Database retrieval value - age.")
        self.assertEqual(user.get_gender(), 1, "Database retrieval value - gender.")
        self.assertEqual(user.get_handedness(), 1, "Database retrieval value - handedness.")
        self.assertEqual(byte_im, user.get_test_image(), "Database retrieval value - test_image.")
        self.assertEqual(user.get_test_image_id(), self.test_image_id, "Database retrieval value - test_image_id.")

        user = conn.select_record_test("149")
        self.assertEqual(user, 0, "Incorrect data type - user_id.")

        user = conn.select_record_test(self.test_id + 1000)
        self.assertEqual(user, 0, "Incorrect database record id.")

    def test_select_test_image_result(self):
        result = conn.select_test_image_result(self.test_image_id)
        self.assertEqual(True, result, "Database retrieval value - result.")

        result = conn.select_test_image_result("self.test_image_id")
        self.assertEqual(0, result, "Incorrect data type - test_image_id.")

        result = conn.select_test_image_result(self.test_image_id + 1000)
        self.assertEqual(0, result, "Incorrect database record id.")


if __name__ == '__main__':
    unittest.main()
