from math import cos, sin, sqrt, atan

import cv2

DISPLACEMENT = 10


class cpoint:
    x = None
    y = None

    def __init__(self, x, y):
        self.x = x
        self.y = y


# Functions to recovery the Neighboors as follow:
# P9 P2 P3
# P8 P1 P4
# P7 P6 P5
def P1(dest, line, col):
    return dest[line][col]


def P2(dest, line, col):
    return dest[line - 1][col]


def P3(dest, line, col):
    return dest[line - 1][col + 1]


def P4(dest, line, col):
    return dest[line][col + 1]


def P5(dest, line, col):
    return dest[line + 1][col + 1]


def P6(dest, line, col):
    return dest[line + 1][col]


def P7(dest, line, col):
    return dest[line + 1][col - 1]


def P8(dest, line, col):
    return dest[line][col - 1]


def P9(dest, line, col):
    return dest[line - 1][col - 1]


def delete(dest, line, col):
    dest[line][col] = 0


def Zhang_Suen(dest):
    height = dest.shape[0]
    width = dest.shape[1]
    ThiningContinue = True
    RemPoints = []

    for line in range(height):
        for col in range(width):
            dest[line][col] = 0 if dest[line][col] == 255 else 1

    print("Zhang_Suen - while started")

    while ThiningContinue:
        ThiningContinue = False

        for line in range(1, height - 1):
            for col in range(1, width - 1):
                Neighboors = 0
                Conectivity = 0

                # Pixel must be black
                if P1(dest, line, col) == 0:
                    continue
                # Connectivity number must be 1;
                Conectivity = 1 if (P2(dest, line, col) == 0 and P3(dest, line, col) == 1) else 0
                Conectivity += 1 if (P3(dest, line, col) == 0 and P4(dest, line, col) == 1) else 0
                Conectivity += 1 if (P4(dest, line, col) == 0 and P5(dest, line, col) == 1) else 0
                Conectivity += 1 if (P5(dest, line, col) == 0 and P6(dest, line, col) == 1) else 0
                Conectivity += 1 if (P6(dest, line, col) == 0 and P7(dest, line, col) == 1) else 0
                Conectivity += 1 if (P7(dest, line, col) == 0 and P8(dest, line, col) == 1) else 0
                Conectivity += 1 if (P8(dest, line, col) == 0 and P9(dest, line, col) == 1) else 0
                Conectivity += 1 if (P9(dest, line, col) == 0 and P2(dest, line, col) == 1) else 0
                if Conectivity != 1:
                    continue
                # 2 <= BlackNeighboors <= 6
                Neighboors = P2(dest, line, col) + P3(dest, line, col) + \
                             P4(dest, line, col) + P5(dest, line, col) + \
                             P6(dest, line, col) + P7(dest, line, col) + \
                             P8(dest, line, col) + P9(dest, line, col)
                if Neighboors < 2 or Neighboors > 6:
                    continue
                # At least one of P2, P4 and P8 are background
                Neighboors = 0
                Neighboors = P2(dest, line, col) * P4(dest, line, col) * P8(dest, line, col)
                if Neighboors != 0:
                    continue

                # At least one of P2, P6 and P8 are background
                Neighboors = 0
                Neighboors = P2(dest, line, col) * P6(dest, line, col) * P8(dest, line, col)
                if (Neighboors != 0):
                    continue
                # Actual Pixel was deleted
                ThiningContinue = True
                RemPoints.append(cpoint(line, col))

        for it in RemPoints:
            dest[it.x][it.y] = 0
        RemPoints.clear()
        # Second Sub-Iteraction
        for line in range(1, height - 1):
            for col in range(1, width - 1):
                Neighboors = 0
                Conectivity = 0
                # Pixel must be black
                # Connectivity number must be 1;
                Conectivity = 1 if (P2(dest, line, col) == 0 and P3(dest, line, col) == 1) else 0
                Conectivity += 1 if (P3(dest, line, col) == 0 and P4(dest, line, col) == 1) else 0
                Conectivity += 1 if (P4(dest, line, col) == 0 and P5(dest, line, col) == 1) else 0
                Conectivity += 1 if (P5(dest, line, col) == 0 and P6(dest, line, col) == 1) else 0
                Conectivity += 1 if (P6(dest, line, col) == 0 and P7(dest, line, col) == 1) else 0
                Conectivity += 1 if (P7(dest, line, col) == 0 and P8(dest, line, col) == 1) else 0
                Conectivity += 1 if (P8(dest, line, col) == 0 and P9(dest, line, col) == 1) else 0
                if Conectivity != 1:
                    continue
                # 2 <= BlackNeighboors <= 6
                Neighboors = P2(dest, line, col) + P3(dest, line, col) + \
                             P4(dest, line, col) + P5(dest, line, col) + \
                             P6(dest, line, col) + P7(dest, line, col) + \
                             P8(dest, line, col) + P9(dest, line, col)
                if Neighboors < 2 or Neighboors > 6:
                    continue
                # At least one of P2, P4 and P6 are background
                Neighboors = 0
                Neighboors = P2(dest, line, col) * P4(dest, line, col) * P6(dest, line, col)
                if Neighboors != 0:
                    continue
                # At least one of P2, P6 and P8 are background
                Neighboors = 0
                Neighboors = P4(dest, line, col) * P6(dest, line, col) * P8(dest, line, col);
                if Neighboors != 0:
                    continue
                # Actual Pixel was deleted
                ThiningContinue = True
                RemPoints.append(cpoint(line, col))

        for it in RemPoints:
            dest[it.x][it.y] = 0
        RemPoints.clear()

    print("Zhang_Suen - while ended")

    for line in range(height):
        for col in range(width):
            if P1(dest, line, col) == 0:
                dest[line][col] = 255
            else:
                dest[line][col] = 0


