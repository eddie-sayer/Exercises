 

def approxpi(N):

    approx = 0

    for n in range(N):

        approx += 8/((4*n+1)*(4*n+3))

    return approx

 

print(approxpi(1))