from Khai_ham_numpy import nhan_vecto_ma_tran, nhan_ma_tran
x = int(input("Nhập giá trị n: "))
y = int(input("Nhập giá trị hàng: "))
z = int(input("Nhập giá trị cột: "))
m1 = int(input("Nhập giá trị hàng 1: "))
n1 = int(input("Nhập giá trị cột 1: "))
m2 = int(input("Nhập giá trị hàng 2: "))
n2 = int(input("Nhập giá trị cột 2: "))
def main():
    nhan_vecto_ma_tran(x,y,z)
    nhan_ma_tran(m1,n1,m2,n2)
    return main
if __name__=="__main__":
    main()
