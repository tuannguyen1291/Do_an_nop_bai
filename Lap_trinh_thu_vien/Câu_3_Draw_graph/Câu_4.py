import numpy as np
import matplotlib.pyplot as plt
def ham_bac_4(a, x):
    f = a*x
    return f
def dao_ham_bac_3():
    x = np.linspace(start=-10.0,stop=10.0, num=200)
    y = ham_bac_4(24, x)
    fig, ax = plt.subplots()
    ax.set_xlabel("Trục hoành - x")
    ax.set_ylabel("Trục tung - y")
    ax.set_title("Đồ thị đạo hàm bậc 2")
    ax.plot(x,y,label=r"$y=24x$")
    ax.plot(x, y)
    ax.legend()
    plt.show()
dao_ham_bac_3()

