import cv2


class CreateDataSet():
    def __init__(self):
        self.imagesPath = 'C:\\Users\\skconan\\Desktop\\classification_rectangle\\images\\rectangle_training\\'
        self.filePath = 'C:\\Users\\skconan\\Desktop\\classification_rectangle\\src_code\\'
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.imageW = 300
        self.imageH = 300
        self.minCntArea = 500
        self.maxCntArea = 150000
        self.fileType = '.txt'
        self.noOftraning = 8

    def create_file(self, name, dataList):
        name += self.fileType
        while True:
            name = self.filePath + name
            try:
                f = open(name, 'r+')
                cmd = input('Do you want overwrite it (y/n) ')
                if not cmd == 'y':
                    name = input('File name: ')
                    continue
            except FileNotFoundError:
                pass
            f = open(name, 'w+')
            break
        text = ''
        for line in dataList:
            for word in line:
                text += str(word) + " "
            text += '\n'
        print(text)
        f.write(text)
        f.close()
        print('Created ' + str(name))

    def find_features(self, img):
        r, c, ch = img.shape
        img = cv2.resize(img, (self.imageW, self.imageH))
        res = img.copy()
        gray = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY)
        ret, th = cv2.threshold(gray.copy(), 200, 255, 0)
        _, cnts, h = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        print(len(cnts))
        cnt = cnts[-1]
        cntArea = cv2.contourArea(cnt)
        print(cntArea)
        if cntArea < self.minCntArea or cntArea > self.maxCntArea:
            return
        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.04 * peri, True)
        sides = len(approx)
        x, y, w, h = cv2.boundingRect(cnt)
        areaRatio = float(cntArea) / (w * h)
        cx, cy = int(x + w / 2), int(y + h / 2)
        cv2.drawContours(res, cnt, -1, (0, 255, 0), 3)
        cv2.drawContours(res, approx, -1, (0, 0, 205), 5)
        cv2.putText(res, str(int(peri)) + " " + str(sides), (cx, cy),
                    self.font, 0.5, (0, 50, 25), 1, cv2.LINE_AA)

        cv2.imshow('result', res)
        cv2.waitKey(0)
        return [sides, areaRatio]

    def run(self):
        dataList = []
        for no in range(self.noOftraning):
            img = cv2.imread(self.imagesPath+"0"+str(no)+".jpg")
            data = self.find_features(img)
            print( data)
            dataList.append(data)
        self.create_file('trainingSet1',dataList)
if __name__ == '__main__':
    cds = CreateDataSet()
    # data = [[121, 32], [621, 72], [1231, 323]]
    # cds.create_file('test', data)
    cds.run()