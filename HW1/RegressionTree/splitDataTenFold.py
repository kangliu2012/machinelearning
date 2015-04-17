def splitDataTenFold(data):
    resTrainData = [];
    resTestData = [];
    div = len(data) / 10;
    for i in range(0, 10):
        trainData = [];
        testData = [];
        for j in range(0, len(data)):
            if( j >= (i * div) and j <= (i + 1) * div ):
                testData.append(data[j]);
            else:
                trainData.append(data[j]);
        resTrainData.append(trainData);
        resTestData.append(testData);
    return (resTrainData, resTestData);
        