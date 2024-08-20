# Code was built or modified to work best on a UNIX vi editor.
# Jason Xia and Muhtasim Chowdhury

import sys
import pygame
import random
import os
import time

wid = 1000
hig = 500
 
def winning(grid): # A function to check if the current board meets the conditions for winning
	for i in range(len(grid)): # Checking all 3 rows
		info = []
		for j in range(len(grid[i])):
			info.append(grid[i][j])
		if info[0] == info[1] and info[0] == info[2] and info[0] != "": # Checks if all values on the current row being checked are the same and not blank; if they meet the win conditions
			if info[0] == "X": # Checks if the winning combination is made of Xs or Os, and returns a value accordingly
				return "X" 
			if info[0] == "O":
				return "O"
		else:
			x=1 # do nothing
	for i in range(len(grid[0])): # Checking all 3 Columns
		info = []
		for j in range(len(grid)):
			info.append(grid[j][i])
		if info[0] == info[1] and info[0] == info[2] and info[0] != "":
			if info[0] == "X":
				return "X"
			if info[0] == "O":
				return "O"
		else:
			x=1
	if grid[0][0] == grid[1][1] and grid[0][0] == grid[2][2] and grid[0][0] != "": # Checking the Diagonal, top left to bottom right
		if grid[0][0] == "X":
			return "X"
		if grid[0][0] == "O":
			return "O"
	if grid[0][2] == grid[1][1] and grid[0][2] == grid[2][0] and grid[0][2] != "": # Checking the Diagonal, top right to bottom left
		if grid[0][2] == "X":
			return "X"
		if grid[0][2] == "O":
			return "O"
	else:
		x=1

def almostwin(grid): # A Function made for the vs. CPU mode. Checks to see if either side is about to win (2/3 cells occupied, remaining cell is blank), and returns a tuple containing data about who is about to win and what row/column/diagonal they are about to win in.
	cond1 = False # All boolean variables here become true if the computer detects that X is about to win.
	cond2 = False 
	cond3 = False
	cond4 = False
	for i in range(len(grid)): # Checking rows
		info = []
		for j in range(len(grid[i])):
			info.append(grid[i][j])
		if info[0] == info[1] and info[2] == "" and info[0] != ""  or info[0] == info[2] and info[1] == "" and info[0] != "": # Checks to see if the 2/3 possible scenarios of almost winning are true, being 2/3 cells being occupied by 1 player, and the remaining cell being blank.
			if info[0] == "O":
				return "O", i, "row"
			if info[0] == "X":
				num1 = i # The same information as O is not returned here because it needs to be checked first if O is about to win. The boolean variable here triggers a series of if operators that return the same information in the event O is not about to win.
				cond1 = True
		if info[1] == info[2] and info[0] == "" and info[1] != "":
			if info[i] == "O":
				return "O", i, "row"
			if info[1] == "X":
				num1 = i
				cond1 = True
		else:
			x=1
	for i in range(len(grid[0])): # Checking columns
		info = []
		for j in range(len(grid)):
			info.append(grid[j][i])
		if info[0] == info[1] and info[2] == "" and info[0] != ""  or info[0] == info[2] and info[1] == "" and info[0] != "":
			if info[0] == "O":
				return "O", i, "column"
			if info[0] == "X":
				num2 = i
				cond2 = True
		if info[1] == info[2] and info[0] == "" and info[1] != "":
			if info[0] == "O":
				return "O", i, "column"
			if info[1] == "X":
				num2 = i
				cond2 = True
		else:
			x=1
	
	if grid[0][0] == grid[1][1] and grid[2][2] == "" and grid[0][0] != "" or grid[0][0] == grid[2][2] and grid[1][1] == "" and grid[0][0] != "": # Checking Diagonals
		if grid[0][0] == "O":
			return "O", 0, "Diagonal"
		if grid[0][0] == "X":
			cond3 = True
	if grid[1][1] == grid[2][2] and grid[0][0] == "" and grid[1][1] != "":
		if grid[1][1] == "O":
			return "O", 0, "Diagonal"
		if grid[1][1] == "X":
			cond3 = True
	if grid[0][2] == grid[1][1] and grid[2][0] == "" and grid[0][2] != "" or grid[0][2] == grid[2][0] and grid[1][1] == "" and grid[0][2] != "":
		if grid[0][2] == "O":
			return "O", 1, "Diagonal"
		if grid[0][2] == "X":
			cond4 = True
	if grid[1][1] == grid[2][0] and grid[0][2] == "" and grid[1][1] != "":
		if grid[1][1] == "O":
			return "O", 1, "Diagonal"
		if grid[1][1] == "X":
			cond4 = True
	
	if cond1 == True: # Checks to see if X is about to win, given that O is not about to win and no moves can be made for the computer winning.
		return "X", num1, "row"
	elif cond2 == True:
		return "X", num2, "column"
	elif cond3 == True:
		return "X", 0, "Diagonal"
	elif cond4 == True:				
		return "X", 1, "Diagonal"
	

