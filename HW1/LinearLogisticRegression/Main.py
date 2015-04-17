from getDataBySplitSpace import getDataBySplitSpace;
from getX import getX;
from getY import getY;
import numpy as np;
import numpy;
from logisticFunc import logisticFunc;

####################################################
##################train data#########################
####################################################
traindata = getDataBySplitSpace("Data//housing_train.txt", 14);
################################################
################################################
##Linear Regression
Xtrain = np.array(getX(traindata));
Ytrain = np.array(getY(traindata));
xtrainT = numpy.transpose(Xtrain); 
w = np.dot(np.dot(np.linalg.inv(np.dot(xtrainT,Xtrain)),xtrainT), Ytrain);
 
testdata = getDataBySplitSpace("Data//housing_test.txt", 14);
Xtest = np.array(getX(testdata));
Ytest = np.array(getY(testdata));
 
err = np.dot(Xtest, w) - Ytest
mse = 0.0;
for i in range(0, len(err)):
    mse = mse + err[i][0] * err[i][0];
mse = mse / len(err);
 
print mse;
#mse = 24.3
    
#################################################
#################################################
###Logistic Regression
traindata = getDataBySplitSpace("Data//housing_train.txt", 14);
Xtrain = np.array(getX(traindata));
XtrainG = [];
for i in range(0, len(Xtrain)):
    res = [];
    for j in range(0, len(Xtrain[0])):
        res.append( logisticFunc(Xtrain[i][j]));
    XtrainG.append(res);

YtrainG = np.array(getY(traindata));
XtrainGT = numpy.transpose(XtrainG);
w = np.dot(np.dot(np.linalg.inv(np.dot(XtrainGT,XtrainG)),XtrainGT), YtrainG);

testdata = getDataBySplitSpace("Data//housing_test.txt", 14);
Xtest = np.array(getX(testdata));
XtestG = [];
for i in range(0, len(Xtest)):
    res = [];
    for j in range(0, len(Xtest[0])):
        res.append( logisticFunc(Xtest[i][j]));
    XtestG.append(res);
    
YtestG = np.array(getY(testdata));

err = np.dot(XtestG, w) - YtestG
mse = 0.0;
for i in range(0, len(err)):
    mse = mse + err[i][0] * err[i][0];
mse = mse / len(err);
#mse = 19.3
