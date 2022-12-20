from sympy import *
def giai_he_ba_phuong_trinh():
    x, y, z = symbols("x,y,z")
    eq1=Eq(2*x-5*y+z+5,0)
    eq2=Eq(4*x+2*y-2*z-2,0)
    eq3=Eq(x+y-z,0)
    answer = solve((eq1,eq2,eq3),(x,y,z))
    print("Hệ ba phương trình x,y,z")
    print("Nghiệm: ",answer)

def gioi_han():
    x=symbols("x")
    f=((x**3-3*x**2)**(1/3)+sqrt(x**2-2*x))
    answer = limit(f,x,oo)
    print("Phương trình (x**3-3*x**2)**(1/3)+sqrt(x**2-2*x)")
    print("Kết quả giới hạn: ",answer)

def dao_ham():
    x=symbols("x")
    f=(2*x-1)/(x+2)
    answer=diff(f,x)
    print("Phương trình đạo hàm")
    print(answer)

def nguyen_ham():
    x=symbols("x")
    f=x/(x**2+1)
    answer = integrate(f,(x))
    print("Nguyên hàm")
    print(answer)

def tich_phan():
    x=symbols("x")
    f=(1-x*tan(x))/(x*x*cos(x)+x)
    answer = integrate(f,(x,pi,2*pi/3))
    print("Tích phân")
    print(answer)

