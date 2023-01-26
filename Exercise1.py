from math import pi

def Leibniz(n):
    approx = 0
    for i in range(n):
        approx += 8/((4*i+1)*(4*i+3))
    return approx

#print(Leibniz(1000))

approx_100 = Leibniz(100)
approx_1000 = Leibniz(1000)
approx_10000 = Leibniz(10000)

error_100 = abs(pi - approx_100)
error_1000 = abs(pi - approx_1000)
error_10000 = abs(pi - approx_10000)

print(error_100, error_1000, error_10000)

error = 1
n = 10000
while error > 10**(-7):
    n += n+1
    error = abs(pi - Leibniz(n))

print(n)
