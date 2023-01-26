def Leibniz(n):
    approx = 0
    for i in range(n):
        approx += 8/((4*n + 1)(4*n + 3))
    end
return approx


