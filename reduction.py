'''
This script performs the reduction algorithm given in chapter 2 
of Munkres' Elementary Algebraic Topology.  Given an integer 
matrix (in this case, a matrix of the homomorphism
\delta_p: C_p(K) --> C_{p-1}(K)), this script performs row and 
column operations on the matrix in order to bring it into "normal
form", where all entries except for those on a main diagonal are 
0.
'''




import numpy as np
import math
import boundary 

def findMin(A):
    m,n = np.shape(A)
    min = 1000
    for i in xrange(m):
        for j in xrange(n):
            if math.fabs(A[i,j]) < math.fabs(min):            
               if A[i,j] != 0:
                  min = A[i,j]
                  min_i = i
                  min_j = j
              
    print min_i,min_j
    return min,min_i,min_j

def col_op(A,i,k,j,q):
    print 'row operation'
    #q = int(A[k,j])/int(A[i,j])
    #r = int(A[k,j])%int(A[i,j])
    A[:,k] = A[:,k] - q*A[:,j]
    print A
    return A

def row_op(A,i,k,j,q):
    print 'column operation'
    #q = int(A[i,k])/int(A[i,j])
    A[k,:] = A[k,:] -  q*A[i,:]
    print A
    return A

def is_diag(A):
    m,n = np.shape(A)
    diag = True
    for i in xrange(m):
        for j in xrange(n):
            if i != j and A[i,j] != 0:
               diag = False
               break
        if not diag: 
           break
    
    return diag


def reduce(A):
    m,n = np.shape(A)
    print m,n
    print is_diag(A)
    done = False
    a,i,j = findMin(A)
    for k in xrange(n):
        if A[i,k] % a != 0:
           q = int(A[i,k])/int(a)
           A = col_op(A,i,k,j,q)
           done = True
           break
    if not done:
       for k in xrange(m):
           if A[k,j] % a != 0:
              q = int(A[k,j])/int(a)
              A = row_op(A,i,k,j,q)
              done = True
              break
    if not done:
       quit = False
       for s in xrange(m):
           for t in xrange(n):
               if int(A[s,t]) % int(a) != 0:
                  q = int(A[s,j]) / int(a)
                  A[s,:] = A[s,:] - q*A[i,:]
                  A[i,:] = A[i,:] + A[s,:]
                  quit = True
                  break
           if quit:
              break
    a,i,j = findMin(A)
    if div_mat(a,A):
       v = A[i,:]
       A[i,:] = A[0,:]
       A[0,:] = v
       v = A[:,j]
       A[:,j] = A[:,0]
       A[:,0] = v
       for i in xrange(1,m):
           q = A[i,0] / a
           A[i,:] = A[i,:] - q*A[0,:]
       for j in xrange(1,n):
           q = A[0,j] / a
           A[:,j] = A[:,j] - q*A[:,0]
    return np.abs(A)
    
def div_mat(a,A):
    m,n = np.shape(A)
    for i in xrange(m):
        for j in xrange(n):
            if A[i,j] % a != 0:
               return False
    return True               




def red_alg(A):
    m,n = np.shape(A)
    print 'm,n',m,n
    p = min([m,n])
    t = 0
    while t < p:
        print 't=',t
        if is_diag(A):
           break
        A[t:,t:] = reduce(A[t:,t:])
        incr = True
        for l in xrange(t,p):
            if l>t or t == p:
               if A[t,l] != 0 or A[l,t] != 0:
                  incr = False
                  break
        if incr:
           t+=1
    
    return A





    




"""


def findMin(A,n,m):
    min = 5
    for i in range(n):
        for j in range(m):
            if i==0 and j==0 and A[i][j] != 0:
                min = A[i][j]
            elif math.fabs(A[i][j]) < math.fabs(min) and A[i][j] != 0:
                min = A[i][j]
 
    return min

def reduce(A,min,n,m):
    t = 0
    while True:
        B = [[0 for j in range(m)] for i in range(n)]
        C = [[0 for j in range(t,m)] for i in range(t,n)]
        for i in range(t,n):
            for j in range(t,m):
                C[i-t][j-t] = A[i][j]        
        if t > 0:
            min = findMin(C,n-t,m-t)

        for i in range(n):
            for j in range(m):
                if A[i][j] == min:
                    minRow = i
                    minCol = j
                    quit1 = True
                    break
                else:
                    quit1 = False
            if quit1:
                break
            
        for i in range(n):
            if A[i][minCol] % min != 0:
                x = A[i][minCol]
                xRow = i
                inCol = True
                inRow = False
                break
            else:
                inCol = False

        if not inCol:
            for j in range(m):
                if A[minRow][j] % min != 0:
                    x = A[minCol][j]
                    xCol = j
                    inRow = True
                    break
                else:
                    inRow = False

        if (not inRow) and (not inCol):
            for i in range(n):
                quit2 = False
                for i in range(t,m):
                    if (i != minRow) and (j != minCol):
                        if A[i][j] % min != 0:
                            x = A[i][j]
                            xRow = i
                            xCol = j
                            quit2 = True
                            break
                if quit2:
                    break

        if not(inCol or inRow or quit2):
            for i in range(n):
                B[i][minCol] = A[i][minCol]
                A[i][minCol] = A[i][t]
                A[i][t] = B[i][minCol]
            for j in range(m):
                B[minRow][j] = A[minRow][j]
                A[minRow][j] = A[t][j]
                A[t][j] = B[minRow][j]
            for i in range(n):
                q = A[i][t]/min
                if i > t:
                    for j in range(m):
                        A[i][j] = A[i][j] - q*A[t][j]
            print matrix(A)            

            if n <= m:
                if t < n-1:
                    t += 1
            else:
                if t < m-1:
                    t += 1
            for i in range(t,n):
                for j in range(t,m):
                    C[i-t][j-t] = A[i][j]        
            if t > 0:
                min = findMin(C,n-t,m-t)
            
            min = findMin        
            for i in range(t,n):
                for j in range(t,m):
                    if (i == t) and (j == t) and (A[i][j] != 0):
                        min = A[i][j]
                    elif math.fabs(A[i][j]) < math.fabs(min):
                        A[i][j] = min
            
                    
        else:
            q = x/min                    
            if inCol:
                for j in range(m):
                    A[xRow][j] = A[xRow][j] - (q*A[minRow][j])
                min = A[xRow][minCol]
            elif inRow:
                for i in range(n):
                    A[i][xCol] = A[i][xCol] - (q*A[i][minCol])
                min = A[minRow][xCol]
            else:
                for i in range(n):
                    A[i][minCol] = A[i][minCol] + A[i][minCol] - (A[minRow][xCol]/min)*A[i][xCol]
                q = A[minCol][xRow]/min           
                for i in range(n):
                    A[minRow][j] = A[minRow][j] - (q*min)
                min = A[xRow][minCol]

        diag = False
        for i in range(n):
            for j in range(m):
                if i != j:
                    if A[i][j] == 0:
                        diag = True
                    else:
                        diag = False
                        break
            if diag != True:
                break
        if diag:
            break
        print min
        
        print matrix(A)
        print

    return matrix(A)
        
                
            

def main():
    A = [[3,0],[2,0],[4,5]]
    print matrix(A)
    print
    n=3
    m=2
    min = findMin(A,n,m)
    print reduce(A,min,n,m)

main()


"""
