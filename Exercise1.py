def Leibniz(n):
    approx = 0
    for i in range(n):
        approx += 8/((4*i+1)*(4*i+3))
    return approx

print(Leibniz(1000))

