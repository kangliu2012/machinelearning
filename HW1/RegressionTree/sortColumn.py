import copy;

def sortOneColumn(data, col):
    newdata = copy.deepcopy(data); 
    for row1 in range(0, len(data[:]) - 1):
        for row2 in range(row1 + 1, len(data[:])):
            if( newdata[row1][col] > newdata[row2][col]):
                newrow = copy.deepcopy(newdata[row1]);
                newdata[row1] = copy.deepcopy(newdata[row2]);
                newdata[row2] = copy.deepcopy(newrow);
    return newdata;




