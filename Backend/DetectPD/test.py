import io
import os

from PIL import Image, ImageFile
from Detector import Detector
from mysql_connection import select_record_test

ImageFile.LOAD_TRUNCATED_IMAGES = True

detector = Detector()

user_model = select_record_test(30)
img = Image.open(io.BytesIO(user_model.get_test_image()))
img.save('images/image' + str(user_model.get_id()) + '.jpg')

os.remove('images/image30.jpg')
