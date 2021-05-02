# install Pygame [2.0.1+] with  : python3 -m pip install pygame
# then, install Pygame Zero with: python3 -m pip install pgzero --no-deps
# docs: https://pygame-zero.readthedocs.io/

import pgzrun, math, time, copy

WIDTH = 400      # window dimensions
HEIGHT = 400
running = False  # whether the simulation is running


class Life:
	def __init__(self, cells_per_dimension = 50):
		self.board = []
		for x in range(cells_per_dimension):              # for each row
			self.board.append([0] * cells_per_dimension)  # add an empty column of cells
		self.w = WIDTH / cells_per_dimension              # size of a cell in px
		self.generation = 0                               # current generation
		self.last_time = 0                                # when the current generation was generated

	def generate(self):
		"""Calculate a new generation of cells from the current ones."""
		# nextboard = self.board.copy()
		nextboard = copy.deepcopy(self.board)

		# Implement the logic game of life here ;)

		for x in range(0, len(self.board)):
			
			for y in range(0, len(self.board[0])):
        
				neighbors = 0
	
				for i in range(-1, 2):
        
					for j in range(-1, 2):
         
						if x + 1 > len(self.board[0]) - 1:	# x wrap around
							x = 0
						if y + 1 > len(self.board[1]) - 1:	# y wrap around
							y = 0
          
						neighbors += self.board[x + i][y + j]
				
				neighbors -= self.board[x][y]

				# * Any live cell with two or three live neighbours survives.
			
				if self.board[x][y] == 1 and neighbors < 2:		# if set to 3 or 4, cells will die out, but if set to 2, cells will stay
					nextboard[x][y] = 0
		
				# * Any dead cell with three live neighbours becomes a live cell.
				
				elif self.board[x][y] == 0 and neighbors == 3:	# if set to 4, cells will die out and constant glider-like figures will remain; at 2, screen will fill fast
					nextboard[x][y] = 1
					
				# * Any live cell with more than 3 neighbors dies from overpopulation

				elif self.board[x][y] == 1 and neighbors > 3:	# at 2, cells will die out, at 4 cells will rarely die
					nextboard[x][y] = 0

    			# * All other live cells die in the next generation. Similarly, all other dead cells stay dead.
       
				else:
					nextboard[x][y] = self.board[x][y]
			

		# self.board ... holds the state of the current generation (only read from it)
		# nextboard  ... holds the state of the next generation (write to it)

		self.board = nextboard
		self.generation += 1
		self.last_time = time.time()

	def draw(self):
		"""Draw the current generation to the screen."""
		for x in range(len(self.board)):
			for y in range(len(self.board[x])):
				cell = Rect((x*self.w, y*self.w), (self.w, self.w))
				if self.board[x][y] == 0:
					screen.draw.filled_rect(cell, (255, 255, 255))
				else:
					screen.draw.filled_rect(cell, (0, 0, 0))

	def toggle_cell(self, x, y):
		"""Change a dead cell to a living one and vice versa."""
		if self.board[x][y] == 0:
			self.board[x][y] = 1
		else:
			self.board[x][y] = 0


life = Life()
# help(Life)

def draw():
	"""Called whenever the screen needs to be repainted."""
	screen.fill((255, 255, 255))
	life.draw()

def update():
	"""Called 60 times a second."""
	if running:                         # if we're running
		now = time.time()               # get the current time
		if now - life.last_time > 0.1:  # and the last generation is older than 100ms (10fps)
			life.generate()             # calculate a new generation

def on_mouse_down(pos, button):
	"""Called whenever the mouse button is clicked."""
	# print(button)
	life.toggle_cell(math.floor(pos[0]/life.w), math.floor(pos[1]/life.w))

def on_key_down(key):
	"""Called whenever a key on the keyboard is pressed."""
	global running
	if key == keys.SPACE:
		life.generate()                 # Space: single step
	elif key == key.RETURN:
		running = not running           # Return: start/stop continuous generations


pgzrun.go()
