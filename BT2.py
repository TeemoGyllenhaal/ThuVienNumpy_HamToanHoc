import numpy as np
import random
random.seed(123)
def sinh_ngau_nhien_so_thuc(a,b,n):
    v1 = [(b-a)*random.random()+ a for i in range (n)]
    v1 = sorted(v1)
    print(v1)
    return v1
x= sinh_ngau_nhien_so_thuc(-100,100,1000)
x1 = sorted (x)
x1= np.array(x)
def giai_phuong_trinh(x):
    y = 3*x**2 - 2*x - 4
    a = np.cos(y*np.pi/180)
    b = np.sin(y*np.pi/180)
    print ("cos(f(x))=", a)
    print ("sin(f(x))=", b)
    return a,b,y
giai_phuong_trinh(x1)