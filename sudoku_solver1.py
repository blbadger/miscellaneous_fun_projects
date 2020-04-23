def solve(puzzle):
	'''A function that takes a list of lists denoting sudoku
	puzzle clues and places to guess (0s) and returns the completed
	puzzle as a list of lists. Expects a solveable puzzle, and will 
	return only solution if multiple exist.
	'''

	# make list of all positions to be determined
	ls = []
	for x in range(9):
		for y in range(9):
			if puzzle[x][y] == 0:
				ls.append([x,y])

	# backtracking algorithm with validation tests
	def backtrack(puzzle, ls):
		'''Solves the sudoku puzzle by iterating through the 
		positions in ls and entering possible values into 
		the puzzle array.  Backtracking occurs when no entry
		is possible for a given space.
		'''
		i = 0
		while i in range(len(ls)):
			a, b = ls[i]
			count = 0

			if puzzle[a][b] == 0: 
				c = 0

			else: 
				c = puzzle[a][b]

			c += 1
			while c < 10:
				if c not in puzzle[a]:
					ls2 = []
					for q in range(9):
						ls2.append(puzzle[q][b])
		
					if c not in ls2:
						ls3 = []
						x, y = a // 3, b // 3
						for k in range(3*x, 3*x+3):
							for l in range(3*y, 3*y+3):
								ls3.append(puzzle[k][l])

						if c not in ls3:
							puzzle[a][b] = c
							count += 1
							i += 1
							break

						else: c += 1
					else: c += 1
				else: c += 1

			if count == 0:
				puzzle[a][b] = 0
				i -= 1
		return puzzle
	
	return backtrack(puzzle, ls)

# example of an input
puzzle = [
 [9, 0, 0, 0, 8, 0, 0, 0, 1],
 [0, 0, 0, 4, 0, 6, 0, 0, 0],
 [0, 0, 5, 0, 7, 0, 3, 0, 0],
 [0, 6, 0, 0, 0, 0, 0, 4, 0],
 [4, 0, 1, 0, 6, 0, 5, 0, 8],
 [0, 9, 0, 0, 0, 0, 0, 2, 0],
 [0, 0, 7, 0, 3, 0, 2, 0, 0],
 [0, 0, 0, 7, 0, 5, 0, 0, 0],
 [1, 0, 0, 0, 4, 0, 0, 0, 7]]

# example function call
import pprint
pprint.pprint (solve(puzzle))

