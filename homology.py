import boundary 
import reduction
import numpy as np



def Homology(K,p):
    A_p = boundary.boundary(K,p)
    #q is p+1
    A_q = boundary.boundary(K,p+1)
    A_p = reduction.red_alg(A_p)
    A_q = reduction.red_alg(A_q)

    m_p,n_p = np.shape(A_p)
    m_q,n_q = np.shape(A_q)

    Z_p = n_p - len(np.nonzero(A_p)[1])
    W_p = len(np.nonzero(A_q)[0])
    
    H_pK = 'Z^'+str(Z_p-W_p) +'+'
    for i in xrange(m_q):
        if A_q[i,i] != 0:
           H_pK += 'Z/'+str(A_q[i,i])
        else: 
           break

    print 'H_'+str(p)+'(K)='+ H_pK

K = np.array([[1,1,0,0],[0,1,1,0],[0,0,1,1],[-1,0,0,-1],[1,0,0,0],
             [0,1,0,0],[0,0,1,0],[0,0,0,1]])

Homology(K,1)



