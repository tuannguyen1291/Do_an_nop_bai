from Khai_ham import sinh_vecto_so_nguyen,sap_xep,tim_kiem,in_tap_tin
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
def main():
    x=sinh_vecto_so_nguyen(a,b)
    sap_xep(x)
    tim_kiem(x)
    in_tap_tin(x)
if __name__=="__main__":
    main()
