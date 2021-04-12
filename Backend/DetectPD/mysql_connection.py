import mysql.connector

from TestImage import TestImage
from UserModel import UserModel

HOST = "detectpd.c4e71ercisib.us-east-2.rds.amazonaws.com"
PORT = "3306"
USER = "admin"
PASSWORD = "password1234"
DATABASE = "DetectPD"


def insert_values_test(age: int, gender: int, handedness: int, image: bytes):
    try:
        my_db = mysql.connector.connect(
            host=HOST,
            port=PORT,
            user=USER,
            password=PASSWORD,
            database=DATABASE
        )

        my_cursor = my_db.cursor()

        if isinstance(age, int) and isinstance(gender, int) and isinstance(handedness, int) and isinstance(image,
                                                                                                           bytes):

            sql_insert_query = "INSERT INTO test (age, gender, handedness, image) VALUES (%s, %s, %s, %s)"

            insert_tuple = (age, gender, handedness, image)

            my_cursor.execute(sql_insert_query, insert_tuple)

            added_id = my_cursor.lastrowid

            my_db.commit()

            return added_id

        else:
            print(f"ERROR(Insert Values test) - Invalid argument type, expected Integer and Bytes. "
                  f"(age={type(age)}, gender={type(gender)}, handedness={type(handedness)}, image={type(image)}")
            return 0

    except mysql.connector.Error as error:
        print(f"ERROR(Insert Values test) - {error}")
        return 0

    finally:
        if my_db.is_connected():
            my_cursor.close()
            my_db.close()
            print("MySQL connection is closed, Insert Values test")


def select_record_test(user_id: int):
    try:
        my_db = mysql.connector.connect(
            host=HOST,
            port=PORT,
            user=USER,
            password=PASSWORD,
            database=DATABASE
        )

        my_cursor = my_db.cursor()

        if isinstance(user_id, int):

            sql_insert_query = "SELECT * FROM test WHERE id=%s" % user_id

            my_cursor.execute(sql_insert_query)

            my_result = my_cursor.fetchone()

            if my_result:
                test_image_id = my_result[5]
                if test_image_id is None:
                    test_image_id = 0

                user_model = UserModel(user_id=my_result[0],
                                       age=my_result[1],
                                       gender=my_result[2],
                                       handedness=my_result[3],
                                       test_image=my_result[4],
                                       test_image_id=test_image_id)
                return user_model
            else:
                print(f"ERROR(Select Record test) - No Record with id={user_id}")
                return 0
        else:
            print(f"ERROR(Select Record test) - Invalid argument type, expected Integer. (user_id={type(user_id)}")
            return 0

    except mysql.connector.Error as error:
        print(f"ERROR(Select Record test) - {error}")
        return 0

    finally:
        if my_db.is_connected():
            my_cursor.close()
            my_db.close()
            print("MySQL connection is closed, Select Record test")


def insert_values_test_image(test_image: TestImage, image_no: int, result: bool):
    try:
        my_db = mysql.connector.connect(
            host=HOST,
            port=PORT,
            user=USER,
            password=PASSWORD,
            database=DATABASE
        )

        my_cursor = my_db.cursor()

        if isinstance(test_image, TestImage) and isinstance(image_no, int) and isinstance(result, bool):

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

            my_cursor.execute(sql_insert_query_test_image, insert_tuple_test_image)

            added_id = my_cursor.lastrowid

            my_db.commit()

            sql_insert_query_test = """UPDATE test
                                        SET test_image_id = %s
                                        WHERE id = %s"""

            insert_tuple_test = (added_id, image_no)

            my_cursor.execute(sql_insert_query_test, insert_tuple_test)

            my_db.commit()

            return added_id

        else:
            print(f"ERROR(Insert Values test_image) - Invalid argument type, expected TestImage, Integer, Boolean. "
                  f"(test_image={type(test_image)}, image_no={type(image_no)}, result={type(result)})")
            return 0

    except mysql.connector.Error as error:
        print(f"ERROR(Insert Values test_image) - {error}")
        return 0

    finally:
        if my_db.is_connected():
            my_cursor.close()
            my_db.close()
            print("MySQL connection is closed, Insert Values test_image")


def select_test_image_result(test_image_id: int):
    try:
        my_db = mysql.connector.connect(
            host=HOST,
            port=PORT,
            user=USER,
            password=PASSWORD,
            database=DATABASE
        )

        my_cursor = my_db.cursor()

        if isinstance(test_image_id, int):

            sql_select_query = "SELECT result FROM test_image WHERE id=%s" % test_image_id

            my_cursor.execute(sql_select_query)

            my_result = my_cursor.fetchone()

            if my_result:
                return bool(my_result)
            else:
                print(f"ERROR(Select Record test_image_result) - No Record with id={test_image_id}")
                return 0
        else:
            print(f"ERROR(Select Record test_image_result) - Invalid argument type, expected Integer. "
                  f"(test_image_id={type(test_image_id)})")
            return 0

    except mysql.connector.Error as error:
        print(f"ERROR(Select Record test_image_result) - {error}")
        return 0

    finally:
        if my_db.is_connected():
            my_cursor.close()
            my_db.close()
            print("MySQL connection is closed, Select Record test_image_result")
