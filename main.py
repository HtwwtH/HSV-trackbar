import cv2
import numpy as np
import time

def Show(name, img):
    cv2.namedWindow(name, cv2.WINDOW_AUTOSIZE)
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def imageProc(imgIn):           # препроцессинг картинки
    img = imgIn
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, img = cv2.threshold(img,227,255,cv2.THRESH_BINARY)

    return img

def find_object(imgIn):
    img = imgIn
    hsv_min = np.array((0, 0, 0), np.uint8)     #только объект
    hsv_max = np.array((162, 164, 251), np.uint8)
    only_hsv = cv2.inRange(img, hsv_min, hsv_max)
    mask = cv2.bitwise_not(only_hsv)
    return mask

def main():

    img = cv2.imread('image.jpg')
    Show('Original image', img)

    img_bw = imageProc(img.copy())
    Show('B&w image', img_bw)

    t0 = time.time()
    mask = find_object(img.copy())              #получить маску, которая затрет объект
    print('Time processing find_object {}'.format(time.time() - t0))

    t0 = time.time()
    output = cv2.bitwise_and(cv2.bitwise_not(img_bw), cv2.bitwise_not(img_bw), mask=mask)     #здесь объект уже затерт
    print('Time processing bitwise_and {}'.format(time.time()-t0))

    Show('Without object', output)

    bwimg = cv2.bitwise_not(output)           #инвертируем ч/б, если надо
    Show('B&w output image', bwimg)

    _, contours, hierarchy = cv2.findContours(output.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    result_img = img.copy()
    # cv2.drawContours(result_img, contours, -1, (255, 0, 0), 3, cv2.LINE_AA, hierarchy, 1)     #контуры найденных
    for cnt in contours:
        rect = cv2.minAreaRect(cnt)  # поиск прямоугольника
        box = cv2.boxPoints(rect)  # вершины прямоугольника
        box = np.int0(box)  # округление координат
        cv2.drawContours(result_img, [box], 0, (255, 0, 0), 2)  # рисуем прямоугольник
    Show('Result image', result_img)

if __name__ == '__main__':
    main()

