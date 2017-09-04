import numpy as np
import cv2
import math
import operator
import random

class KNN:
    def __init__(self):
        self.imagesPath = 'C:\\Users\\skconan\\Desktop\\classification_rectangle\\images\\rectangle_training\\'
        self.filePath = 'C:\\Users\\skconan\\Desktop\\classification_rectangle\\src_code\\'
        self.fileType = '.txt'
        self.trainingSet, self.testSet = self.get_data_set()
        self.sizeOfTraning = len(self.trainingSet)
        self.sizeOfTest = len(self.testSet)
        # Number of traningSet around testSet
        self.k = 3
        self.accuracy = 0
    def read_file(self,name):
        data = []
        name += self.fileType
        name = self.filePath + name
        print(name)
        f = open(name, 'r')
        while True:
            line = f.readline()
            if line == '':
                break
            cols = line.split(' ')
            row = [int(cols[0]),float(cols[1]),bool(cols[2]=='True'),cols[3]]
            # print(row)
            data.append(row)
        return data
    
    def get_data_set(self):
        data = self.read_file('trainingSet1')
        trainingSet = []
        testSet = []
        for d in data:
            rand = random.random()
            if rand >= 0.7:
                testSet.append(d)
            else :
                trainingSet.append(d)
        print(testSet)
        print("")
        print(trainingSet)
        return trainingSet,testSet

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
        pass

if __name__=='__main__':
    knn = KNN()
    # knn.read_file()