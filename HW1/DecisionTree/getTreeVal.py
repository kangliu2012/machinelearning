def getTreeNodeVal(data, nd):
    oneCount = 0;
    zeroCount = 0;
    col = len(data[0]) - 1;
    for i in range(0, len(data)):
        if( float(data[i][col]) > 0 ):
            oneCount = oneCount + 1;
        else:
            zeroCount = zeroCount + 1;
    if( oneCount >= zeroCount ):
        nd.res = 1.0;
    else:
        nd.res = 0.0;