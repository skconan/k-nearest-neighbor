from create_data_set import CreateDataSet
from knn_classification_rect import KNN

def main():
    cds = CreateDataSet()
    data = [[121,32],[621,72],[1231,323]]
    cds.create_file('test',data)
    
if __name__ =='__main__':
    main()