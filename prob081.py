import string, time
START = time.time()

fileRead = open('matrix.txt','r')
matrix = string.split(fileRead.read(),'\n') #Reading in the matrix and splitting it into rows

matrix = [string.split(row,",") for row in matrix] #Splitting the matrix rows into individual entries
matrix = matrix[:-1] +matrix[-1][:-1] #Clean off junk at the ends

matrix = [ [int(x) for x in row ] for row in matrix] #int-ifying the matrix

for i in xrange(1,len(matrix)): #initializing the edges
    matrix[0][i] += matrix[0][i-1]
    matrix[i][0] += matrix[i-1][0]


for i in xrange(1,len(matrix)):
    for j in xrange(1, len(matrix[i])):
        matrix[i][j] += min(matrix[i-1][j],matrix[i][j-1]) #come from the cheaper direction

print matrix[-1][-1]
print "Time taken:", time.time() - START

"""
Time taken: 0.00715804100037 
Answer = 427377



"""
