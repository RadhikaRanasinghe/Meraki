import cv2

BLUR_RADIUS = 5


def extractTemplate(img):
    img = cv2.blur(img, (BLUR_RADIUS, BLUR_RADIUS))
    img = cv2.medianBlur(img, 11)

    if not img.data:
        print("No image data \n")
        return -1

    for i in img:
        for color in i:
            if color[0] < 120 and color[1] < 120 and color[2] < 120:
                color[0] = 0
                color[1] = 0
                color[2] = 0
            else:
                color[0] = 255
                color[1] = 255
                color[2] = 255

    erosion_type = cv2.MORPH_RECT
    erosion_size = 2
    element = cv2.getStructuringElement(erosion_type, (2 * erosion_size + 1, 2 * erosion_size + 1),
                                        (erosion_size, erosion_size))

    img = cv2.erode(img, element)

    erosion_size = 1
    element1 = cv2.getStructuringElement(erosion_type, (2 * erosion_size + 1, 2 * erosion_size + 1),
                                         (erosion_size, erosion_size))

    img = cv2.dilate(img, element1)
    img = cv2.dilate(img, element1)

    img = cv2.blur(img, (3 * BLUR_RADIUS, 3 * BLUR_RADIUS))
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    element2 = cv2.getStructuringElement(erosion_type, (2 * erosion_size + 1, 2 * erosion_size + 1),
                                         (erosion_size, erosion_size))

    # Otsu threshold is used to remove the noise and background
    ret, img_gray = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    img_gray = cv2.dilate(img_gray, element2)
    img_gray = cv2.dilate(img_gray, element2)
    img_gray = cv2.dilate(img_gray, element2)
    img_gray = cv2.dilate(img_gray, element2)
    img_gray = cv2.dilate(img_gray, element2)

    return img_gray
