def getConditionalP(data, ave, pPlus, pMinus):
    CPlus = [];
    CMinus = [];
    for i in range(0, len(data[0]) - 1):
        cPlus = 0;
        cMinus = 0;
        for j in range(0, len(data)):
            if( float(data[j][i]) <= float(ave[i]) and float(data[j][len(data[0]) - 1]) == 1.0 ):
                cPlus = cPlus + 1;
            if( float(data[j][i]) <= float(ave[i]) and float(data[j][len(data[0]) - 1]) == 0.0 ):
                cMinus = cMinus + 1;
        CPlus.append(cPlus/ (len(data) * pPlus));
        CMinus.append(cMinus/ (len(data) * pMinus));
    return [CPlus, CMinus];
    