import numpy as np
import cv2
import math
import operator

class KNN:
    def __init__(self):
        pass
        self.trainingSet = []
        self.sizeOfTraning = len(self.trainingSet)
        self.testSet = []
        self.sizeOfTest = len(self.testSet)
        # Number of traningSet around testSet
        self.k = 3
        self.accuracy = 0
    def euclidean_distance(self, instance1, instance2):
        distance = 0
        # number of attributes
        size = len(instance1) - 1
        for attNO in range(size):
            distance += pow((instance1[attNO] - instance2[attNO]), 2)
        return math.sqrt(distance)

    def get_neighbours(self, testInstance):
        distances = []
        # tnsNO = training set number
        for tnsNO in range(self.sizeOfTraning):
            dist = self.euclidean_distance(
                testInstance, self.trainingSet[tnsNO])
            distances.append((self.trainingSet[tnsNO], dist))
        distances.sort(key=operator.itemgetter(1))
        neighbours = []
        for neighbourNO in range(self.k):
            neighbours.append(distances[neighbourNO][0])
        return neighbours
    
    def get_answer(self,neighbours):
        class_vote={}
        for neighbour in neighbours:
            response = neighbour[-1]
            if response in class_vote:
                class_vote[response] += 1
            else:
                class_vote[response] = 1
        vote_sort = sorted(class_vote.items(), key=operator, reverse=True)
        return vote_sort[0][0]

    def get_accuracy(predictions):
        # test set number
        correct = 0
        for tsNO in range(self.sizeOfTest):
            if self.testSet[tsNO][-1] is predictions[tsNO]:
                correct += 1.0
        return (correct/self.sizeOfTest)*100.0
    
    def run():

class GetData():
    PATH = 'C:\\Users\\skconan\\Desktop\\classification_shape\\images\\'
    font = cv2.FONT_HERSHEY_SIMPLEX
    def __init__(self,path):

    def find_shape(cnt, req):
        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.04 * peri, True)
        if len(approx) == 3 and req == 'tri':
            return True
        elif len(approx) == 4 and req == 'rect':
            return True
        elif len(approx) >= 10 and req == 'cir':
            return True
        elif len(approx) == req:
            return True
        return False


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


if __name__ == '__main__':
    main()
