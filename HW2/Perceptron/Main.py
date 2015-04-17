from getDataBySplitTab import getDataBySplitTab;
from errorCount import errorCount;
import random;

print ;

trainData = getDataBySplitTab("Data//perceptron.txt", 5);

#learningRate = float(random.randrange(0, 1000))/1000.0;
learningRate = 0.4;

#w =[-12, 5, 4, 6, 6.0];
w =[-11.2, 3, 4.7, 6.7, 8.9];

minerr = 1000;
step = 0;

for i in range(0, 100):
    val = w[0];
    for j in range(1, 5):
        val = val + w[j] * trainData[i][j - 1];
    if( val > 0):
        val = 1.0;
    else:
        val = -1.0;
    w[0] = w[0] + learningRate * (trainData[i][4] - val);
    for k in range(1, 5):
        if( val > 0):
            val = 1.0;
        else:
            val = -1.0;
        w[k] = w[k] + learningRate * (trainData[i][4] - val) * trainData[i][k - 1];
    err = errorCount(trainData, w);
    if( err < minerr ):
        step = i;
        minerr = err;

#print step;
print minerr;
              
