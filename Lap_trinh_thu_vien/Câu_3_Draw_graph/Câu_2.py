import numpy as np
import matplotlib.pyplot as plt
def ham_bac_4(a, b, x):
    f = a*x**3 - b*x
    return f
def ve_dao_ham():
    x = np.linspace(start=-10.0,stop=10.0, num=200)
    y = ham_bac_4(4, -4, x)
    fig, ax = plt.subplots()
    ax.set_xlabel("Trục hoành - x")
    ax.set_ylabel("Trục tung - y")
    ax.set_title("Đồ thị đạo hàm bậc 1")
    ax.plot(x,y,label=r"$y=4x^{3}-4x$")
    ax.plot(x, y)
    ax.legend()
    plt.show()
ve_dao_ham()
