### General information
    
    VirtualENV - python 3.8
    BASE URL - http://detectpd.us-east-2.elasticbeanstalk.com


###POST request format

    URL - '/create_user'

    INPUT
        image : binary file
        age : int
        gender : int
        handedness : int

    OUTPUT
        image_no: int


##GET request format

    URL - '/retrieve_result'

    INPUT
        image_no: int (as a parameter)

    OUTPUT
        result: Boolean (True if PD is detected)


### Status Codes used

    201 - successfully created (POST)
    200 - successful diagnosis (GET)
    400 - missing input (GET/POST)
    416 - not found content (GET)
    415 - invalid input type (GET/POST)
