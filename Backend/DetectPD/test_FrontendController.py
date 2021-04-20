import io
import json
import unittest

import cv2

from FrontendController import application


class FlaskTest(unittest.TestCase):
    """
    This class performs the unit tests of the FrontendController.py
    """

    def test_create_user(self):
        """
        Unit test to check the POST request controller
        """

        # Loading the Flask application.
        tester = application.test_client(self)

        # Loading the image as a byteString.
        im = cv2.imread('sample_images/exam_1.jpg')
        is_success, im_buf_arr = cv2.imencode(".jpg", im)
        byte_im = im_buf_arr.tobytes()

        # Testing Correct instance--------------------------------------------------------------------------------------
        data = {'age': 18, 'gender': 1, 'handedness': 1}
        data = {key: str(value) for key, value in data.items()}
        data['image'] = (io.BytesIO(byte_im), 'exam_1.jpg')

        response = tester.post('/create_user', data=data, content_type='multipart/form-data')
        self.assertEqual(201, response.status_code, "Checking status code returned - 201 (Successfully Created)")
        self.assertEqual(response.content_type, "application/json", "Checking data type returned - json")
        self.assertTrue(b'image_no' in response.data, "Checking image_no returned.")
        image_no = json.loads(response.data.decode('utf-8'))['image_no']
        self.assertEqual(type(image_no), int, "Checking data type of image_no - int")
        self.image_no = image_no

        # Testing error handling - invalid input type-------------------------------------------------------------------
        error_message = "Invalid input type. \n'age'/'gender'/'handedness' - Integer, \n'image' - jpg/jpeg image"

        # Invalid input for 'age'.
        data = {'age': 'a', 'gender': 1, 'handedness': 1}
        data = {key: str(value) for key, value in data.items()}
        data['image'] = (io.BytesIO(byte_im), 'exam_1.jpg')

        response = tester.post('/create_user', data=data, content_type='multipart/form-data')
        self.assertEqual(415, response.status_code, "Checking status code returned - 415 (Invalid input type)")
        self.assertEqual(response.content_type, "application/json", "Checking data type returned - json")
        self.assertTrue(b'error' in response.data, "Checking if an error message is returned")
        error = json.loads(response.data.decode('utf-8'))['error']
        self.assertEqual(error_message, error, "Checking if the error message returned is the correct message for "
                                               "status code 415")

        # Invalid input for 'gender'.
        data = {'age': 1, 'gender': 'a', 'handedness': 1}
        data = {key: str(value) for key, value in data.items()}
        data['image'] = (io.BytesIO(byte_im), 'exam_1.jpg')

        response = tester.post('/create_user', data=data, content_type='multipart/form-data')
        self.assertEqual(415, response.status_code, "Checking status code returned - 415 (Invalid input type)")
        self.assertEqual(response.content_type, "application/json", "Checking data type returned - json")
        self.assertTrue(b'error' in response.data, "Checking if an error message is returned")
        error = json.loads(response.data.decode('utf-8'))['error']
        self.assertEqual(error_message, error, "Checking if the error message returned is the correct message for "
                                               "status code 415")

        # Invalid input for 'handedness'.
        data = {'age': 1, 'gender': 1, 'handedness': 'a'}
        data = {key: str(value) for key, value in data.items()}
        data['image'] = (io.BytesIO(byte_im), 'exam_1.jpg')

        response = tester.post('/create_user', data=data, content_type='multipart/form-data')
        self.assertEqual(415, response.status_code, "Checking status code returned - 415 (Invalid input type)")
        self.assertEqual(response.content_type, "application/json", "Checking data type returned - json")
        self.assertTrue(b'error' in response.data, "Checking if an error message is returned")
        error = json.loads(response.data.decode('utf-8'))['error']
        self.assertEqual(error_message, error, "Checking if the error message returned is the correct message for "
                                               "status code 415")

        # Invalid input for 'image'.
        im = cv2.imread('sample_images/exam_1.png')
        is_success, im_buf_arr = cv2.imencode(".png", im)
        byte_im = im_buf_arr.tobytes()

        data = {'age': 1, 'gender': 1, 'handedness': 1}
        data = {key: str(value) for key, value in data.items()}
        data['image'] = (io.BytesIO(byte_im), 'exam_1.png')

        response = tester.post('/create_user', data=data, content_type='multipart/form-data')
        self.assertEqual(415, response.status_code, "Checking status code returned - 415 (Invalid input type)")
        self.assertEqual(response.content_type, "application/json", "Checking data type returned - json")
        self.assertTrue(b'error' in response.data, "Checking if an error message is returned")
        error = json.loads(response.data.decode('utf-8'))['error']
        self.assertEqual(error_message, error, "Checking if the error message returned is the correct message for "
                                               "status code 415")

        # Testing error handling - missing input------------------------------------------------------------------------
        error_message = "Missing input. \n'age', 'gender', 'handedness', 'image' is required."

        # Missing input for 'image'.
        data = {'age': 1, 'gender': 1, 'handedness': 1}
        data = {key: str(value) for key, value in data.items()}

        response = tester.post('/create_user', data=data, content_type='multipart/form-data')
        self.assertEqual(400, response.status_code, "Checking status code returned - 400 (Missing input)")
        self.assertEqual(response.content_type, "application/json", "Checking data type returned - json")
        self.assertTrue(b'error' in response.data, "Checking if an error message is returned")
        error = json.loads(response.data.decode('utf-8'))['error']
        self.assertEqual(error_message, error, "Checking if the error message returned is the correct message for "
                                               "status code 400")

        # Loading the image as a byteString.
        im = cv2.imread('sample_images/exam_1.jpg')
        is_success, im_buf_arr = cv2.imencode(".jpg", im)
        byte_im = im_buf_arr.tobytes()

        # Missing input for 'age'.
        data = {'gender': 1, 'handedness': 1}
        data = {key: str(value) for key, value in data.items()}
        data['image'] = (io.BytesIO(byte_im), 'exam_1.jpg')

        response = tester.post('/create_user', data=data, content_type='multipart/form-data')
        self.assertEqual(400, response.status_code, "Checking status code returned - 400 (Missing input)")
        self.assertEqual(response.content_type, "application/json", "Checking data type returned - json")
        self.assertTrue(b'error' in response.data, "Checking if an error message is returned")
        error = json.loads(response.data.decode('utf-8'))['error']
        self.assertEqual(error_message, error, "Checking if the error message returned is the correct message for "
                                               "status code 400")

        # Missing input for 'gender'.
        data = {'age': 1, 'handedness': 1}
        data = {key: str(value) for key, value in data.items()}
        data['image'] = (io.BytesIO(byte_im), 'exam_1.jpg')

        response = tester.post('/create_user', data=data, content_type='multipart/form-data')
        self.assertEqual(400, response.status_code, "Checking status code returned - 400 (Missing input)")
        self.assertEqual(response.content_type, "application/json", "Checking data type returned - json")
        self.assertTrue(b'error' in response.data, "Checking if an error message is returned")
        error = json.loads(response.data.decode('utf-8'))['error']
        self.assertEqual(error_message, error, "Checking if the error message returned is the correct message for "
                                               "status code 400")

        # Missing input for 'handedness'.
        data = {'age': 1, 'gender': 1}
        data = {key: str(value) for key, value in data.items()}
        data['image'] = (io.BytesIO(byte_im), 'exam_1.jpg')

        response = tester.post('/create_user', data=data, content_type='multipart/form-data')
        self.assertEqual(400, response.status_code, "Checking status code returned - 400 (Missing input)")
        self.assertEqual(response.content_type, "application/json", "Checking data type returned - json")
        self.assertTrue(b'error' in response.data, "Checking if an error message is returned")
        error = json.loads(response.data.decode('utf-8'))['error']
        self.assertEqual(error_message, error, "Checking if the error message returned is the correct message for "
                                               "status code 400")

    def test_retrieve_result(self):
        """
        Unit test to check the GET request controller
        """

        # Loading the Flask application.
        tester = application.test_client(self)

        # Testing Correct instance--------------------------------------------------------------------------------------
        query_string = {'image_no': 1}
        response = tester.get('/retrieve_result', query_string=query_string)
        self.assertEqual(200, response.status_code, "Checking status code returned - 200 (Successful diagnosis)")
        self.assertEqual(response.content_type, "application/json", "Checking data type returned - json")
        self.assertTrue(b'result' in response.data, "Checking if the result is returned")

        # Testing error handling - invalid input type-------------------------------------------------------------------
        error_message = "Invalid input type. \n'image_no' - Integer"

        # Invalid input for 'image_no'.
        query_string = {'image_no': 'a'}
        response = tester.get('/retrieve_result', query_string=query_string)
        self.assertEqual(415, response.status_code, "Checking status code returned - 415 (Invalid input type)")
        self.assertEqual(response.content_type, "application/json", "Checking data type returned - json")
        self.assertTrue(b'error' in response.data, "Checking if an error message is returned")
        error = json.loads(response.data.decode('utf-8'))['error']
        self.assertEqual(error_message, error, "Checking if the error message returned is the correct message for "
                                               "status code 415")

        # Testing error handling - not found content--------------------------------------------------------------------
        error_message = "Invalid image_no, No such id exists in the database."

        query_string = {'image_no': 0}
        response = tester.get('/retrieve_result', query_string=query_string)
        self.assertEqual(416, response.status_code, "Checking status code returned - 416 (Not found content)")
        self.assertEqual(response.content_type, "application/json", "Checking data type returned - json")
        self.assertTrue(b'error' in response.data, "Checking if an error message is returned")
        error = json.loads(response.data.decode('utf-8'))['error']
        self.assertEqual(error_message, error, "Checking if the error message returned is the correct message for "
                                               "status code 416")

        # Testing error handling - missing input------------------------------------------------------------------------
        error_message = "Missing input. \n'image_no' is required."

        # Missing input for 'image_no'.
        response = tester.get('/retrieve_result')
        self.assertEqual(400, response.status_code, "Checking status code returned - 400 (Missing input)")
        self.assertEqual(response.content_type, "application/json", "Checking data type returned - json")
        self.assertTrue(b'error' in response.data, "Checking if an error message is returned")
        error = json.loads(response.data.decode('utf-8'))['error']
        self.assertEqual(error_message, error, "Checking if the error message returned is the correct message for "
                                               "status code 400")

    if __name__ == "__main__":
        unittest.main()
