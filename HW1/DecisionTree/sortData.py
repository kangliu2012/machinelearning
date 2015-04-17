import copy;

def sortData(data, col):
    res = copy.copy(data);
    for i in range(0, len(res) - 1):
        for j in range(i + 1, len(res)):
            if( res[i][col] > res[j][col]):
                newline = copy.copy(res[i]);
                res[i] = copy.copy(res[j]);
                res[j] = copy.copy(newline);
    return res;