def getMinSME(data):
   
    minmse = -1.0;
    idx = 0;
    for i in range(0, len(data) - 1):
        ave1 = 0.0;
        for j in range(0, i + 1):
            ave1 = ave1 + data[j][len(data[0]) - 1];
        ave1 = ave1 / float(i + 1);
        sum1 = 0.0;
        for j in range(0, i + 1):
            diff = data[j][len(data[0]) - 1] - ave1;
            sum1 = sum1 + diff * diff;
        
        ave2 = 0.0;
        for j in range(i + 1, len(data)):
            ave2 = ave2 + data[j][len(data[0]) - 1];
        ave2 = ave2 / float(len(data) - i - 1);
        sum2 = 0.0;
        for j in range(i + 1, len(data)):
            diff = data[j][len(data[0]) - 1] - ave2;
            sum2 = sum2 + diff * diff;

        msesum = (sum1 + sum2) / len(data);
        if( minmse == -1.0 or msesum < minmse ):
            minmse = msesum;
            idx = i;
    return (idx, minmse);
        