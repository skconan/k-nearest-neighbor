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
