import random
def sinh_vecto_so_nguyen(a,b):
    A = []
    for i in range(a,b):
      A.append(random.uniform(-10,10))
    print(A)
    return A

def sap_xep(x):
    x1 = sorted(x, reverse=True)
    print("In danh sách giảm dần", x1)
    x2 = sorted(x, reverse=False)
    print("In danh sách tăng dần", x2)

def tim_kiem(y):
    n = input("Nhập số n: ")
    for i in range(len(y)):
        if y[i] == n:
           print("Phần tử: ", y[i], "trong list")
        else:
           print("phần tử: ", y[i], "không nằm trong list")

def in_tap_tin(z):
    a= input("Nhập vào đuôi: ")
    if a =="wb":
        f=open("D:\\nnlt.txt","wb")
        f.writelines(str(z))
        f.close()
        f = open("D:\\nnlt.txt", "r")
        f.readlines()
    else:
        f=open("D:\\nnlt.txt","w")
        f.writelines(str(z))
        f.close()
        f=open("D:\\nnlt.txt","r")
        f.readlines()