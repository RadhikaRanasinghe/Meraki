import mysql.connector

from TestImage import TestImage
from UserModel import UserModel


def insert_values_test(age: int, gender: int, handedness: int, image: bytes):
    try:
        my_db = mysql.connector.connect(
            host="detectpd.c4e71ercisib.us-east-2.rds.amazonaws.com",
            port="3306",
            user="admin",
            password="password1234",
            database="DetectPD"
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
            print(f"ERROR - Invalid argument type. (age={type(age)}, gender={type(gender)}, handedness={type(handedness)}, image={type(image)}")
            return 0

    except mysql.connector.Error as error:
        print(f"ERROR - {error}")
        return 0

    finally:
        if my_db.is_connected():
            my_cursor.close()
            my_db.close()
            print("MySQL connection is closed, Insert Values")


def select_record(user_id: int):
    try:
        my_db = mysql.connector.connect(
            host="detectpd.c4e71ercisib.us-east-2.rds.amazonaws.com",
            port="3306",
            user="admin",
            password="password1234",
            database="DetectPD"
        )

        my_cursor = my_db.cursor()

        sql_insert_query = "SELECT * FROM test WHERE id=%s" % user_id

        my_cursor.execute(sql_insert_query)

        my_result = my_cursor.fetchone()

        if my_result:
            user_model = UserModel(my_result[0], my_result[1], my_result[2], my_result[3], my_result[4])
            return user_model
        else:
            return 0

    except mysql.connector.Error as error:
        print(f"ERROR - {error}")
        return 0

    finally:
        if my_db.is_connected():
            my_cursor.close()
            my_db.close()
            print("MySQL connection is closed, Select Record")


def insert_values_test_image(test_image: TestImage, image_no: int):
    try:
        my_db = mysql.connector.connect(
            host="detectpd.c4e71ercisib.us-east-2.rds.amazonaws.com",
            port="3306",
            user="admin",
            password="password1234",
            database="DetectPD"
        )

        my_cursor = my_db.cursor()

        if isinstance(test_image, TestImage) and isinstance(image_no, int):

            sql_insert_query_test_image = """INSERT INTO test_image 
                                    (rms, max_between_st_ht, min_between_st_ht, std_deviation_st_ht, mrt, max_ht,
                                     min_ht, std_ht, changes_from_n_to_p_between_st_ht) 
                                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

            insert_tuple_test_image = (
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

            sql_insert_query_test = """INSERT INTO test (test_image) VALUES (%s) WHERE id=(%s)"""

            insert_tuple_test = (added_id, image_no)

            my_cursor.execute(sql_insert_query_test, insert_tuple_test)

            return added_id

        else:
            print(f"ERROR - Invalid argument type. (test_image={type(test_image)}, image_no={type(image_no)})")
            return 0

    except mysql.connector.Error as error:
        print(f"ERROR - {error}")
        return 0

    finally:
        if my_db.is_connected():
            my_cursor.close()
            my_db.close()
            print("MySQL connection is closed, Select Record")
