import mysql.connector

from UserModel import UserModel

# Database details.
HOST = "detectpd.c4e71ercisib.us-east-2.rds.amazonaws.com"
PORT = "3306"
USER = "admin"
PASSWORD = "password1234"
DATABASE = "DetectPD"


def insert_values_test(age: int, gender: int, handedness: int, image: bytes):
    """
    Method to insert a test to the "test" table in the database.
    :param age: age of testee
    :param gender: gender of the testee
    :param handedness: handedness of the testee
    :param image: hand drawn test
    :return: The primary key of the inserted row, if it is inserted properly, 0 is returned if an error occurs.
    """

    # Handling mysql errors.
    try:
        # Creating database connection.
        my_db = mysql.connector.connect(
            host=HOST,
            port=PORT,
            user=USER,
            password=PASSWORD,
            database=DATABASE
        )

        # Initialising cursor.
        my_cursor = my_db.cursor()

        print(f"MySQL connection started, Insert Values test (age: {age}, handedness: {handedness}, image: {type(image)})")

        # Checking if all the values are in correct format.
        if isinstance(age, int) and isinstance(gender, int) and isinstance(handedness, int) and isinstance(image,
                                                                                                           bytes):

            # Creating the query.
            sql_insert_query = "INSERT INTO test (age, gender, handedness, image) VALUES (%s, %s, %s, %s)"
            insert_tuple = (age, gender, handedness, image)

            # executing the query.
            my_cursor.execute(sql_insert_query, insert_tuple)

            # Getting the primary key of the last added record.
            added_id = my_cursor.lastrowid

            # Commit the changes to the database.
            my_db.commit()

            # Return the primary key of the last added record.
            print(f"Insert Values test - {{'output': {added_id}}}")
            return added_id

        # When the data type of values to be inserted are incorrect.
        else:
            # Print the error message.
            print(f"ERROR(Insert Values test) - Invalid argument type, expected Integer and Bytes. "
                  f"(age={type(age)}, gender={type(gender)}, handedness={type(handedness)}, image={type(image)}")

            # Return 0 since an error occurred.
            return 0

    # When mysql error occurs.
    except mysql.connector.Error as error:
        # Print the error message.
        print(f"ERROR(Insert Values test) - {error}")

        # Return 0 since an error occurred.
        return 0

    finally:
        # Closing the database connection if it is connected.
        if my_db.is_connected():
            my_cursor.close()
            my_db.close()
            print(f"MySQL connection is closed, Insert Values test (age: {age}, handedness: {handedness}, image: {type(image)})")


def select_record_test(user_id: int):
    """
    Method to select a record from the "test" table in the database.
    :param user_id: Primary key of the record.
    :return: If there is no error, the record data in as a UserModel object, else 0.
    """

    # Handling mysql errors.
    try:
        # Creating database connection.
        my_db = mysql.connector.connect(
            host=HOST,
            port=PORT,
            user=USER,
            password=PASSWORD,
            database=DATABASE
        )

        # Initialising cursor.
        my_cursor = my_db.cursor()

        print(f"MySQL connection started, Select Record test (user_id: {user_id})")

        # Checking if the primary key is in correct format.
        if isinstance(user_id, int):

            # Creating the query.
            sql_insert_query = "SELECT * FROM test WHERE id=%s" % user_id

            # executing the query.
            my_cursor.execute(sql_insert_query)

            # Getting the result of the execution.
            my_result = my_cursor.fetchone()

            # When a record is found.
            if my_result:
                # Reading the "test_image_id" column.
                test_image_id = my_result[5]
                if test_image_id is None:
                    test_image_id = 0

                # Making the UserModel object.
                user_model = UserModel(user_id=my_result[0],
                                       age=my_result[1],
                                       gender=my_result[2],
                                       handedness=my_result[3],
                                       test_image=my_result[4],
                                       test_image_id=test_image_id)
                # Returning the UserModel object.
                print(f"Select Record test - {{'output': {user_model}}}")
                return user_model
            # When a record is not found.
            else:
                # Print the error message.
                print(f"ERROR(Select Record test) - No Record with id={user_id}")

                # Return 0 since an error occurred.
                return 0
        # When the data type of the primary key is incorrect.
        else:
            # Print the error message.
            print(f"ERROR(Select Record test) - Invalid argument type, expected Integer. (user_id={type(user_id)}")

            # Return 0 since an error occurred.
            return 0

    # When mysql error occurs.
    except mysql.connector.Error as error:
        # Print the error message.
        print(f"ERROR(Select Record test) - {error}")

        # Return 0 since an error occurred.
        return 0

    finally:
        # Closing the database connection if it is connected.
        if my_db.is_connected():
            my_cursor.close()
            my_db.close()
            print(f"MySQL connection is closed, Select Record test (user_id: {user_id})")


