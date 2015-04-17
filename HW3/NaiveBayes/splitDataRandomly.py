import random;

def splitDataRandomly(data):
    resTrainData = [];
    resTestData = [];
    randomdata = generateRandom(len(data));
    div = len(data) / 10;
    for i in range(0, div):
        resTestData.append(data[randomdata[i]]);
    for i in range(div, len(data)):
        resTrainData.append(data[randomdata[i]]);
    return (resTrainData, resTestData);

def generateRandom(length):
    res = [];
    while(True):
        if( len(res) == length ):
            return res;
        val = random.randint(0, length - 1);
        if( not Contains(res, val) ):
            res.append(val);

def Contains(res, val):
    for i in range(0, len(res)):
        if( res[i] == val ):
            return True;
    return False;

