
class GetData():
    PATH = 'C:\\Users\\skconan\\Desktop\\classification_shape\\images\\'
    font = cv2.FONT_HERSHEY_SIMPLEX
    def __init__(self,path):
        pass
    def main():
        global PATH, font
        img = cv2.imread(PATH + 'rectangle.jpg', 1)
        r, c, ch = img.shape
        img = cv2.resize(img, (int(c / 2), int(r / 2)))
        rows, cols, ch = img.shape
        resCnt = img.copy()
        gray = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY)
        ret, th = cv2.threshold(gray.copy(), 250, 255, 0)
        _, cnts, h = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        for c in cnts:
            if cv2.contourArea(c) < 1500:
                continue
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.04 * peri, True)
            sides = len(approx)
            x, y, w, h = cv2.boundingRect(c)
            cx, cy = int(x + w / 2), int(y + h / 2)

            cv2.drawContours(resCnt, c, -1, (0, 255, 0), 3)
            cv2.drawContours(resCnt, approx, -1, (0, 0, 205), 5)
            cv2.putText(resCnt, str(int(peri)) + " " + str(sides), (cx, cy),
                        font, 0.5, (0, 50, 25), 1, cv2.LINE_AA)

        res = img.copy()

        cv2.imshow('resultCnt', resCnt)
        cv2.waitKey(0)