scrn = pygame.display.set_mode((wid,hig))
bgc = (207, 207, 207)
pygame.font.init()

# 2D array to store the board info
tictactoeinfo = [["","",""]\
		,["","",""]\
		,["","",""]]

scrn.fill(bgc)
pygame.display.set_caption("Tic tac toe")
clock = pygame.time.Clock()

regfontpath = os.path.join("Fonts", "DIN Condensed Bold.ttf") # a series of os.path.join to let python know where to get the proper files in the correct folders
titlefontpath = os.path.join ("Fonts", "PressStart2P-Regular.ttf")
sbpath = os.path.join("Assets", "Startbutton.png")
blankpath = os.path.join("Assets", "Blanksquare.png")
Opath = os.path.join("Assets", "Osquare.png")
Xpath = os.path.join("Assets", "Xsquare.png")

startbutton = pygame.image.load(sbpath).convert() # Loads an image as a surface object
sb_area = startbutton.get_rect() # Loads the co-ordinates of a rectangle with the same dimensions of the above image, used for interaction with rectangle objects and getting values such as image height and length, something you normally can't do on a surface object, but can on a rectangle object.
Titlefont = pygame.font.Font(titlefontpath, 50) #Initializes a bunch of fonts
SubTitlefont = pygame.font.Font(titlefontpath, 35)
Regfont = pygame.font.Font(regfontpath,35)

# Pre-game text section
Title = Titlefont.render("Tic Tac Toe",False,(0,0,0)) # Renders text based on the initialized fonts
Titlearea = Title.get_rect() 
Whovs = SubTitlefont.render("Play against:", False, (0,0,0))
WVS_area = Whovs.get_rect()
CPU = Titlefont.render("COMPUTER", False, (0,0,0))
PLAYER = Titlefont.render("PLAYER", False, (0,0,0))
cpu_area = CPU.get_rect()
player_area = PLAYER.get_rect()

# Game text section
Whoseturn1 = SubTitlefont.render("It is YOUR turn",False,(40, 0, 199))
WT1_area = Whoseturn1.get_rect()
WT1_area2 = Whoseturn1.get_rect()
Whoseturn2 = SubTitlefont.render("It is THEIR turn",False,(191,17,17))
WT2_area = Whoseturn2.get_rect()
YouWin = SubTitlefont.render("You Win!",False,(0,0,0))
CompWin = SubTitlefont.render("They Win!",False,(0,0,0))
YW_area = YouWin.get_rect()
CW_area = CompWin.get_rect()
Tie = SubTitlefont.render("Tie!", False,(0,0,0))
Tie_area = Tie.get_rect()

# Game info text section
YouareX = Regfont.render("You are:",False, (40, 0, 199))
YRX_area = YouareX.get_rect()
X = Titlefont.render("X", False, (40, 0, 199))
X_area = X.get_rect()
TheyareO = Regfont.render("They are:",False, (191,17,17))
TRO_area = TheyareO.get_rect()
O = Titlefont.render("O", False, (191,17,17))
O_area = O.get_rect()

pygame.Rect.move_ip(WT1_area2,((wid-WT1_area.x)/4,10))

# Loading 9 instances of a Blank Square surface object (image)
blanksquare1 = pygame.image.load(blankpath).convert()
blanksquare2 = pygame.image.load(blankpath).convert()
blanksquare3 = pygame.image.load(blankpath).convert()
blanksquare4 = pygame.image.load(blankpath).convert()
blanksquare5 = pygame.image.load(blankpath).convert()
blanksquare6 = pygame.image.load(blankpath).convert()
blanksquare7 = pygame.image.load(blankpath).convert()
blanksquare8 = pygame.image.load(blankpath).convert()
blanksquare9 = pygame.image.load(blankpath).convert()

