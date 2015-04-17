def errorCount(data, w):
    errorCount = 0;
    for i in range(0, len(data)):
        val = w[0];
        for j in range(1, 5):
            val = val + w[j]*data[i][j - 1];
        if( (val >= 0.0 and data[i][4] == -1.0) or (val < 0.0 and data[i][4] == 1.0)):
            errorCount = errorCount + 1;
    return errorCount;