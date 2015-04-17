from getDataBySplitSpace import getDataBySplitSpace;
from treeNode import Node;
from createRegressionTree import createRegressionTree;
from getLableFromTestData import getLableFromTestData;

def trainAndTestData(trainData, testData):
    traindata = getDataBySplitSpace("Data//housing_train.txt", 14)
    regressiontree = Node();
    Tree_Depth = 3;
    createRegressionTree(traindata, regressiontree,Tree_Depth);
    
    summse = 0.0;
    for i in range(0, len(testData)):
        diff = getLableFromTestData(testData[i], regressiontree) - testData[i][13];
        summse = summse + diff * diff;
    return summse/len(testData);