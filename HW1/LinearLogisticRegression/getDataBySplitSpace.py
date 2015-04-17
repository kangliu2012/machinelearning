'''
Created on Mar 28, 2015

@author: kangliu
'''
#!/usr/bin/python

def getDataBySplitSpace(filedir,num):
    
    f = open(filedir, 'r');

    res = [];

    while 1:
        
        line = str(f.readline())
        if not line:
            break
        
        t = "";
        b = True;
        l = [];
        
        for i in line:
            if (i== " ") or (i == "\n"):
                if b == False:
                    l.append(float(t));
                    t = "";
                    b = True;
            else:
                if b == True:
                    b = False;
                t = t + i;    
    
        if b == False:
            l.append(t);
        
        if len(l) == num:
            res.append(l);
        
    f.close()
    return res;
