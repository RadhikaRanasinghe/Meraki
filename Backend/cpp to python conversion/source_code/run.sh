# example of code usage 
# To compile use the scrip compile.sh and put the file name to be compiled

img_name_without_extension="exam_1"; shift #image name without the extension (e.g. for the image exam_1.jpg put just exam_1)
class_identifier="c"; shift # use c to identify the control group and p to patient group

./extractPen ${img_name_without_extension} #Will save and image ${img_name_without_extension}_pen.jpg
./extractTemplate ${img_name_without_extension} #Will save and image ${img_name_without_extension}_pen.jpg

./extractFeats ${img_name_without_extension}.jpg ${img_name_without_extension}_pen.jpg ${class_identifier}
