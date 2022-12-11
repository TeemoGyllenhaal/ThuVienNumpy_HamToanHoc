import numpy as np
#BT1
def sinh_ngau_nhien_so_nguyen(a,b,n):
    v1 = np.random.randint(low = a, high= b, size=n )
    return v1
#BT2
def luong_giac(x):
    a = np.sin(x)
    print ("cos (x) = ",a)
    b = np.cos(x)
    print ("sin (x) = ",b)
    c = np.sqrt(x)
    print ("sqrt (x) = ",c)
    d = np.log(x)
    print ("log (x) = ",d)
    return a,b,c,d
#Không chọn a, b số âm
x = sinh_ngau_nhien_so_nguyen(1,10,4)
luong_giac(x)
#BT3
def lam_tron(x,y):
    a = np.sin(x)
    a = np.round(a,y)
    b = np.cos(x)
    b = np.round(b,y)
    c = np.sqrt(x)
    c = np.round(c,y)
    d = np.log(x)
    d = np.round(d,y)
    print ("cos (x) = ",a)
    print ("sin (x) = ",b)        
    print ("sqrt (x) = ",c)
    print ("log (x) = ",d)
    return a,b,c,d
lam_tron(x,2)
def ma_tran(m,n):
    z = np.random.rand(m, n)
    print (z)
    return z
z = ma_tran(2,3)
lam_tron(z,3)