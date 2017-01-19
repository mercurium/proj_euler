import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

totient      = (num1 - 1) * (num2 - 1)
coresilience = num1 * num2 - totient

print "the remainder of n-1 when mod C(num1 * num2) is:", (num1 * num2 - 1) % coresilience