def insert_result_test_image(image_no: int, result: bool):
    """
    Method to insert values to the "test_image" table in the database.
    :param image_no: The record primary key for the associated row in "test" table in database.
    :param result: The result of the test.
    :return: If there is no error, the primary key of the record added to the "test_image" table, else 0.
    """

    # Handling mysql errors.
    try:
        # Creating database connection.
        my_db = mysql.connector.connect(
            host=HOST,
            port=PORT,
            user=USER,
            password=PASSWORD,
            database=DATABASE
        )

        # Initialising cursor.
        my_cursor = my_db.cursor()

        print(f"MySQL connection started, Insert result test_image (image_no: {image_no}, result: {result})")

        # Checking if all the values are in correct format.
        if isinstance(image_no, int) and isinstance(result, bool):

            sql = f"SELECT test_image_id FROM test WHERE id={image_no}"

            my_cursor.execute(sql)

            my_result = my_cursor.fetchone()

            if my_result is None:
                # Print the error message.
                print(f"ERROR(Insert result test_image) - Record with image_no={image_no}.")

                # Return 0 since an error occurred.
                return 0
            else:
                test_image_id = bool(my_result[0])

                # Creating the query.
                sql_insert_query_test_image = f"UPDATE test_image SET result = {result} WHERE id={test_image_id}"

                # executing the query.
                my_cursor.execute(sql_insert_query_test_image)

                # Commit the changes to the database.
                my_db.commit()

                # Returning the primary key of the record added to the "test_image" table.
                print(f"Insert result test_image - {{'output': {type(test_image_id)}}}")
                return test_image_id

        # When the data type of values to be inserted are incorrect.
        else:
            # Print the error message.
            print(f"ERROR(Insert result test_image) - Invalid argument type, expected Integer, Boolean. "
                  f"(image_no={type(image_no)}, result={type(result)})")

            # Return 0 since an error occurred.
            return 0

    # When mysql error occurs.
    except mysql.connector.Error as error:
        # Print the error message.
        print(f"ERROR(Insert result test_image) - {error}")

        # Return 0 since an error occurred.
        return 0

    finally:
        # Closing the database connection if it is connected.
        if my_db.is_connected():
            my_cursor.close()
            my_db.close()
            print(f"MySQL connection is closed, Insert result test_image (image_no: {image_no}, result: {result})")


def select_test_image_result(test_image_id: int):
    """
    Method to select the 'result" column a record from "test_image" table in the database.
    :param test_image_id: Primary key of the record.
    :return: if there is no error, the "result" of the record, else 0.
    """

    # Handling mysql errors.
    try:
        # Creating database connection.
        my_db = mysql.connector.connect(
            host=HOST,
            port=PORT,
            user=USER,
            password=PASSWORD,
            database=DATABASE
        )

        # Initialising cursor.
        my_cursor = my_db.cursor()

        print(f"MySQL connection started, Select Record test_image_result (test_image_id: {test_image_id})")

        # Checking if the primary key is in correct format.
        if isinstance(test_image_id, int):

            # Creating the query.
            sql_select_query = "SELECT result FROM test_image WHERE id=%s" % test_image_id

            # executing the query.
            my_cursor.execute(sql_select_query)

            # Getting the result of the execution.
            my_result = my_cursor.fetchone()

            # When a record is found.
            if my_result:
                # Return the "result".
                print(f"Select Record test_image_result - {{'output': {bool(my_result[0])}}}")
                return bool(my_result[0])

            # When a record is not found.
            else:
                # Print the error message.
                print(f"ERROR(Select Record test_image_result) - No Record with id={test_image_id}")

                # Return 0 since an error occurred.
                return 0
        else:
            # Print the error message.
            print(f"ERROR(Select Record test_image_result) - Invalid argument type, expected Integer. "
                  f"(test_image_id={type(test_image_id)})")

            # Return 0 since an error occurred.
            return 0

    except mysql.connector.Error as error:
        # Print the error message.
        print(f"ERROR(Select Record test_image_result) - {error}")

        # Return 0 since an error occurred.
        return 0

    finally:
        # Closing the database connection if it is connected.
        if my_db.is_connected():
            my_cursor.close()
            my_db.close()
            print("MySQL connection is closed, Select Record test_image_result (test_image_id: {test_image_id})")
