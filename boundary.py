'''
This script takes a simplicial complex K and positive integer p
and returns the pth boundary operator on the chain complex of K
in matrix form, where the ijth entry of the matrix is the integer
coordinant of the image of the ith basis element of C_p(K) for 
the jth element of C_{p-1}(K).
'''


import numpy as np

def boundary(K,p):
    p += 1
    CpK = []
    CqK = []
    for simplex in K:
        if len(np.nonzero(simplex)[0]) == p:
           CpK.append(simplex)
        elif len(np.nonzero(simplex)[0]) == p-1:
           CqK.append(simplex)
    CpK = np.array(CpK)
    CqK = np.array(CqK)
    A = np.zeros((len(CpK),len(CqK)))    
        
    for i in xrange(len(CpK)):
        sig = CpK[i]
        v = np.nonzero(sig)[0]
        bdry = []
        for j in xrange(len(v)):
            bdry.append(np.array(list(sig)))
            bdry[j][v[j]] = 0
            print j
            print bdry[j] 
            bdry[j] = ((-1)**j)*bdry[j]
        bdry = np.array(bdry)
        for j in xrange(len(bdry)):
            chain = bdry[j]
            for q in xrange(len(CqK)):

                if (np.nonzero(chain)[0] == np.nonzero(CqK[q])[0]  ).all():
                   ind = np.nonzero(chain)[0][0]
                   A[i,q] = chain[ind]/CqK[q,ind]
                   break


    return A
    


K = np.array([[1,1,0,0],[0,1,1,0],[0,0,1,1],[-1,0,0,-1],[1,0,0,0],
     [0,1,0,0],[0,0,1,0],[0,0,0,1]])

print boundary(K,2)


'''
def boundary(K,p):
    K_p = set([])
    for sig in K:
        print sig
        t = 0
        for i in sig:
            if i != 0:
                t += 1
        print t
        if t >= p:
            A = [0 for i in range(len(sig))]
            for i in range(t-1):
                count = 0
                for j in range(len(sig)):
                    if sig[j]==0:
                        A[j]=0
                    elif count == i:
                        A[j] == 0
                        count += 1
                    else:
                        A[j] == sig[j]
                        count+=1
                print A
'''                    
                
                    
                            
            
            

'''

def main():
    K = [[1,1,0],[1,0,1],[0,1,1]]
    boundary(K,1)


main()
'''    

