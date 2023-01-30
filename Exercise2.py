#Part a

def dot(a,b):
    size_a = len(a)
    size_b = len(b)
    if size_a == size_b:
        dot_ans = 0
        for i in range(size_a):
            dot_ans += a[i]*b[i]
        print("The dot product between the two vectors is " + str(dot_ans))
    else:
        print("The two vectors must be the same size.")
    

Q2_a_a = [1,2,3,7,6,5,9]
Q2_a_b = [6,5,4,3,4,9,7]

dot(Q2_a_a,Q2_a_b)

#Part b

x1 = [[1,2],[3,4]]
x2 = [[5,6],[7,8]]