# Creates the dimensions for a full 3x3 blank square grid
bs_area = blanksquare1.get_rect()
bs_area.w *=3
bs_area.h *=3

# Obtains Rect info from all 9 instances of blank square surface object
bs_area1 = blanksquare1.get_rect()
bs_area2 = blanksquare1.get_rect()
bs_area3 = blanksquare1.get_rect()
bs_area4 = blanksquare1.get_rect()
bs_area5 = blanksquare1.get_rect()
bs_area6 = blanksquare1.get_rect()
bs_area7 = blanksquare1.get_rect()
bs_area8 = blanksquare1.get_rect()
bs_area9 = blanksquare1.get_rect()

# moving the Rect values (coordinates) to their desired location, being enter of screen.
pygame.Rect.move_ip(bs_area,((wid - bs_area.right)/2),((hig - bs_area.bottom)/2))
pygame.Rect.move_ip(sb_area,((wid - sb_area.right)/2),((hig - sb_area.bottom)/2))
pygame.draw.rect(scrn,(0,0,0),sb_area)

# More Rect value moving to desired locations
pygame.Rect.move_ip(bs_area1, bs_area.x, bs_area.y)
pygame.Rect.move_ip(bs_area2, (bs_area.w/3)+((wid - bs_area.w)/2), bs_area.y)
pygame.Rect.move_ip(bs_area3, (bs_area.w/3*2)+((wid - bs_area.w)/2), bs_area.y)
pygame.Rect.move_ip(bs_area4, bs_area.x, (bs_area.h/3) + (hig - bs_area.h)/2)
pygame.Rect.move_ip(bs_area5, (bs_area.w/3)+((wid - bs_area.w)/2), (bs_area.h/3) + (hig - bs_area.h)/2)
pygame.Rect.move_ip(bs_area6, (bs_area.w/3*2)+((wid - bs_area.w)/2), (bs_area.h/3) + (hig - bs_area.h)/2)
pygame.Rect.move_ip(bs_area7, bs_area.x, (bs_area.h/3*2) + (hig - bs_area.h)/2)
pygame.Rect.move_ip(bs_area8, (bs_area.w/3)+((wid - bs_area.w)/2), (bs_area.h/3*2) + (hig - bs_area.h)/2)
pygame.Rect.move_ip(bs_area9, (bs_area.w/3*2)+((wid - bs_area.w)/2), (bs_area.h/3*2) + (hig - bs_area.h)/2)

pygame.Rect.move_ip(cpu_area, (wid-cpu_area.w)/2, 166)
pygame.Rect.move_ip(player_area, (wid-player_area.w)/2, 332)

# A series of boolean values to indicate what squares have been clicked and by whom
# If a player has clicked a square
bs1p = False
bs2p = False
bs3p = False
bs4p = False
bs5p = False
bs6p = False
bs7p = False
bs8p = False
bs9p = False 

# If a computer has selected a square
# each number lines up with an instance of a blank square
cc1 = False
cc2 = False
cc3 = False
cc4 = False
cc5 = False
cc6 = False
cc7 = False
cc8 = False
cc9 = False

