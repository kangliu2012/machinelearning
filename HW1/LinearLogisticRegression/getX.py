def getX(data):
    X = [];
    for i in range(0, len(data)):
        r = [];
        for j in range(0, len(data[0]) - 1):
            r.append(data[i][j]);
        X.append(r);
    return X;
