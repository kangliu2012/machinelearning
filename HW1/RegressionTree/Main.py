from getDataBySplitSpace import getDataBySplitSpace;
from getLableFromTestData import getLableFromTestData;
from createRegressionTree import createRegressionTree;
from treeNode import Node;
from splitDataTenFold import splitDataTenFold;
from trainAndTestData import trainAndTestData;

####################################################
##################train data#########################
####################################################
traindata = getDataBySplitSpace("Data//housing_train.txt", 14)
regressiontree = Node();
Tree_Depth = 6;
createRegressionTree(traindata, regressiontree,Tree_Depth);

####################################################
##################test data#########################
####################################################
testdata = getDataBySplitSpace("Data//housing_test.txt", 14)
 
summse = 0.0;
for i in range(0, len(testdata)):
    diff = getLableFromTestData(testdata[i], regressiontree) - testdata[i][13];
    summse = summse + diff * diff;
print "MSE = " + str(summse/len(testdata));
   
#tree depth     mse
#    0         34.51
#    1         25.57
#    2         23.33
#    3         18.94
#    4         14.67
#    5         15.35
#    6         15.70
#    7         14.98
#    8         14.59

(splitedTrainData, splitedTestData) = splitDataTenFold(traindata);
mse = [];
for i in range(0, 10):
    mse.append( trainAndTestData(splitedTrainData[i], splitedTestData[i]) );
print mse;

#[8.266582218082393, 10.828917996387839, 5.669411229447007, 63.74731956701211, 36.81420207477575, 32.428380924978825, 7.063406032435993, 8.165464244836336, 6.821513928731619, 4.9104501924044754]

