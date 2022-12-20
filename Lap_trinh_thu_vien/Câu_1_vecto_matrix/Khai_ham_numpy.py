import numpy as np
import random
def nhan_vecto_ma_tran(a,b,c):
    x=[random.randint(1,10) for i in range(a)]
    print("Vecto R^n: ",x)
    A=np.random.randint(1,10,(b,c))
    print("Ma trận mxn: ",A)
    B=x*A
    print("Ma trận vecto R^n nhân ma trận mxn: ",B)
    return a,b,c

def nhan_ma_tran(a,b,c,d):
    A=np.random.randint(1,10,(a,b))
    print("Ma trận A: ", A)
    B=np.random.randint(1,10,(c,d))
    print("Ma trận B: ", B)
    print("Ma trận AxB: ",A.dot(B))
    print("Ma trận chuyển vị: ",np.transpose(A))
    print("Ma trận nhân A^T nhân B: ",np.transpose(A)*B)
    return a,b,c,d

