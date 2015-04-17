from treeNode import Node;
from createDecisionTree import createDecisionTree;
from getLableFromTestData import getLableFromTestData;

def trainAndTestData(splitedTrainData, splitedTestData, depth):
                     
    decisiontree = Node();
    createDecisionTree(splitedTrainData, decisiontree,depth);
  
    summse = 0.0;
    for i in range(0, len(splitedTestData)):
        label = getLableFromTestData(splitedTestData[i], decisiontree);
        labelT = float(splitedTestData[i][57]);
        diff = label - labelT;
        summse = summse + diff * diff;
    print "MSE = " + str(summse/len(splitedTestData));