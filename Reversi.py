black = '\u25cf'
white = '\u25cb'
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
	board[int(b_size/2)-1][int(b_size/2)-1] = black
	board[int(b_size/2)][int(b_size/2)] = black
	board[int(b_size/2)-1][int(b_size/2)] = white
	board[int(b_size/2)][int(b_size/2)-1] = white

	blackturn = True
	
	print("Enter moves of the form letter, number.")
	print("For example to move to A3 you would type 'A3' then press enter.")
	print("It is case insensitive.")
	
	while True:
		poss = possibleMoves(board)
		printBoard(board)
		print(poss)
		if poss[black] == [] and poss[white] == []:
			break
		else:
			if blackturn:
				if poss[black]:
					the_move = playerMove(poss, black)
					changeBoard(the_move, board, black)
					blackturn = False
				else:
					the_move = playerMove(poss, white)
					changeBoard(the_move, board, white)
			else:
				if poss[white]:
					the_move = playerMove(poss, white)
					changeBoard(the_move, board, white)
					blackturn = True
				else:
					the_move = playerMove(poss, black)
					changeBoard(the_move, board, black)
				

	print("Gameover. {0} is the winner.".format(winner(board)))

def possibleMoves(board):

	moves = {black:[], white:[]}
	
	isopen = False
	for x in range(b_size):
		if ' ' in board[x]:
			isopen = True
			break
	#print("Open is ", isopen)
	if not isopen:
		return moves

	for x in range(b_size):
		for y in range(b_size):
			if board[x][y] == ' ':
				#print(x, ' ', y)
				if validDirs(x, y, board, black):
					moves[black].append((x,y))
				elif validDirs(x, y, board, white):
					moves[white].append((x,y))
	return moves
		
def printBoard(board):
	print('      A   B   C   D   E   F   G  H ')
	print('    -------------------------------')
	for x in range(b_size):
		print(x, end=" ")
		print(' | {0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} |'.format(*board[x]))
		print('    -------------------------------')

def playerMove(poss, color):
	# the column is the letter and the row is the number
	while(True):
		prompt = "{}'s move: ".format(color)
		move = input(prompt)
		move = move.upper()
		col = ord(move[0])-ord('A')
		row = int(move[1])
		if(b_size >= col >= 0):
			if(0 <= row <= b_size):
				if (row, col) in poss[color]:
					return (row, col)
				else:
					print("Invalid location.")
			else:
				print("Invalid number.")
		else:
			print("Invalid letter.")

def validDirs(base_x, base_y, board, color):
	# returns a tuple of the valid directions
	directions = []

	if board[base_x][base_y] != " ": return directions

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
	#if delta_x == 0 and delta_y == 0:
	#	return False

	#print("\t", color,"dx", delta_x,"dy", delta_y)

	temp_x = base_x + delta_x
	temp_y = base_y + delta_y

	if 0 > temp_x or temp_x >= b_size or 0 > temp_y or temp_y >= b_size: return False

	if board[temp_x][temp_y] == ' ': return False

	other = (black if white == color else white)
	foundother = False
	#print("\tMade it to loop:", other)
	while 0 <= temp_x < b_size and 0 <= temp_y < b_size:
		#print("\t\tWhere:", temp_x, temp_y, " is: ", board[temp_x][temp_y])
		if board[temp_x][temp_y] == color: return foundother
		elif board[temp_x][temp_y] == other: foundother = True
		elif board[temp_x][temp_y] == ' ': return False
		temp_x += delta_x
		temp_y += delta_y
	return False

def winner(board):
	b, w = 0, 0
	for x in range(b_size):
		for y in range(b_size):
			if(board[x][y] == white): w += 1
			elif(board[x][y] == black): b += 1

	return black if b > w else white

def changeBoard(move, board, color):
	#print("Move selected: ", move[0], move[1])
	board[move[0]][move[1]] = color
	#print("board[{}][{}]:{}".format(move[0], move[1], board[move[0]][move[1]]))
	for dx in [-1, 0, 1]:
		for dy in [-1, 0, 1]:
			if dy == 0 and dx == 0: continue
			#print("\t Loop:", dx, dy)
			if checkOneWay(move[0], move[1], board, color, dx, dy):
				#print("\t\tNow changing.")
				changeOneDir(move[0], move[1], board, color, dx, dy)

def changeOneDir(base_x, base_y, board, color, delta_x = 0, delta_y = 0):

	temp_x = base_x + delta_x
	temp_y = base_y + delta_y

	other = (black if white == color else white)

	while 0 <= temp_x < b_size and 0 <= temp_y < b_size:
		if board[temp_x][temp_y] == ' ': return
		elif board[temp_x][temp_y] == other: board[temp_x][temp_y] = color
		elif board[temp_x][temp_y] == color: return

		temp_x += delta_x
		temp_y += delta_y
	return

if __name__ == '__main__':
	main()