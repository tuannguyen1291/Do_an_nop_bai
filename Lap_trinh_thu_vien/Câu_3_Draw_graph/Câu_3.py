import numpy as np
import matplotlib.pyplot as plt
def ham_bac_4(a, b, x):
    f = a*x**2 + b
    return f
def dao_ham_bac_2():
    x = np.linspace(start=-10.0,stop=10.0, num=200)
    y = ham_bac_4(12, -4, x)
    fig, ax = plt.subplots()
    ax.set_xlabel("Trục hoành - x")
    ax.set_ylabel("Trục tung - y")
    ax.set_title("Đồ thị đạo hàm bậc 2")
    ax.plot(x,y,label=r"$y=12x^{2}-4$")
    ax.plot(x, y)
    ax.legend()
    plt.show()
dao_ham_bac_2()

