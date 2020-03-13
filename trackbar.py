
import numpy as np
import cv2

class EdgeFinder:
    def __init__(self, image):
        self.image = image
        self.h1 = 0         # минимум диапазона
        self.s1 = 0
        self.v1 = 0
        self.h2 = 255       # максимум диапазона
        self.s2 = 255
        self.v2 = 255

        def onchange_h1(pos):
            self.h1 = pos
            self._render()

        def onchange_s1(pos):
            self.s1 = pos
            self._render()

        def onchange_v1(pos):
            self.v1 = pos
            self._render()

        def onchange_h2(pos):
            self.h2 = pos
            self._render()

        def onchange_s2(pos):
            self.s2 = pos
            self._render()

        def onchange_v2(pos):
            self.v2 = pos
            self._render()

        cv2.namedWindow('settings', cv2.WINDOW_NORMAL)
        cv2.createTrackbar('h1', 'settings', 0, 255, onchange_h1)
        cv2.createTrackbar('s1', 'settings', 0, 255, onchange_s1)
        cv2.createTrackbar('v1', 'settings', 0, 255, onchange_v1)
        cv2.createTrackbar('h2', 'settings', 0, 255, onchange_h2)
        cv2.createTrackbar('s2', 'settings', 0, 255, onchange_s2)
        cv2.createTrackbar('v2', 'settings', 0, 255, onchange_v2)

        self._render()
        print("Adjust the parameters as desired.  Hit any key to close.")

        cv2.waitKey(0)
        cv2.destroyWindow('settings')


    def _render(self):

        print('{} {} {}, {} {} {}'.format(self.h1, self.s1, self.v1, self.h2, self.s2, self.v2))
        h_min = np.array((self.h1, self.s1, self.v1), np.uint8)
        h_max = np.array((self.h2, self.s2, self.v2), np.uint8)
        thresh = cv2.inRange(self.image, h_min, h_max)
        thresh = cv2.resize(thresh, (960, 540))
        cv2.imshow('result', thresh)



def main():

    img = cv2.imread('image.jpg')
    EdgeFinder(img)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()