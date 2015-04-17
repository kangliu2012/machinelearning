from getDataByComma import getDataByComma;
from splitDataRandomly import splitDataRandomly;
from trainAndTestData import trainAndTestData;

####################################################
##################train data#########################
####################################################
traindata = getDataByComma("Data//spambase.txt");

for i in range(0, 5):
    (splitedTrainData, splitedTestData) = splitDataRandomly(traindata);
    trainAndTestData(splitedTrainData, splitedTestData, i);

# depth = 1, MSE = 0.234782608696
# depth = 2, MSE = 0.230434782609
# depth = 3, MSE = 0.117391304348
# depth = 4, MSE = 0.102173913043
# depth = 5, MSE = 0.113043478261
