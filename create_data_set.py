import cv2


class CreateDataSet():
    font = cv2.FONT_HERSHEY_SIMPLEX

    def __init__(self):
        self.imagesPath = 'C:\\Users\\skconan\\Desktop\\classification_shape\\images\\'
        self.filePath = 'C:\\Users\\skconan\\Desktop\\classification_shape\\images\\'
        self.imageW = 300
        self.imageH = 300
        self.minCntArea = 100
        self.maxCntArea = 500

    def create_file(self, name, dataList):
        while True:
            name = self.filePath+name
            try:
                f = open(name, 'r+')
                cmd = input('Do you want overwrite it (y/n) ')
                if not cmd == 'y':
                    name = input('File name: ')
                    continue

            except ValueError:
                f = open(name, 'r+')
            f = open(name, 'w+')
            break
        text = ''
        for line in dataList:
            for word in line:
                text += str(word) + " "
            text += '\n'
        print text
        f.write(text)
        f.close()
        print('Finish')

    def find_features(self,img):
        r, c, ch = img.shape
        img = cv2.resize(img, (self.imageW, self.imageH))
        res = img.copy()
        gray = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY)
        ret, th = cv2.threshold(gray.copy(), 250, 255, 0)
        _, cnts, h = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        data = []
        for c in cnts:
            if cv2.contourArea(c) < self.minCntArea or cv2.contourArea(c) > self.maxCntArea:
                continue
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.04 * peri, True)
            sides = len(approx)

            x, y, w, h = cv2.boundingRect(c)
            cx, cy = int(x + w / 2), int(y + h / 2)

            cv2.drawContours(res, c, -1, (0, 255, 0), 3)
            cv2.drawContours(res, approx, -1, (0, 0, 205), 5)
            cv2.putText(resCnt, str(int(peri)) + " " + str(sides), (cx, cy),
                        font, 0.5, (0, 50, 25), 1, cv2.LINE_AA)

            data.append((sides))

        cv2.imshow('result', resCnt)
        cv2.waitKey(0)
