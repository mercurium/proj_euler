import time
from pydash import _
START = time.time()

cachedResults = dict()

def checkIfWin(gameboard, turn):
  #check if done
  if not _.any( [isViableMove(gameboard, index) for index in xrange(len(gameboard)-1) ] ):
    return False if turn is 'player1' else True

  tupleGameboard = tuple(gameboard)
  if tupleGameboard in cachedResults:
    return cachedResults[tupleGameboard]

  if turn is 'player1':
    result = _.any(checkIfWin(board, 'player2') for board in getAllPossibleMoves(gameboard))
  elif turn is 'player2':
    result = _.all(checkIfWin(board, 'player1') for board in getAllPossibleMoves(gameboard))

  cachedResults[tupleGameboard] = result
  return result


def getAllPossibleMoves(gameboard):
  possibleMoves = filter(lambda move: isViableMove(gameboard, move), range(len(gameboard)-1))
  newBoards     = [makeMoveNoMod(gameboard,move) for move in possibleMoves]
  return newBoards

def isViableMove(gameboard, move):
  return move < len(gameboard) - 1 and gameboard[move] and gameboard[move+1]

def makeMoveNoMod(gameboard, move):
  newGameboard              = gameboard[:]
  newGameboard[move:move+2] = [0,0]
  return newGameboard

for i in xrange(1,20,2):
  print i, '\t', checkIfWin([1]*i, 'player1')
  possibleMoves = getAllPossibleMoves([1]*i)
  winningMoves  = filter(lambda move: tuple(move) in cachedResults and cachedResults[tuple(move)], possibleMoves)
  print i, winningMoves


print "Time Taken:", time.time() - START 


"""
  Only making this a variable so my syntax/style checker stops complaining
  
  So we're going to count player 1 as winning as a Win and player 2 winning as a Loss.
  
  Win = 1
  not yet computed = 0
  Loss = 2
  
  i = number of strips.
  g = array of wins/losses
  
  if i%2==0: g[i] = 1
  
  if g[i-2] == 2 or g[i-3] == 2: g[i] =1

  (ran the winning algorithm till 33)

  can't force a win : 1,5,9,15,21,25,29,35
  can't force a loss: 2,3,7,8,12,16,17,21,22,26,30,31

  can't force loss or win = player 2's choice
  can't force a win but can force loss = even
  can't force a loss but can force win = odd
  can force win or loss = player 1's choice


  looks like 35 is another one (not confirmed but it can't find a win yet)

"""
