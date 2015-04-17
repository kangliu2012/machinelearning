from sortColumn import sortOneColumn;
from getMinSME import getMinSME;

def splitData(data, node):
    minmse = -1.0;
    idx = [];
    dataToSplit = [];
    col = 0;

    for i in range(0, len(data[0]) - 1):
        sortTrainData = sortOneColumn(data, i);
        (idxt, minmset) = getMinSME(sortTrainData);

        if( minmse == -1.0 or minmset < minmse ):
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

