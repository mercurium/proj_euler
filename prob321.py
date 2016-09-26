import time
START   = time.time()
LIM     = 10**6
LIM_TRI = LIM * (LIM+1)/2
NUM     = 40

answers = [1]
diffs   = [2]

secondDiffs = [5,5,29,29]

while len(secondDiffs) < NUM:
  secondDiffs.append(secondDiffs[-2] * 6 - secondDiffs[-4])

for secondDiff in secondDiffs:
  diffs.append(diffs[-1] + secondDiff)

for diff in diffs:
  answers.append(answers[-1] + diff)

print sum(answers[:40])
print "Time taken:", time.time() - START


"""
Congratulations, the answer you gave to problem 321 is correct.

You are the 1122nd person to have solved this problem.

Answer     : 2470433131948040
Time taken : 0.000121831893921

Started this problem with 244's maze solving code to get a general formula for # of steps. Got:
  1 3
  2 8
  3 15
  4 24
  5 35
  6 48
  7 63
  8 80

This is pretty obviously G(n) = n * (n+2)

Plugging this in and getting the first few results, you get
[1, 3, 10, 22, 63, 133, 372, 780, 2173, 4551, 12670, 26530, 73851, 154633, 430440]

Taking the diffs between continous results, you get:
[2, 7, 12, 41, 70, 239, 408, 1393, 2378, 8119, 13860, 47321, 80782, 275807]

And with the second diff, you get:
[5, 5, 29, 29, 169, 169, 985, 985, 5741, 5741, 33461, 33461, 195025]

which is conveniently http://oeis.org/A001653, or a(n) = 6 * a(n-1) - a(n-2)

Now that we know the first and second diff, we can compute the actual answer quite easily.

And we win :)



G(n) = n * (n+2)

Super relevant lol:
http://oeis.org/A001653

Second diff = http://oeis.org/A001653

a(n) = 6 * a(n-1) - a(n-2)


"""
