from getDataByComma import getDataByComma;
from splitDataRandomly import splitDataRandomly;
from simpleBernoulli import simpleBernoulli;

####################################################
##################train data#########################
####################################################
spamdata = getDataByComma("Data//spambase.txt");
for i in range(0, 10):
    [traindata, testdata] = splitDataRandomly(spamdata);
    corr = simpleBernoulli(traindata, testdata);
    print corr;
