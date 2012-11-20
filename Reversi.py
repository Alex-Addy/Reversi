
black = 'B'
white = 'W'
b_size = 8

def main():
	board = [0 for x in range(b_size) for y in range(b_size)]
	
	# setup the board
	board[b_size/2-1][b_size/2-1] = black
	board[b_size/2][b_size/2] = black
	board[b_size/2-1][b_size/2] = white
	board[b_size/2][b_size/2-1] = white
	
	while(not gameOver()):
		pass
	
def printBoard(board):
	for x in range(b_size):
		print '---------------------------------'
		print '| {0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} |'.format(*board[x])
	print '---------------------------------'
	
def gameOver(board):
	open = False
	for x in range(b_size):
		if 0 in board[x]:
			open = True
	if not open:
		return True
		
	for x in range(b_size):
		for y in range(b_size):
			if board[x][y] == 0:
				if isvalid(x, y, board, black):
					return False
				elif isvalid(x, y, board, white):
					return False
	return True
	
def playerMove(name, board):
	pass
	
def validDirs(base_x, base_y, board, color):
	# returns a tuple of the valid directions
	directions = []
	
	if board[base_x][base_y]: return directions
	
	# do a check out from the x, y coordinates using dx and dy values for each direction
	# check left        (-x y)
	if checkOneWay(base_x, base_y, board, color, -1, 0): directions.append((-1, 0))
	# check left-up     (-x -y)
	if checkOneWay(base_x, base_y, board, color, -1, -1): directions.append((-1, -1))
	# check up          (x -y)
	if checkOneWay(base_x, base_y, board, color, 0, -1): directions.append((0, -1))
	# check right-up    (+x -y)
	if checkOneWay(base_x, base_y, board, color, 1, -1): directions.append((1, -1))
	# check right       (+x y)
	if checkOneWay(base_x, base_y, board, color, 1, 0): directions.append((1, 0))
	# check right-down  (+x +y)
	if checkOneWay(base_x, base_y, board, color, 1, 1): directions.append((1, 1))
	# check down        (x +y)
	if checkOneWay(base_x, base_y, board, color, 0, 1): directions.append((0, 1))
	# check left-down   (-x +y)
	if checkOneWay(base_x, base_y, board, color, -1, 1): directions.append((-1, 1))
	
	return directions

def checkOneWay(base_x, base_y, board, color, delta_x = 0, delta_y = 0):
	if delta_x == delta_y == 0:
		raise ValueError("delta_x and delta_y cannot both be zero.")

	if board[base_x + delta_x][base_y + delta_y] == color: return False
	if board[base_x + delta_x][base_y + delta_y] == 0: return False
	
	temp_x = base_x + delta_x
	temp_y = base_y + delta_y
	
	other = (black == color ? black : white)
	foundother = False
	while 0 <= temp_x < b_size and 0 <= temp_y < b_size:
		if board[temp_x][temp_y] == 0: return False
		elif board[temp_x][temp_y] == other: foundother = True
		elif board[temp_x][temp_y] == color: return foundother
		temp_x += delta_x
		temp_y += delta_y
	return False
	