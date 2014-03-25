#NOTE TODO need to solve it
import time
START = time.time()

def a(n):
    if a == 1: return  0
    binary, count = bin(n)[2:], 0
    for dig in xrange(len(binary) - 1 ):
        if binary[dig] == binary[dig+1] == '1':
            count +=1
    return count

def b(n):
    return pow(-1,a(n))

s_values = dict()
def s(n):
    if n == 0:
        return 1
    if n not in s_values:
        s_values[n] = s(n-1) + b(n)
    return s_values[n]

def fibo(n):
    fibo_num = [1,1]
    for fib in xrange(2,n+1):
        fibo_num.append(fibo_num[-1] + fibo_num[-2])
    return fibo_num

fibo_nums = fibo(45)

rudin_sharp = dict()

for i in xrange(4000):
    ans = s(i)
    rudin_sharp[ans] = [i] if ans not in rudin_sharp else rudin_sharp[ans] + [i]

for key in rudin_sharp:
    #print key, '\t', rudin_sharp[key]
    if key in fibo_nums[2:]:
        pos = fibo_nums.index(key)
        print rudin_sharp[key][fibo_nums[pos - 1]-1]

print "\nTime Taken:", time.time() - START

