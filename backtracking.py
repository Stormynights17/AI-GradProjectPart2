# This code is from Geeks For Geeks: https://www.geeksforgeeks.org/sudoku-backtracking-7/
import sys
import time

start_time = time.time()

# N is the size of the 2D matrix N*N
N = 9

# A utility function to print grid
def printing(arr):
	for i in range(N):
		for j in range(N):
			print(arr[i][j], end = " ")
		print()

# Checks whether it will be
# legal to assign num to the
# given row, col
def isSafe(grid, row, col, num):

	# Check if we find the same num
	# in the similar row , we
	# return false
	for x in range(9):
		if grid[row][x] == num:
			return False

	# Check if we find the same num in
	# the similar column , we
	# return false
	for x in range(9):
		if grid[x][col] == num:
			return False

	# Check if we find the same num in
	# the particular 3*3 matrix,
	# we return false
	startRow = row - row % 3
	startCol = col - col % 3
	for i in range(3):
		for j in range(3):
			if grid[i + startRow][j + startCol] == num:
				return False
	return True

# Takes a partially filled-in grid and attempts
# to assign values to all unassigned locations in
# such a way to meet the requirements for
# Sudoku solution (non-duplication across rows,
# columns, and boxes) */
def solveSudoku(grid, row, col):

	# Check if we have reached the 8th
	# row and 9th column (0
	# indexed matrix) , we are
	# returning true to avoid
	# further backtracking
	if (row == N - 1 and col == N):
		return True

	# Check if column value becomes 9 ,
	# we move to next row and
	# column start from 0
	if col == N:
		row += 1
		col = 0

	# Check if the current position of
	# the grid already contains
	# value >0, we iterate for next column
	if grid[row][col] > 0:
		return solveSudoku(grid, row, col + 1)
	for num in range(1, N + 1, 1):

		# Check if it is safe to place
		# the num (1-9) in the
		# given row ,col ->we
		# move to next column
		if isSafe(grid, row, col, num):

			# Assigning the num in
			# the current (row,col)
			# position of the grid
			# and assuming our assigned
			# num in the position
			# is correct
			grid[row][col] = num

			# Checking for next possibility with next
			# column
			if solveSudoku(grid, row, col + 1):
				return True

		# Removing the assigned num ,
		# since our assumption
		# was wrong , and we go for
		# next assumption with
		# diff num value
		grid[row][col] = 0
	return False

# Driver Code

# 0 means unassigned cells
easy = 	   [[0,7,0,0,2,0,0,4,6],
			[0,6,0,0,0,0,8,9,0],
			[2,0,0,8,0,0,7,1,5],
			[0,8,4,0,9,7,0,0,0],
			[7,1,0,0,0,0,0,5,9],
			[0,0,0,1,3,0,4,8,0],
			[6,9,7,0,0,2,0,0,8],
			[0,5,8,0,0,0,0,6,0],
			[4,3,0,0,8,0,0,7,0]]

medium =   [[5,0,7,2,0,0,0,9,0],
			[0,0,6,0,3,0,7,0,1],
			[4,0,0,0,0,0,0,6,0],
			[1,0,0,4,9,0,0,0,7],
			[0,0,0,5,0,8,0,0,0],
			[8,0,0,0,2,7,0,0,5],
			[0,7,0,0,0,0,0,0,9],
			[2,0,9,0,8,0,6,0,0],
			[0,4,0,0,0,9,3,0,8]]

hard = 	   [[0,0,6,5,0,0,0,0,8],
			[0,9,5,0,0,0,0,2,0],
			[7,0,0,9,0,0,3,0,0],
			[0,0,0,0,4,0,2,7,0],
			[0,0,0,8,7,3,0,0,0],
			[0,7,9,0,5,0,0,0,0],
			[0,0,2,0,0,8,0,0,9],
			[0,5,0,0,0,0,8,1,0],
			[3,0,0,0,0,5,4,0,0]]
if str(sys.argv[1]) == "easy":
	if (solveSudoku(easy, 0, 0)):
		printing(easy,)
		end_time = time.time()
		print(str(1000*(end_time - start_time)) + " ms")
	else:
		print("no solution exists ")
elif str(sys.argv[1]) == "medium":
	if (solveSudoku(medium, 0, 0)):
		printing(medium)
		end_time = time.time()
		print(str(1000*(end_time - start_time)) + " ms")
	else:
		print("no solution exists ")
elif str(sys.argv[1]) == "hard":
	if (solveSudoku(hard, 0, 0)):
		printing(hard)
		end_time = time.time()
		print(str(1000*(end_time - start_time)) + " ms")
	else:
		print("no solution exists ")
else:
		print("you entered: " + str(sys.argv[1]))
	# This code is contributed by sudhanshgupta2019a
