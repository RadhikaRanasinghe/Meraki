from FrontendController import application
import unittest


class FlaskTest(unittest.TestCase):
    """
    This class performs the unit tests of the FrontendController.py
    """

    def test_create_user(self):
        """
        Unit test to check if the status code returned is 200
        """
        tester = application.test_client(self)
        response = tester.get("/create_user")
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_create_user_content(self):
        """
        Unit test to check if the content type returned is json
        """
        tester = application.test_client(self)
        response = tester.get("/create_user")
        self.assertEqual(response.content_type, "application/json")

    def test_create_user_data(self):
        """
        Unit test to check if the data returned is
        """
        tester = application.test_client(self)
        response = tester.get("/create_user")
        # TODO Change message
        self.assertTrue(b'Message' in response.data)

    def test_retrieve_result(self):
        """
        Unit test to check if the status code returned is 200
        """
        tester = application.test_client(self)
        response = tester.get("/retrieve_result")
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_retrieve_result_content(self):
        """
        Unit test to check if the content type returned is json
        """
        tester = application.test_client(self)
        response = tester.get("/retrieve_result")
        self.assertEqual(response.content_type, "application/json")

    def test_retrieve_result_data(self):
        """
        Unit test to check if the data returned is
        """
        tester = application.test_client(self)
        response = tester.get("/retrieve_result")
        # TODO Change message
        self.assertTrue(b'Message' in response.data)

    if __name__ == "__main__":
        unittest.main()
