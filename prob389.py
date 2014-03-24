import time
START = time.time()

#dieT = [0,1,1,1,1]
#
#dieC = dict()
#for i in range(1,7): dieC[(i,1)] = 1
#dieClst = [0] * (4*6+1)
#
#dieO = dict()
#for i in range(1,9): dieO[(i,1)] = 1
#dieOlst = [0] * (4*6*8+1)
#
#dieD = dict()
#for i in range(1,13): dieD[(i,1)] = 1
#dieDlst = [0] * (4*6*8*12+1)
#
#sumI = [0] * (4*6*8*12*20+1)
#
#dieDict = [dieC, dieO, dieD]
#countLst = [dieT, dieClst, dieOlst, dieDlst, sumI]
#diceLen = [6,8,12,20]
#
#for iteration in range(5):
#	for numDie in xrange(2,len(countLst[iteration])): #computing the values for the cube
#		for i in xrange(numDie,numDie * (diceLen[iteration]) + 1):
#			dieC[(i,numDie)] = 0
#			start = max(numDie-1, i-6)
#			end = min(i, numDie*6-5)
#			for j in xrange(start, end):
#				dieC[(i,numDie)] += dieC[(j,numDie-1)]
#	
#	for i in dieC.keys(): #this is the spread for the cubes
#		dieClst[i[0]] += dieT[i[1]] * dieC[i]



diceDistr = [[1,1,1,1,1], \
			[0, 1,1,1,1], \
			[0] * (4*6+1), \
			[0] * (4*6*8+1),\
			[0] * (4*6*8*12+1),  \
			[0] * (4*6*8*12*20+1)]
diceProb = [{(1,1):1}, {(1,1):1, (2,1):1, (3,1):1,(4,1):1}, dict(), dict(), dict(), dict()]
iterSize = [2,5, 4*6+1, 4*6*8+1, 4*6*8*12+1, 4*6*8*12*20+1]
dieSize = [1,4,6,8,12,20]

for i in xrange(1,6):
	for j in range(1,dieSize[i]+1):
		diceProb[i][(j,1)] = 1

for iterat in xrange(2,6):
	sizeOfDice = dieSize[iterat]
	for numDie in xrange(2, iterSize[iterat-1]):
		for i in xrange(numDie, sizeOfDice*numDie+1):
			diceProb[iterat][(i,numDie)] = 0
			
			start = max(numDie-1, i-sizeOfDice)
			end = min((numDie-1) * sizeOfDice+1, i)
			for j in xrange(start, end):
				diceProb[iterat][(i,numDie)] += diceProb[iterat][(j,numDie-1)]
			#print numDie, i, diceProb[iterat][(i,numDie)], start, end

	for i in diceProb[iterat].keys():
		diceDistr[iterat][i[0]] += diceProb[iterat][i] * diceDistr[iterat-1][i[1]]
	print iterat



print "Time Taken:", time.time() - START
