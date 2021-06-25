# DetectPD by MERAKI

### General information

    VirtualENV - python 3.8
    BASE URL - http://detectpd.us-east-2.elasticbeanstalk.com

### POST request format

    URL - '/create_user'

    INPUT
        image : binary file (jpg or jpeg)
        age : int 
        gender : int (male: 1, female: 2)
        handedness : int (right-handed: 1, left-handed: 2)

    OUTPUT
        image_no: int

## GET request format

    URL - '/retrieve_result'

    INPUT
        image_no: int (as query string)

    OUTPUT
        result: Boolean (PD detected: True, Healthy: False)

### Status Codes used

    201 - successfully created (POST)
    200 - successful diagnosis (GET)
    400 - missing input (GET/POST)
    416 - not found content (GET)
    415 - invalid input type (GET/POST)
