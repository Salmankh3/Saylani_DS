def cent_to_far(c):
    return (9*c/5)+32

def cent_to_kel(c):
    return 273+c
    
def far_to_cent(f):
    return 5*(f-32)/9

def far_to_kel(f):
    c=5*(f-32)/9
    k=c+273
    return k

def kel_to_cent(k):
    return k-273

def kel_to_far(k):
    c = k-273
    f = (9*c/5)+32
    return f