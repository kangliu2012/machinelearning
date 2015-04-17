def getPLabel(data):
    pPlus = 0.0;
    pMinus = 0.0;
    for i in range(0, len(data)):
        if( float(data[i][len(data[0]) - 1]) == 1.0 ):
            pPlus = pPlus + 1;
        else:
            pMinus = pMinus + 1;
    return[pPlus / len(data), pMinus / len(data)];