# Initializing a bunch of variables to be used in the game
delay = 0
yourturn = 0
yourturn2 = True
vsplayer = False
vscpu = False
clicked = False
sbclicked = False
running = True
while running:
	for event in pygame.event.get(): # seeks out a pygame event every frame
		if event.type == pygame.QUIT:
			running = False


		if sbclicked == False: # If the user has not yet clicked the start button
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					if sb_area.collidepoint(event.pos): # Checks to see if the user has clicked a start button
						sbclicked = True
						print("click")
			scrn.blit(Title,((wid-Titlearea.right)/2,30)) # Blits the Title to the screen
			scrn.blit(startbutton,(((wid - sb_area.right)),((hig - sb_area.bottom)-1)))  # Blits the image of a start button to the screen
		else: # If the user has clicked the start button
			scrn.fill(bgc)
			if event.type == pygame.MOUSEBUTTONDOWN: # Checks to see if the user has clicked either option
				if event.button == 1:
					if cpu_area.collidepoint(event.pos):
						vscpu = True
					if player_area.collidepoint(event.pos):
						vsplayer = True
			scrn.blit(Whovs, ((wid - WVS_area.right)/2,10))
			scrn.blit(CPU, ((wid-cpu_area.w)/2, 166))
			scrn.blit(PLAYER, ((wid-player_area.w)/2, 332))

		if sbclicked == True and vscpu == True or sbclicked == True and vsplayer == True: # Checks to see if the user has clicked on an option on who to play against on the option screen
			scrn.fill(bgc)
			pygame.draw.rect(scrn,(50,50,50),bs_area)
			pygame.draw.rect(scrn, (0,0,0), bs_area1)			
			pygame.draw.rect(scrn, (0,0,0), bs_area2)			
			pygame.draw.rect(scrn, (0,0,0), bs_area3)			
			pygame.draw.rect(scrn, (0,0,0), bs_area4)			
			pygame.draw.rect(scrn, (0,0,0), bs_area5)			
			pygame.draw.rect(scrn, (0,0,0), bs_area6)			
			pygame.draw.rect(scrn, (0,0,0), bs_area7)			
			pygame.draw.rect(scrn, (0,0,0), bs_area8)			
			pygame.draw.rect(scrn, (0,0,0), bs_area9)			
        
            # Blits all instances of Blank squares to form a grid
			scrn.blit(blanksquare1, (bs_area.x, bs_area.y))	
			scrn.blit(blanksquare2, ((bs_area.w/3)+((wid - bs_area.w)/2),bs_area.y))
			scrn.blit(blanksquare3, ((bs_area.w/3*2)+((wid - bs_area.w)/2),bs_area.y))


			scrn.blit(blanksquare4, (bs_area.x, (bs_area.h/3) + (hig - bs_area.h)/2 ))	
			scrn.blit(blanksquare5, ((bs_area.w/3)+((wid - bs_area.w)/2), (bs_area.h/3) + (hig - bs_area.h)/2 ))
			scrn.blit(blanksquare6, ((bs_area.w/3*2)+((wid - bs_area.w)/2), (bs_area.h/3) + (hig - bs_area.h)/2))


			scrn.blit(blanksquare7, (bs_area.x, (bs_area.h/3*2) + (hig - bs_area.h)/2 ))	
			scrn.blit(blanksquare8, ((bs_area.w/3)+((wid - bs_area.w)/2), (bs_area.h/3*2) + (hig - bs_area.h)/2 ))
			scrn.blit(blanksquare9, ((bs_area.w/3*2)+((wid - bs_area.w)/2), (bs_area.h/3*2) + (hig - bs_area.h)/2))
		

			scrn.blit(YouareX, ((wid-YRX_area.right)/6-13, (hig-YRX_area.bottom)/2-50))
			scrn.blit(X,((wid-X_area.right)/6, (hig-X_area.bottom)/2))
			scrn.blit(TheyareO, ((wid-TRO_area.right)/6*5+13, (hig-TRO_area.bottom)/2-50))
			scrn.blit(O,((wid-O_area.right)/6*5, (hig-O_area.bottom)/2))
			
			delay +=1 # A counter that goes up each frame to delay certain if conditions without using time.sleep			
			a=winning(tictactoeinfo) # Calling the winning check function to check if anyone has won before the start of a new turn
			if a == "X":
				scrn.blit(YouWin, ((1000-YW_area.right)/2,10))
				yourturn = 1000 # Yourturn must be under 9 for the game to proceed under a "playing" state
			elif a == "O":
				scrn.blit(CompWin, ((1000-CW_area.right)/2,10))
				yourturn = 1000

			if yourturn % 2 == 0 and yourturn < 9 and delay > 5: # 15 frames are updated per second, delay needs to be higher than 5, meaning a delay of 1/3 of a second. This is to prevent the mouse from clicking a vs player or vs computer option and then immediately clicking on a blank cell in the same click.
				print(yourturn)
				if event.type == pygame.MOUSEBUTTONDOWN: # Checks to see if the user has clicked
					if event.button == 1:
						if bs_area1.collidepoint(event.pos) and tictactoeinfo[0][0] == "": # Checks to see if the User has clicked within the boundaries of a Rect value, and to see if the space is blank based on the info in the 2D array
							bs1p = True
							clicked = True
							print("sq1")
						if bs_area2.collidepoint(event.pos) and tictactoeinfo[0][1] == "":
							bs2p = True
							clicked = True
							print("sq2")
						if bs_area3.collidepoint(event.pos) and tictactoeinfo[0][2] == "":
							bs3p = True
							clicked = True
							print("sq3")
						if bs_area4.collidepoint(event.pos) and tictactoeinfo[1][0] == "":
							bs4p = True
							clicked = True
							print("sq4")
						if bs_area5.collidepoint(event.pos) and tictactoeinfo[1][1] == "":
							bs5p = True
							clicked = True
							print("sq5")
						if bs_area6.collidepoint(event.pos) and tictactoeinfo[1][2] == "":
							bs6p = True
							clicked = True
							print("sq6")
						if bs_area7.collidepoint(event.pos) and tictactoeinfo[2][0] == "":
							bs7p = True
							clicked = True
							print("sq7")
						if bs_area8.collidepoint(event.pos) and tictactoeinfo[2][1] == "":
							bs8p = True
							clicked = True
							print("sq8")
						if bs_area9.collidepoint(event.pos) and tictactoeinfo[2][2] == "":
							bs9p = True
							clicked = True
							print("sq9")
				scrn.blit(Whoseturn1,((1000-WT1_area.right)/2,10)) # Blits a message saying it is the user's turn

			elif yourturn % 2 == 1 and yourturn < 9: # Other player's turn
				print(yourturn)
				if vscpu == True: # If the user has selected to face off against a computer
					print(yourturn)
					time.sleep(2) # "Processing"
					Valid = False # A check to see if the randomly selected square is valid or not
					abouttowin = almostwin(tictactoeinfo)
								
					while Valid == False:
						computerchoice = random.randint(1,9) # Randomly selects a square
						if abouttowin != None: # Checks to see if either side is winning, if they are, discard the randomly selected value and replace it with one that either has the computer win the game or deny the user a win
							print(abouttowin[0], "Is about to win!")
							if abouttowin[2] == "row": # Searches through the row stated in the location value returned by the almostwin function for a blank space
								for item in tictactoeinfo[abouttowin[1]]:
									if item == "":
										computerchoice = tictactoeinfo[abouttowin[1]].index(item) + 1 + (3*abouttowin[1])
							elif abouttowin[2] == "column": # Searches through column for a blank space
								row = -1
								for item in tictactoeinfo:
									row +=1
									if item[abouttowin[1]] == "":
										computerchoice = abouttowin[1] + 1 + (3*row)
										print("info is", abouttowin[1])
							elif abouttowin[2] == "Diagonal": # Searches through diagonal for a blank space
								if abouttowin[1] == 0:
									if tictactoeinfo[0][0] == "":
										computerchoice = 1
									elif tictactoeinfo[1][1] == "":
										computerchoice = 5
									elif tictactoeinfo[2][2] == "":
										computerchoice = 9
								if abouttowin[1] == 1:
									print(tictactoeinfo[0][2])
									if tictactoeinfo[0][2] == "":
										computerchoice = 3
										print("TEST")
									elif tictactoeinfo[1][1] == "":
										computerchoice = 5
									elif tictactoeinfo[2][0] == "":
										computerchoice = 7
						print("choice is",computerchoice)					
						if computerchoice == 1 and tictactoeinfo[0][0] == "": # Checks to see what either the randomly selected or forcefully picked computer choice is
							cc1 = True
							Valid = True
						elif computerchoice == 2 and tictactoeinfo[0][1] == "":
							cc2 = True
							Valid = True
						elif computerchoice == 3 and tictactoeinfo[0][2] == "":
							cc3 = True
							Valid = True
						elif computerchoice == 4 and tictactoeinfo[1][0] == "":
							cc4 = True
							Valid = True
						elif computerchoice == 5 and tictactoeinfo[1][1] == "":
							cc5 = True
							Valid = True
						elif computerchoice == 6 and tictactoeinfo[1][2] == "":
							cc6 = True
							Valid = True
						elif computerchoice == 7 and tictactoeinfo[2][0] == "":
							cc7 = True
							Valid = True
						elif computerchoice == 8 and tictactoeinfo[2][1] == "":
							cc8 = True
							Valid = True
						elif computerchoice == 9 and tictactoeinfo[2][2] == "":
							cc9 = True
							Valid = True
					yourturn+=1
					print(yourturn)
				
				if vsplayer == True: # essentially a repeat of the regular user code.
								
					if event.type == pygame.MOUSEBUTTONDOWN:
						if event.button == 1:
							if bs_area1.collidepoint(event.pos) and tictactoeinfo[0][0] == "":
								cc1 = True
								clicked = True
								print("sq1")
							if bs_area2.collidepoint(event.pos) and tictactoeinfo[0][1] == "":
								cc2 = True
								clicked = True
								print("sq2")
							if bs_area3.collidepoint(event.pos) and tictactoeinfo[0][2] == "":
								cc3 = True
								clicked = True
								print("sq3")
							if bs_area4.collidepoint(event.pos) and tictactoeinfo[1][0] == "":
								cc4 = True
								clicked = True
								print("sq4")
							if bs_area5.collidepoint(event.pos) and tictactoeinfo[1][1] == "":
								cc5 = True
								clicked = True
								print("sq5")
							if bs_area6.collidepoint(event.pos) and tictactoeinfo[1][2] == "":
								cc6 = True
								clicked = True
								print("sq6")
							if bs_area7.collidepoint(event.pos) and tictactoeinfo[2][0] == "":
								cc7 = True
								clicked = True
								print("sq7")
							if bs_area8.collidepoint(event.pos) and tictactoeinfo[2][1] == "":
								cc8 = True
								clicked = True
								print("sq8")
							if bs_area9.collidepoint(event.pos) and tictactoeinfo[2][2] == "":
								cc9 = True
								clicked = True
								print("sq9")
					scrn.blit(Whoseturn2,((1000-WT2_area.right)/2,10))
			else: # When the board is full:
				a=winning(tictactoeinfo) # Check if anyone has one
				if a == "X":
					scrn.blit(YouWin, ((1000-YW_area.right)/2,10))
				elif a == "O":
					scrn.blit(CompWin, ((1000-CW_area.right)/2,10))
				elif delay > 5: # If no one has won, it results in a tie.
					scrn.blit(Tie, ((1000-Tie_area.right)/2,10))
					
			if cc1 == True: # replaces the blank square surface corresponding to the variable with a surface of a square with an O
                    # these If conditions are here because pygame updates everything every frame, meaning if the squares were made to appear in the if event.type == pygame.MOUSEBUTTONDOWN condition, they would disappear as soon as the event MOUSEBUTTONDOWN was not active
					Os = pygame.image.load(Opath).convert()
					scrn.blit(Os, (bs_area.x, bs_area.y))
					tictactoeinfo[0].pop(0)
					tictactoeinfo[0].insert(0,"O") # Updates board info
			if cc2 == True:
					Os = pygame.image.load(Opath).convert()
					scrn.blit(Os, ((bs_area.w/3)+((wid - bs_area.w)/2), bs_area.y))
					tictactoeinfo[0].pop(1)
					tictactoeinfo[0].insert(1,"O")
			if cc3 == True:
					Os = pygame.image.load(Opath).convert()
					scrn.blit(Os, ((bs_area.w/3*2)+((wid - bs_area.w)/2), bs_area.y))
					tictactoeinfo[0].pop(2)
					tictactoeinfo[0].insert(2,"O")
			if cc4 == True:
					Os = pygame.image.load(Opath).convert()
					scrn.blit(Os, (bs_area.x, (bs_area.h/3) + (hig - bs_area.h)/2))
					tictactoeinfo[1].pop(0)
					tictactoeinfo[1].insert(0,"O")
			if cc5 == True:
					Os = pygame.image.load(Opath).convert()
					scrn.blit(Os, ((bs_area.w/3)+((wid - bs_area.w)/2), (bs_area.h/3) + (hig - bs_area.h)/2))
					tictactoeinfo[1].pop(1)
					tictactoeinfo[1].insert(1,"O")
			if cc6 == True:
					Os = pygame.image.load(Opath).convert()
					scrn.blit(Os, ((bs_area.w/3*2)+((wid - bs_area.w)/2), (bs_area.h/3) + (hig - bs_area.h)/2))
					tictactoeinfo[1].pop(2)
					tictactoeinfo[1].insert(2,"O")
			if cc7 == True:
					Os = pygame.image.load(Opath).convert()
					scrn.blit(Os, (bs_area.x, (bs_area.h/3*2) + (hig - bs_area.h)/2))
					tictactoeinfo[2].pop(0)
					tictactoeinfo[2].insert(0,"O")
			if cc8 == True:
					Os = pygame.image.load(Opath).convert()
					scrn.blit(Os, ((bs_area.w/3)+((wid - bs_area.w)/2), (bs_area.h/3*2) + (hig - bs_area.h)/2))
					tictactoeinfo[2].pop(1)
					tictactoeinfo[2].insert(1,"O")
			if cc9 == True:
					Os = pygame.image.load(Opath).convert()
					scrn.blit(Os, ((bs_area.w/3*2)+((wid - bs_area.w)/2), (bs_area.h/3*2) + (hig - bs_area.h)/2))
					tictactoeinfo[2].pop(2)
					tictactoeinfo[2].insert(2,"O")
			 
			if bs1p == True: # Same but for X
					Xs = pygame.image.load(Xpath).convert()
					scrn.blit(Xs, (bs_area.x, bs_area.y))
					tictactoeinfo[0].pop(0)
					tictactoeinfo[0].insert(0,"X")
			if bs2p == True:
					Xs = pygame.image.load(Xpath).convert()
					scrn.blit(Xs, ((bs_area.w/3)+((wid - bs_area.w)/2), bs_area.y))
					tictactoeinfo[0].pop(1)
					tictactoeinfo[0].insert(1,"X")
			if bs3p == True:
					Xs = pygame.image.load(Xpath).convert()
					scrn.blit(Xs, ((bs_area.w/3*2)+((wid - bs_area.w)/2), bs_area.y))
					tictactoeinfo[0].pop(2)
					tictactoeinfo[0].insert(2,"X")
			if bs4p == True:
					Xs = pygame.image.load(Xpath).convert()
					scrn.blit(Xs, (bs_area.x, (bs_area.h/3) + (hig - bs_area.h)/2))
					tictactoeinfo[1].pop(0)
					tictactoeinfo[1].insert(0,"X")
			if bs5p == True:
					Xs = pygame.image.load(Xpath).convert()
					scrn.blit(Xs, ((bs_area.w/3)+((wid - bs_area.w)/2), (bs_area.h/3) + (hig - bs_area.h)/2))
					tictactoeinfo[1].pop(1)
					tictactoeinfo[1].insert(1,"X")
			if bs6p == True:
					Xs = pygame.image.load(Xpath).convert()
					scrn.blit(Xs, ((bs_area.w/3*2)+((wid - bs_area.w)/2), (bs_area.h/3) + (hig - bs_area.h)/2))
					tictactoeinfo[1].pop(2)
					tictactoeinfo[1].insert(2,"X")
			if bs7p == True:
					Xs = pygame.image.load(Xpath).convert()
					scrn.blit(Xs, (bs_area.x, (bs_area.h/3*2) + (hig - bs_area.h)/2))
					tictactoeinfo[2].pop(0)
					tictactoeinfo[2].insert(0,"X")
			if bs8p == True:
					Xs = pygame.image.load(Xpath).convert()
					scrn.blit(Xs, ((bs_area.w/3)+((wid - bs_area.w)/2), (bs_area.h/3*2) + (hig - bs_area.h)/2))
					tictactoeinfo[2].pop(1)
					tictactoeinfo[2].insert(1,"X")
			if bs9p == True:
					Xs = pygame.image.load(Xpath).convert()
					scrn.blit(Xs, ((bs_area.w/3*2)+((wid - bs_area.w)/2), (bs_area.h/3*2) + (hig - bs_area.h)/2))
					tictactoeinfo[2].pop(2)
					tictactoeinfo[2].insert(2,"X")

			a = winning(tictactoeinfo)

			if yourturn % 2 == 0 and clicked == True and a == None and vscpu == True: # Updates turn value and blits text on whose turn it is if facing off a computer
				yourturn += 1
				clicked = False
				pygame.draw.rect(scrn, bgc, WT1_area2)
				scrn.blit(Whoseturn2,((1000-WT2_area.right)/2,10))
			
			if yourturn % 2 == 1 and clicked == True and a == None and vsplayer == True: # Updates turn value if facing off against a player
				yourturn += 1
				clicked = False

			if yourturn % 2 == 0 and clicked == True and a == None and vsplayer == True:
				yourturn += 1
				clicked = False
		pygame.display.flip()
		clock.tick(15) #Pygame updates the screen 15 times per second

pygame.quit()
sys.exit()