class Vertices:
    x = 0.0
    y = 0.0


class RadiusAngle:
    radius = 0.0
    angle = 0.0


def invert(ini, fim):
    i = ini
    f = fim
    ini = f
    fim = i
    return ini, fim


def lineIDDA(img_, yi, xi, yf, xf, v):
    quant = None
    erro = 0
    q = 0
    deltax = xf - xi
    deltay = yf - yi
    vert = Vertices()

    # When yi>yf the line is diagonal to down. For this is
    # necessary invert the points
    # When Deltax= 0 and Deltay  < 0, the line is in vertical
    # to down. For this is necessary invert yi with yf.
    if (yi > yf) or ((deltax == 0) and (deltay < 0)):
        xi, xf = invert(xi, xf)
        yi, yf = invert(yi, yf)
        deltax = xf - xi
        deltay = yf - yi
    x = xi
    y = yi

    # "quant" denotes the maximum number of ploted points
    if abs(deltax) > abs(deltay):
        quant = abs(deltax)
    else:
        quant = abs(deltay)
    get_point = True
    entered = False
    finished = False
    walk = 1000  # clean more pixels.
    while q <= quant and q <= walk:  # While have points to plot
        print(y, x, type(y), type(x))

        if x >= 0 and y >= 0 and x < img_.shape[1] and y < img_.shape[0]:
            print('breaking if', x, y)
            if not entered and img_[y][x] == 0:  # Find a espiral

                entered = True
                if (get_point):  # get the first point.
                    get_point = False
                    vert.x = x
                    vert.y = y
                    v.append(vert)
                img_[y][x] = 255  # Set the color white to avoid reprocessing

        if entered:
            walk -= 1
            if x >= 0 and y >= 0 and x < img_.shape[1] and y < img_.shape[0]:
                img_[y][x] = 255  # Set the color white to avoid reprocessing

        if (deltax >= 0) and (deltay >= 0) and (deltax >= deltay):  # 1 0ct
            print(' 1 0ct', x, y)
            if (erro < 0) or (deltay == 0):
                print('if true:')
                x += 1
                erro = erro + deltay
            else:
                print('else:')
                x += 1
                y += 1
                erro = erro + deltay - deltax
            print(' 1 0ct - DONE', x, y)


        elif (deltax >= 0) and (deltay >= 0) and (deltay > deltax):  # 2 oct
            print(' 2 0ct')
            if erro < 0:
                x += 1
                y += 1
                erro = erro + deltay - deltax
            else:
                y += 1
                erro = erro - deltax

        elif (deltay >= 0) and (deltax < 0) and (-deltax >= deltay):  # 4 oct
            print(' 4 0ct')
            if (erro < 0) or (deltay == 0):
                x -= 1
                erro = erro + deltay
            else:
                x -= 1
                y += 1
                erro = erro + deltax + deltay

        elif (deltay > 0) and (deltax < 0) and (deltay > -deltax):  # 3 oct
            print(' 3 0ct')
            if erro < 0:
                x -= 1
                y += 1
                erro = erro + deltax + deltay
            else:
                y += 1
                erro = erro + deltax

        elif (deltax >= 0) and (deltay < 0) and (deltax >= -deltay):  # 8 oct
            print(' 8 0ct')
            if erro < 0:
                x += 1
                erro = erro - deltay
            else:
                x += 1
                y -= 1
                erro = erro + abs(deltay) - deltax

        elif (deltax >= 0) and (deltay < 0) and (-deltay > deltax):  # 7 oct
            print(' 7 0ct')
            if erro < 0:
                x += 1
                y -= 1
                erro = erro - deltay - deltax
            else:
                y -= 1
                erro = erro - deltax

        elif (deltay < 0) and (deltax < 0) and (-deltay > -deltax):  # 3 oct
            print(' 3 0ct - 2')
            if erro < 0:
                x -= 1
                y -= 1
                erro = erro + deltax - deltay
            else:
                y -= 1
                erro = erro + deltax

        elif (deltay < 0) and (deltax < 0) and (-deltax >= -deltay):  # 4 oct
            print(' 4 0ct - 2')
            if erro < 0:
                x -= 1
                erro = erro - deltay
            else:
                x -= 1
                y -= 1
                erro = erro + deltax - deltay

        print('end if:', y, x)

        q += 1  # number of plotted point
        print('end while:', y, x)

    return v


