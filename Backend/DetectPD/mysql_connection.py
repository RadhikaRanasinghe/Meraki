import mysql.connector

from TestImage import TestImage
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

    Parameters
    ----------
    age - age of testee
    gender - gender of the testee
    handedness - handedness of the testee
    image - hand drawn test

    Returns
    -------
    The primary key of the inserted row, if it is inserted properly,
    0 is returned if an error occurs.
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

        print("MySQL connection started, Insert Values test")

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
            print("MySQL connection is closed, Insert Values test")


def select_record_test(user_id: int):
    """
    Method to select a record from the "test" table in the database.

    Parameters
    ----------
    user_id - Primary key of the record.

    Returns
    -------
    If there is no error, the record data in as a UserModel object, else 0.
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

        print("MySQL connection started, Select Record test")

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
            print("MySQL connection is closed, Select Record test")


def insert_values_test_image(test_image: TestImage, image_no: int, result: bool):
    """
    Method to insert values to the "test_image" table in the database.

    Parameters
    ----------
    test_image - A TestImage object containing values according to the users hand drawing.
    image_no - The record primary key for the associated row in "test" table in database.
    result - The result of the test.

    Returns
    -------
    If there is no error, the primary key of the record added to the "test_image" table, else 0.
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

        print("MySQL connection started, Insert Values test_image")

        # Checking if all the values are in correct format.
        if isinstance(test_image, TestImage) and isinstance(image_no, int) and isinstance(result, bool):

            # Creating the query.
            sql_insert_query_test_image = """INSERT INTO test_image 
                                    (result, rms, max_between_st_ht, min_between_st_ht, std_deviation_st_ht, mrt, 
                                    max_ht, min_ht, std_ht, changes_from_n_to_p_between_st_ht) 
                                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

            insert_tuple_test_image = (
                result,
                test_image.get_rms(),
                test_image.get_max_between_st_ht(),
                test_image.get_min_between_st_ht(),
                test_image.get_std_deviation_st_ht(),
                test_image.get_mrt(),
                test_image.get_max_ht(),
                test_image.get_min_ht(),
                test_image.get_std_ht(),
                test_image.get_changes_from_negative_to_positive_between_st_ht()
            )

            # executing the query.
            my_cursor.execute(sql_insert_query_test_image, insert_tuple_test_image)

            # Getting the primary key of the last added record.
            added_id = my_cursor.lastrowid

            # Commit the changes to the database.
            my_db.commit()

            # Creating the query to update the "test" table.
            sql_insert_query_test = """UPDATE test
                                        SET test_image_id = %s
                                        WHERE id = %s"""

            insert_tuple_test = (added_id, image_no)

            # executing the query to update the "test" table.
            my_cursor.execute(sql_insert_query_test, insert_tuple_test)

            # Commit the changes to the database.
            my_db.commit()

            # Returning the primary key of the record added to the "test_image" table.
            return added_id

        # When the data type of values to be inserted are incorrect.
        else:
            # Print the error message.
            print(f"ERROR(Insert Values test_image) - Invalid argument type, expected TestImage, Integer, Boolean. "
                  f"(test_image={type(test_image)}, image_no={type(image_no)}, result={type(result)})")

            # Return 0 since an error occurred.
            return 0

    # When mysql error occurs.
    except mysql.connector.Error as error:
        # Print the error message.
        print(f"ERROR(Insert Values test_image) - {error}")

        # Return 0 since an error occurred.
        return 0

    finally:
        # Closing the database connection if it is connected.
        if my_db.is_connected():
            my_cursor.close()
            my_db.close()
            print("MySQL connection is closed, Insert Values test_image")


def select_test_image_result(test_image_id: int):
    """
    Method to select the 'result" column a record from "test_image" table in the database.

    Parameters
    ----------
    test_image_id - Primary key of the record.

    Returns
    -------
    if there is no error, the "result" of the record, else 0.
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

        print("MySQL connection started, Select Record test_image_result")

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
                return bool(my_result)
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
            print("MySQL connection is closed, Select Record test_image_result")
