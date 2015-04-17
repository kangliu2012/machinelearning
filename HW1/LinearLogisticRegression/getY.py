def getY(data):
    res = [];
    for i in range(0, len(data)):
       d = [];
       d.append(data[i][len(data[0]) - 1]);
       res.append(d);
    return res;
 