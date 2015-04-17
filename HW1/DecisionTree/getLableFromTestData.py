import copy;

def getLableFromTestData(testpoint, treenode):
    ndt = copy.copy(treenode);
    while(ndt.col != None):
        if( float(testpoint[ndt.col]) <= float(ndt.val) ):
            ndt = ndt.left;
        else:
            ndt = ndt.right;
    return ndt.res;
        