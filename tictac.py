import itertools
from colorama import Fore,Back,Style
import sys


move=0
def win(game):
# horizontal_win:
	def all_same(l):
		'''if l.count(l[0])==len(l) and l[0]!=0:
									return True
								else:
									return False
								'''
		return True if l.count(l[0])==len(l) and l[0]!=0 else False

	for row in game:
		if all_same(row):
			print(f"Player {row[0]} is the Winner horizontally (---) ")
			return True

# vertical_win:
	for col in range(len(game)):
		res=[]
		for row in game:
			#print(row)
			res.append(row[col])
		#print(res)		

		if all_same(res):
			print(f"Player {res[0]} is the Winner vertically (|) ! ")
			return True		
	
# diagonal_win(game):
	
	diags=[]
	for index in range(len(game)):
		diags.append(game[index][index])

	if all_same(diags):	
		print(f"Player {diags[0]} is the Winner diagonally (\\) ! ")		
		return True
	diags=[]	
	for row,col in enumerate(reversed(range(len(game)))):
		diags.append(game[row][col])

	if all_same(diags):	
		print(f"Player {diags[0]} is the Winner diagonally (/) ! ")	
		return True	
		
	return False

def game_board(game_map,player=0,row=0,column=0,just_display=False):
	global move
	
	try:
		if game_map[row][column]!=0:
			print("Invalid Move! Try another position. ")
			return game_map,move,False
		if not just_display:
			game_map[row][column]=player
			move+=1

		#print('   0  1  2')
		print('   '+'  '.join([str(i) for i in range(len(game_map))]))
		for count,row in enumerate(game_map):
			#  print(count,row)
			colored_row=""
			for item in row:
				if item==0:
					colored_row+="   "
				if item==1:
					colored_row+=Fore.MAGENTA+' X '+Style.RESET_ALL
				if item==2:
					colored_row+=Fore.RED+' O '+Style.RESET_ALL

			print(count,colored_row)				


				#sys.exit(0)
		return game_map,move,True
	
	except IndexError as e:
		print("Error :Please enter either 0,1 or 2",e)
		return game_map,move,False
	except Exception as e:
		print("Oops ,Something went wrong!!",e)	
		return game_map,move,False





play=True
while play:
	'''	game = [[0,0,0],
			[0,0,0],
			[0,0,0],]'''
	game_size=int(input('what size of Tictactoe ,you wanna play ?'))
	game=[[0 for i in range(game_size)]  for i in range(game_size)]
	#print(game)
	game_won=False

	game,moves,_ = game_board(game,just_display=True)
	player_choice=itertools.cycle([1,2])
	while not game_won:
		current_player=next(player_choice)
		print(f"Current Player:{current_player}")
		played=False
		
		while not played:
			row_choice=int(input("what row do you want to play? (0, 1, 2): "))
			column_choice=int(input("what column do you want to play? (0, 1, 2): "))
			game,moves,played=game_board(game,current_player,row_choice,column_choice)
			if win(game):
				game_won=True
				move=0
				again=input("GAME OVER , wanna play again ? (y/n) ")
				if again.lower() == "y":
					print("\nRestarting please wait..")
					
				elif again.lower() == "n":
					print("\n Exiting... ")
					play = False
				else:
					print("\n Invalid choice ")	
					play = False

			if moves==(game_size)**2:
				game_won=True
				again=input("\n MATCH DRAW \n  wanna play again ? (y/n) ")
				if again.lower() == "y":
					print("\nRestarting please wait..")
					move=0
				elif again.lower() == "n":
					print("\n Exiting... ")
					play = False
	

					



