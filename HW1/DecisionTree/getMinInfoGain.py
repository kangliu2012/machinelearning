import math;
from splitDataRandomly import splitDataRandomly;
from getDataByComma import getDataByComma;
from sortData import sortData;

def zeroOrLog(p):
    if( p == 0.0):
        return 0;
    else:
        return math.log(p, 2);

def getMinInfoGain(data, col):
    oneCounts = 0;
    zeroCounts = 0;
    for i in range(0, len(data)):
        if( data[i][len(data[0]) - 1] == "1"):
            oneCounts = oneCounts + 1;
        elif( data[i][len(data[0]) - 1] == "0"):
            zeroCounts = zeroCounts + 1;
    oneCountsT = 0;
    zeroCountsT = 0;
    curVal = float(data[0][col]);
    gainInfo = - 100.0;
    idx = 0;
    
    for i in range(0, len(data)):
        if( not ( float(data[i][col]) == curVal ) ):
            p1 = float((oneCountsT + zeroCountsT)) / float(len(data));
            p2 = float(oneCountsT) / float(oneCountsT + zeroCountsT);
            p3 = 1 - p2;
            
            p4 = 1 - p1;
            p5 = float(oneCounts) / float(oneCounts + zeroCounts);
            p6 = 1 - p5;
                
            gainInfoT = p1 * ( p2 * zeroOrLog(p2) + p3 * zeroOrLog(p3) ) + p4 * ( p5 * zeroOrLog(p5) + p6 * zeroOrLog(p6) );
            if(gainInfoT > gainInfo):
                gainInfo = gainInfoT;
                idx = i - 1;
                curVal = float(data[i][col]);
                
        if( data[i][len(data[0]) - 1] == "1"):
            oneCountsT = oneCountsT + 1;
            oneCounts = oneCounts - 1;
        elif( data[i][len(data[0]) - 1] == "0"):
            zeroCountsT = zeroCountsT + 1;
            zeroCounts = zeroCounts - 1;
    
    return (gainInfo, idx);
         
# traindata = getDataByComma("Data//spambase.txt");
# (splitedTrainData, splitedTestData) = splitDataRandomly(traindata);
# for i in range (0,58):
#     sortTrainData = sortData(splitedTrainData, i);
#     (gainInfo, idx) = getMinInfoGain(sortTrainData, i);
#     print gainInfo;

