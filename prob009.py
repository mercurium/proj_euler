
pythagMax = [-1] * 3001
for m in range(1,3000):
    if 2*m**2 > 3000:
        break
    for n in range(1,m):
        if 2*m**2 + 2*m*n > 3000:
            break
        for k in range(1,1000):
            if 2*m*k*(n+m) > 3000:
                break
            a = k* (m**2 - n**2)
            b = 2*m*n * k
            c = m**2*k + n**2 *k
            pythagMax[a+b+c] = max(pythagMax[a+b+c], a*b*c)

numTestCases = int(raw_input())
for i in range(numTestCases):
    N = int(raw_input())
    print pythagMax[N]
