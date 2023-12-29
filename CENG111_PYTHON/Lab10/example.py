import pdb
def isOrdered(l):
    for i in range(len(l)):
        if l[i]>l[i+1]:
            return False
    
    return True

isOrdered([1,2,3])