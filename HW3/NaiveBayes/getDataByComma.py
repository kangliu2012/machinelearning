'''
Created on Mar 28, 2015

@author: kangliu
'''
#!/usr/bin/python

def getDataByComma(filedir):
    f = open(filedir, 'r');

    res = [];

    while (1):
        line = str(f.readline())
        
        if not line:
            break;
        
        st = line.split(",")
        
        l = [];
        for i in st:
            l.append(i);
        l[len(l) - 1] = l[len(l) - 1].replace("\n","");
        res.append(l)
        
    f.close()
    return res;



