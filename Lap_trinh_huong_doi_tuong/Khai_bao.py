import os
import pickle
class NhanVien():
    def __init__(self, hoten, tuoi, luong):
        self.hoten = hoten
        self.tuoi = tuoi
        self.luong = luong
    def __str__(self):
        message = "[họ và tên:" + self.hoten + ";tuổi:" + str(self.tuoi) + ";lương:" + str(self.luong) + "$]"
        return message
    def __gt__(self, obj):
        return (self.tuoi > obj.tuoi)
    def __ge__(self, obj):
        return (self.tuoi >= obj.tuoi)
    def __lt__(self, obj):
        return (self.tuoi < obj.tuoi)
    def __le__(self, obj):
        return (self.tuoi <= obj.tuoi)
    def __eq__(self, obj):
        return (self.tuoi == obj.tuoi)
def nhap_nhan_vien():
    n = abs(int(input("Nhập số lượng thành viên: ")))
    nv = []
    for i in range(n):
        nv.append(NhanVien(input("Nhập tên: "), input("Nhập tuổi: "), input("Nhập lương: ")))
    return nv
def hien_thi_nhan_vien(nhanvien):
    print("---------------------")
    print("BT1: Hien thi toan bo nhan vien")
    for items in nhanvien:
        print("Ho va ten: " + items.hoten)
        print("Tuoi: " + items.tuoi)
        print("Luong: " + items.luong)
        print("---------------------")
def hien_thi_nhan_vien_theo_tuoi(nhanvien):
    nhan_vien_theo_tuoi = sorted(nhanvien)
    hien_thi_nhan_vien(nhan_vien_theo_tuoi)
def doc_tap_tin(thumuc: str, tentaptin: str) -> NhanVien:
    try:
        with open(os.path.join(thumuc, tentaptin), "rb") as f:
            nv = pickle.load(f)
        return nv
    except Exception as e:
        print("Xảy ra lổi")
def ghi_tap_tin(thumuc: str, tentaptin: str, objs: list[NhanVien]):
    try:
        with open(os.path.join(thumuc, tentaptin), "wb") as f:
            pickle.dump(objs, f)
        print("Kết thúc chương trình")
    except:
        print("Xãy ra lỗi")



