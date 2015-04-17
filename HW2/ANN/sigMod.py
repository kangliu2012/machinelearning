import math
def sigMod(val):
    e = 2.7182818;
    if( float(val) > 500.0):
        return 1.0;
    res = 1/ (1 + 1/math.pow(e, val));
    return res;
