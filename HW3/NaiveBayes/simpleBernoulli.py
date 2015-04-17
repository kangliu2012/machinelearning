from getMean import getMean;
from getPLabel import getPLabel;
from getConditionalP import getConditionalP;

def simpleBernoulli(traindata,testdata):
    ave = getMean(traindata);
    [pPlus, pMinus] = getPLabel(traindata);
    [CPlus, CMinus] = getConditionalP(traindata, ave, pPlus, pMinus);
    corr = 0;
    for i in range(0,  len(testdata)):
        proportion = 1;
        for j in range(len(testdata[0]) - 1):
            if( float(testdata[i][j]) <= float(ave[j]) ):
                proportion = proportion * ( CPlus[j] / CMinus[j]);
            else:
                proportion = proportion * ( (1 - CPlus[j]) / (1 - CMinus[j]));
        proportion = proportion * (pPlus / pMinus);
        
        if( proportion >= 1 and float(testdata[i][len(testdata[0]) - 1]) == 1.0):
            corr = corr + 1;
        if( proportion < 1 and float(testdata[i][len(testdata[0]) - 1]) == 0.0):
            corr = corr + 1;   
    
    return float(corr) / float(len(testdata));
