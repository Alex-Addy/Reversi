black = 'B'
white = 'W'
b_size = 8

# currently the code references the coordinate system as
#    y ------->
#  x D D D D D
#  | D D D D D
#  | D D D D D
#  \/

# the names are useless, don't listen to them

def main():
	board = [[' ' for x in range(b_size)] for y in range(b_size)]

	# setup the board
	board[b_size/2-1][b_size/2-1] = black
	board[b_size/2][b_size/2] = black
	board[b_size/2-1][b_size/2] = white
	board[b_size/2][b_size/2-1] = white

	white_player = "Player1"
	black_player = "Player2"
	is1turn = True
	
	print "Enter moves of the form letter, number."
	print "For example to move to A3 you would type 'A3' then press enter."
	print "It is case insensitive."
	
	while True:
		poss = possibleMoves(board)
		if (not poss{black}) and (not poss{white}):
			pass
		
		else

def possibleMoves(board):

	moves = {black:[], white:[]}
	
	open = False
	for x in range(b_size):
		if 0 in board[x]:
			open = True
			break

	if not open:
		return moves

	for x in range(b_size):
		for y in range(b_size):
			if board[x][y] == 0:
				if isvalid(x, y, board, black):
					moves{black}.append((x,y))
				elif isvalid(x, y, board, white):
					moves{white}.append((x,y))
	return True
		
def printBoard(board):
	print '      {0}   {1}   {2}   {3}   {4}   {5}   {6}   {7}  '.format(*[chr(x+ord('A')) for x in range(0, b_size)])
	print '    ---------------------------------'
	for x in range(b_size):
		print x, ' ',
		print '| {0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} |'.format(*board[x])
		print '    ---------------------------------'

def playerMove(name, board, color):
	# the column is the letter and the row is the number
	while(True):
		move = raw_input("{0} move: ".format(name))
		move = move.toUpperCase()
		if(ord('A') + b_size >= ord(move[0]) >= ord('A')):
			if(0 <= move[1] <= b_size):
				directions = validDirs(move[1], ord(move[0]) - ord('A'), board, color)
				if(len(directions) > 0):
					return directions
				else:
					print "Invalid location."
			else:
				print "Invalid number."
		else:
			print "Invalid letter."

def validDirs(base_x, base_y, board, color):
	# returns a tuple of the valid directions
	directions = []

	if board[base_x][base_y]: return directions

	# do a check out from the x, y coordinates using dx and dy values for each direction
	# check left (-x y)
	if checkOneWay(base_x, base_y, board, color, -1, 0): directions.append((-1, 0))
	# check left-up (-x -y)
	if checkOneWay(base_x, base_y, board, color, -1, -1): directions.append((-1, -1))
	# check up (x -y)
	if checkOneWay(base_x, base_y, board, color, 0, -1): directions.append((0, -1))
	# check right-up (+x -y)
	if checkOneWay(base_x, base_y, board, color, 1, -1): directions.append((1, -1))
	# check right (+x y)
	if checkOneWay(base_x, base_y, board, color, 1, 0): directions.append((1, 0))
	# check right-down (+x +y)
	if checkOneWay(base_x, base_y, board, color, 1, 1): directions.append((1, 1))
	# check down (x +y)
	if checkOneWay(base_x, base_y, board, color, 0, 1): directions.append((0, 1))
	# check left-down (-x +y)
	if checkOneWay(base_x, base_y, board, color, -1, 1): directions.append((-1, 1))

	return directions

def checkOneWay(base_x, base_y, board, color, delta_x = 0, delta_y = 0):
	if delta_x == delta_y == 0:
		raise ValueError("delta_x and delta_y cannot both be zero.")

	if board[base_x + delta_x][base_y + delta_y] == color: return False
	if board[base_x + delta_x][base_y + delta_y] == 0: return False

	temp_x = base_x + delta_x
	temp_y = base_y + delta_y

	other = (black if black == color else white)
	foundother = False
	while 0 <= temp_x < b_size and 0 <= temp_y < b_size:
		if board[temp_x][temp_y] == 0: return False
		elif board[temp_x][temp_y] == other: foundother = True
		elif board[temp_x][temp_y] == color: return foundother
		temp_x += delta_x
		temp_y += delta_y
	return False

