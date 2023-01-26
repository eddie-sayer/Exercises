def Leibniz(n):
    approx = 0
    for i in range(n):
        approx += 8/((4*i+1)*(4*i+3))
    return approx

#print(Leibniz(1000))

approx_100 = Leibniz(100)
approx_1000 = Leibniz(1000)
approx_10000 = Leibniz(10000)