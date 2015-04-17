def getTreeNodeVal(data, nd):
    ave = 0.0;
    col = len(data[0]) - 1;
    for i in range(0, len(data)):
        ave = ave + data[i][col];
    
    ave = ave / len(data);
    nd.res = ave;