import numpy as np
import matplotlib.pyplot as plt

def runge_kutta_4(f, t0, x0, v0, Tmax, h):
    t = np.arange(t0, Tmax + 2 * h, h)
    x = np.zeros_like(t)
    v = np.zeros_like(t)
    x[0] = x0
    v[0] = v0
    for i in range(len(t) - 1):
        ti = t[i]
        xi = x[i]
        vi = v[i]
        k1_x = h * vi
        k1_v = h * f(xi)
        k2_x = h * (vi + 0.5 * k1_v)
        k2_v = h * f(xi + 0.5 * k1_x)
        k3_x = h * (vi + 0.5 * k2_v)
        k3_v = h * f(xi + 0.5 * k2_x)
        k4_x = h * (vi + k3_v)
        k4_v = h * f(xi + k3_x)
        x[i + 1] = xi + (k1_x + 2 * k2_x + 2 * k3_x + k4_x) / 6
        v[i + 1] = vi + (k1_v + 2 * k2_v + 2 * k3_v + k4_v) / 6
        print(i, ')', 't =', ti, ', x =', xi)
    return t, x


m = 1.0
k = 5.0
Tmax = 10.0
v0 = 3.0
x0 = 0.0
t0 = 0.0
h = 0.01
t, x = runge_kutta_4(lambda x: (-k * x) / m, t0, x0, v0, Tmax, h)
plt.plot(t, x)
plt.xlabel('t')
plt.ylabel('x')
plt.title('Частное решение дифференциального уравнения')
plt.grid(True)
plt.show()
