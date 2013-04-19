

g = [1,2,1,1,1,2,1,1,1,2,1,1,1] + [0]*10**6

for i in range(2,len(g),2):
  g[i] = 1



"""
So we're going to count player 1 as winning as a Win and player 2 winning as a Loss.

Win = 1
not yet computed = 0
Loss = 2

i = number of strips.
g = array of wins/losses

if i%2==0: g[i] = 1

if g[i-2] == 2 or g[i-3] == 2: g[i] =1

1L
2W
3W
4W
5L
6W
7W
8W
9L
10W
11W
12W


"""
