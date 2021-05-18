# battleships_validation.py

def validate_battlefield(field):
	'''A function that takes a 10x10 list of lists corresponding to a 
	battleship board as an argument and returns True if the field is
	a legal arrangement of ships or False if not.  Ships are standard
	(1 carrier size 4, 2 battleships size 3, 3 destroyers size 2, 4 subs
	size 1) and ships may be touching each other.  Only the location of 
	hits are known, not the identity of each hit.  
	'''
	ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
	import pprint

	# make a wrapper for the field for ease of iteration
	for i in field:
		i.insert(0, 0)
		i.append(0)
	field.insert(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
	field.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

	# preliminary check for the correct number of spaces
	count = 0
	for lst in field:
		for element in lst:
			if element == 1:
				count += 1
	if count != 20:
		return False

	return validate(field, ships)
	
def validate(field, ships):
	'''Assesses the validity of a given field (field), with a 
	list of ships that are yet to be accounted for (ships).  The
	method is to remove ships, largest to smallest, using recursion.
	Returns a boolean corresponding to the possibility of the field
	being legal or not.
	'''
	for i in range(12):
		for j in range(12):
			if field[i][j] == 1:

				k = 0
				while field[i+k][j] == 1:
					k += 1

					if k == ships[0]:
						del ships[0]

						for m in range(k):
							field[i+m][j] = 0
						
						if len(ships) == 0: 
							y = 1
							return True

						ships2 = ships[:]
						if validate(field, ships2):
							return True
						
						else:
							for x in range(k):
								field[i+x][j] = 1
							ships = [k] + ships
						
				w = 0
				while field[i][j+w] == 1:
					w += 1

					if w == ships[0]:
						del ships[0]

						for n in range(w):
							field[i][j+n] = 0
			
						if len(ships)==0:
							y = 1
							return True

						ships3 = ships[:]

						if validate(field, ships3):
							return True

						else:
							for n in range(w):
								field[i][j+n] = 1
							ships = [w] + ships
						
	if len(ships)==0:
		return True
	else:
		return False


# example input
field = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		 [1, 1, 1, 0, 0, 0, 0, 0, 1, 0],
		 [1, 1, 0, 0, 0, 0, 0, 0, 1, 0],
		 [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
		 [1, 1, 0, 0, 0, 0, 0, 0, 1, 0],
		 [1, 1, 0, 0, 1, 1, 1, 0, 0, 0],
		 [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# example function call
print (validate_battlefield(field))