# ---------------------------------------------------------------------------
def rotation(vert, yp, xp, teta):
    x = (((vert.x - xp) * cos(teta * 3.14159265358 / 180)) - ((vert.y - yp) * sin(teta * 3.14159265358 / 180))) + xp
    y = (((vert.x - xp) * sin(teta * 3.14159265358 / 180)) + ((vert.y - yp) * cos(teta * 3.14159265358 / 180))) + yp

    vert.x = x
    vert.y = y

    return vert


# VERIFY THE CENTRAL PÍXEL
def verify(img_, y, x):
    cont = 0
    for i in range(y - 1, y + 2):
        for j in range(x - 1, x + 2):
            if img_[i][j] == 0:
                cont += 1
    return cont


# FIND THE SPIRAL ORIGEN
def origem(img_, oy, ox):
    lines = int(oy + 100)
    cols = int(ox + 100)
    com_line = int(oy - 100)
    com_col = int(ox - 100)

    for i in range(com_line, lines):
        for j in range(com_col, cols):
            if img_[i][j] == 0:
                if verify(img_, i, j):
                    ox = j
                    oy = i
    return oy, ox


def extractFeats(argv):
    radiusangle = []
    radiusrigin = []
    difradial = []
    ptosoriginal = []
    ptosdesenhada = []
    tremor_relativo = []
    tremor = []
    ra = RadiusAngle()
    raorigin = RadiusAngle()
    vert = Vertices()

    img = cv2.imread(argv[0], cv2.IMREAD_COLOR)
    img1 = cv2.imread(argv[1], cv2.IMREAD_COLOR)

    # Gray scale
    img_ = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, img_ = cv2.threshold(img_, 220, 255, 0)
    Zhang_Suen(img_)

    # Spiral pen
    nx = img.shape[0]  # number of columns
    ny = img.shape[1]  # number of lines/rows

    img1_ = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    ret, img1_ = cv2.threshold(img_, 220, 255, 0)
    Zhang_Suen(img1_)

    yc = img_.shape[1] / 2  # 370;
    xc = img_.shape[0] / 2  # 350;
    # Find the spiral origin.
    yc, xc = origem(img1_, yc, xc)

    print("Line - 379")

    """/////////////////////////////////////////////////////////////////////////"""
    # Get points from spiral
    for j in range(0, 3):  # 3 turns in the spiral.
        vert.y = yc
        vert.x = img_.shape[0] + 350  # pegar a img inteira
        vert = rotation(vert, yc, xc, 1)
        for i in range(0, 360):
            pt_ori = len(ptosoriginal)
            pt_des = len(ptosdesenhada)
            vert = rotation(vert, yc, xc, -1)
            ptosoriginal = lineIDDA(img1_, yc, xc, vert.y, vert.x, ptosoriginal)
            ptosdesenhada = lineIDDA(img_, yc, xc, vert.y, vert.x, ptosdesenhada)
    """/////////////////////////////////////////////////////////////////////////"""
    yc = img_.shape[1] / 2  # 370;
    xc = img_.shape[0] / 2  # 350;

    print("Line - 397")

    """/////////////////////////////////////////////////////////////////////////"""
    # Transformation to polar coordinates
    for i in range(0, len(ptosoriginal)):
        raiz = (ptosoriginal[i].x - xc) * (ptosoriginal[i].x - xc) + (ptosoriginal[i].y - yc) * (ptosoriginal[i].y - yc)
        raorigin.radius = sqrt(raiz)  # computating the radius.
        atangente = (ptosoriginal[i].y - yc) / (ptosoriginal[i].x - xc)
        raorigin.angle = atan(atangente)  # computating the angle. (Radianos)
        radiusrigin.append(raorigin)

    i = 0
    while i < len(ptosdesenhada) and i < len(ptosoriginal):
        raiz = (ptosdesenhada[i].x - xc) * (ptosdesenhada[i].x - xc) + (ptosdesenhada[i].y - yc) * (
                ptosdesenhada[i].y - yc)
        ra.radius = sqrt(raiz)
        atangente = (ptosdesenhada[i].y - yc) / (ptosdesenhada[i].x - xc)
        ra.angle = atan(atangente)
        radiusangle.append(ra)
        i += 1

    print("Line - 418")

    """/////////////////////////////////////////////////////////////////////////"""
    # Calculate the difference between the template and drawed spiral
    dif_rad = 0.0
    prev_rad = radiusrigin[0].radius - radiusangle[0].radius
    count_cross = 0

    ra.radius = abs(prev_rad)
    difradial.append(ra)

    i = 1
    while i < len(ptosdesenhada) and i < len(ptosoriginal):
        dif_rad = radiusrigin[i].radius - radiusangle[i].radius
        ra.radius = abs(dif_rad)
        difradial.append(ra)
        if dif_rad * prev_rad < 0:
            count_cross += 1  # // CROSS THE TEMPLATE
        prev_rad = dif_rad
        i += 1

    """/////////////////////////////////////////////////////////////////////////"""
    # computating the Relative Tremor
    i = 0
    while i < len(ptosdesenhada) and i < len(ptosoriginal):
        raiz = (ptosoriginal[i].x - xc) * (ptosoriginal[i].x - xc) + (ptosoriginal[i].y - yc) * (ptosoriginal[i].y - yc)
        vert.x = (1 - difradial[i].radius / sqrt(raiz)) * ptosdesenhada[i].x
        # cout << vert.x << endl;
        vert.y = (1 - difradial[i].radius / sqrt(raiz)) * ptosdesenhada[i].y
        # cout << vert.y << endl;
        tremor_relativo.append(vert)
        i += 1

    mean_tremor = 0.0
    std_tremor = 0.0
    max_tremor = 0.0
    min_tremor = 10000.0
    count = 0

    i = 0
    while i < len(ptosdesenhada) and i < len(ptosoriginal):
        raiz = sqrt(
            (ptosoriginal[i].x - xc) * (ptosoriginal[i].x - xc) + (ptosoriginal[i].y - yc) * (ptosoriginal[i].y - yc))
        tremor.append(raiz)
        i += 1

    for i in range(DISPLACEMENT, len(tremor)):
        dif = abs(tremor[i] - tremor[i - DISPLACEMENT])
        mean_tremor += dif
        count += 1
        if dif > max_tremor:
            max_tremor = dif
        if dif < min_tremor:
            min_tremor = dif

    mean_tremor /= count

    for i in range(DISPLACEMENT, len(tremor)):
        dif = abs(tremor[i] - tremor[i - DISPLACEMENT])
        std_tremor += pow(dif - mean_tremor, 2.0) / (len(tremor) - DISPLACEMENT)

    """	///////// Extracting features from Tremor //////////"""
    # computating the RMS (Root Mean Square)
    RMS = 0.0
    minRMS = 10e10
    maxRMS = 0.0
    std = 0.0
    min_p = len(ptosdesenhada)
    if min_p > len(ptosoriginal):
        min_p = len(ptosoriginal)

    i = 0
    while i < len(ptosdesenhada) and i < len(ptosoriginal):
        RMS += difradial[i].radius * difradial[i].radius
        if difradial[i].radius * difradial[i].radius > maxRMS:
            maxRMS = difradial[i].radius * difradial[i].radius
        if difradial[i].radius * difradial[i].radius < minRMS:
            minRMS = difradial[i].radius * difradial[i].radius
        i += 1

    RMS /= min_p

    i = 0
    while i < len(ptosdesenhada) and i < len(ptosoriginal):
        std += pow(difradial[i].radius * difradial[i].radius - RMS, 2.0) / len(ptosoriginal)
        i += 0

    std = sqrt(std)

    f = open("RMS.txt", "w")
    f.write(
        f"1:{RMS} 2:{std} 3:{maxRMS} 4:{minRMS} 5:{mean_tremor} 6:{max_tremor} 7:{min_tremor} 8:{std_tremor} 9:{count_cross / count}")
    f.close()
