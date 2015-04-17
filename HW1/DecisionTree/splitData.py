from sortData import sortData;
from getMinInfoGain import getMinInfoGain;

def splitData(data, node):
    minmse = -100.0;
    idx = 0;
    dataToSplit = [];
    col = 0;
    
    for i in range(0, len(data[0]) - 1):
        sortTrainData = sortData(data, i);
        (minmset, idxt) = getMinInfoGain(sortTrainData, i);
        if( minmse == -100.0 or minmset > minmse ):
            minmse = minmset;
            idx = idxt;
            col = i;
            dataToSplit = sortTrainData;
    
    leftSplitData = [];
    rightSplitData = [];
    for i in range(0, idx + 1):
        leftSplitData.append(dataToSplit[i]);
    
    for i in range(idx + 1, len(dataToSplit)):
        rightSplitData.append(dataToSplit[i]); 
        
    node.val = dataToSplit[idx][col];
    node.col = col;
    node.depth = node.depth + 1;
    
    return (leftSplitData, rightSplitData, node);
