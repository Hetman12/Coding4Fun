# -*- coding: utf-8 -*-

import numpy as np


def MultiplyV(A,val):
    C=val*A
    print(C) 


def Multiply(A,B):
    C=A*B
    print(C)     


def Add(A,B):
    C=A+B
    print(C)    

def Rotate(A):
    m=len(A)
    n=len(A[0])
    C=np.zeros((m, n)) 
    for i in range(m):
        for j in range(n):
            #numer wiersza
            nrow=n-1-j
            #numer kolumny
            ncol=i
            C[i][j]=A[nrow][ncol]
    print(C)
            


#dane wejsciowe
A = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
B = np.array([[9, 8, 7],[6, 5, 4],[3, 2, 1]])   
val = 3

Rotate(A)

