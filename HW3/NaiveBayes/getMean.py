def getMean(data):
    ave = [];
    for i in range(0, len(data[0]) - 1):
        s = 0.0;
        for j in range(len(data)):
            s = s + float(data[j][i]);
        ave.append(s/len(data));
    return ave;