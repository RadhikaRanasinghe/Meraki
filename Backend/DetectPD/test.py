import base64
import io
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
from Detector import Detector
from mysql_connection import select_record_test

detector = Detector()
user_model = select_record_test(32)
print(user_model.get_test_image())
img = Image.open(io.BytesIO(user_model.get_test_image()))
img.show()
img.save('images/image.jpg')
