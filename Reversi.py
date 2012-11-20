
black = 'B'
white = 'W'

def main():
	board = [0 for x in range(8) for y in range(8)]
	
	# setup the board
	board[3][3] = black
	board[4][4] = black
	board[3][4] = white
	board[4][3] = white
	
	while(not gameOver()):
		
	
def printBoard(board):
	for x in range(8):
		print '---------------------------------'
		print '| {0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} |'.format(*board[x])
	print '---------------------------------'
	
def gameOver(board):
	open = False
	for x in range(0):
		if 0 in board[x]:
			open = True
	if not open:
		return True
		
	for x in range(8):
		for y in range(8):
			if board[x][y] == 0:
				if isvalid(x, y, board, black):
					return False
				elif isvalid(x, y, board, white):
					return False
	return True
	
def playerMove(name, board):
	pass
	
def isValid(x, y, board, color):
	pass
	