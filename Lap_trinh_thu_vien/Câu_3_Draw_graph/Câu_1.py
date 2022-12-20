import numpy as np
import matplotlib.pyplot as plt
def ham_bac_4(a, b, c, x):
    f = a*x**4 + b*x**2 + c
    return f
def ve_ham_so():
    x = np.linspace(start=-10.0,stop=10.0, num=200)
    y = ham_bac_4(1, -2, -3, x)
    fig, ax = plt.subplots()
    ax.set_xlabel("Trục hoành - x")
    ax.set_ylabel("Trục tung - y")
    ax.set_title("Đồ thị y")
    ax.plot(x,y,label=r"$y=x^{4}-2x^{2}-3$")
    ax.plot(x, y)
    ax.legend()
    plt.show()
ve_ham_so()
