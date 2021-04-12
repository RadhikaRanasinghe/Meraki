from extractPen import extractPen
from extractTemplate import extractTemplate
from extractFeats import extractFeats

filePath = "Resources/mea1-P1"

extractPen(filePath)
print("Pen Complete")
extractTemplate(filePath)
print("Template Complete")

extractFeats([filePath + '.jpg', filePath + '_pen.jpg'])
