class TicTacToe:
    #Creates the Main board
    def __init__(self,):
        self.board = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"],
        ]
    #Creates the tittle 
    def title_ttt(self):
        print("="*30),
        print(" "*9, "TicTacToe", " "*9),
        print("="*30)
    #Show the tittle + board
    def show_ttt_and_board(self):
        self.title_ttt()
        for row in self.board:
            print(*row)

    #///

    #Get player's choice
    def get_player_coordinate(self, player_choice):             # METHOD 1: Validate user's coordinate
        self.get_found = False
        self.board_state = self.board                
        self.player_choice = player_choice
        for row in self.board_state:                      
            #print(*row)
            if self.player_choice in row:                    
                self.get_found = True
                break
        return True
    #//
    def coordinate_tester(self):                                # METHOD 2
        #print(self.get_found)
        if not self.get_found:
            return False
        else: return True
    #//
    def place_move(self, player_choice, current_player):        # METHOD 3
        for row in self.board:
            if player_choice in row:
                column = row.index(player_choice)
                row[column] = current_player
                break
    #//
    def player_switch(self, current_player):                    # METHOD 4
        if current_player == "X":
            current_player = "O"
        else: current_player = "X"
        return current_player
    #//
    #def check_winner(self, player_choice, current_player):      # METHOD 5
        #return

#///

if __name__ == "__main__":
    game = TicTacToe()
    game.show_ttt_and_board()

current_player = "X"
while True:
    print("The current player is: ",current_player)
    player_choice = str(input("Enter with a coordinate (1-9): ")) #getting the input outside
    #//
    result = game.get_player_coordinate(player_choice) #calling the method 1
    if not game.coordinate_tester():
        print("Invalid coordinate. Try again")
    else:
        game.place_move(player_choice, current_player) #calling the method 2
        game.show_ttt_and_board()
    current_player = game.player_switch(current_player)
    #//
    
#game.player_switch(current_player)
#game.check_winner(player_choice, current_player) #calling the method 4
#game.check_draw()
#game.restart()


#testers!!


#1.make one full turn work correctly
#2.make the move update the board visibly
#3.add win/draw checks
#4.add the turn loop
#5.add play-again
#Also: check the get_player_coordinate boolean


#TO KEEP IN MIND:
#1.What role is the function fulfilling?
#2.What is temporary and what is part of the game's state?
#   -If I close this method now, this information still needs to exist?
#   -Temp: "Code entered by the user"
#3.Who is authorized to modify the state?
# ///
# When creating a function or class, ask yourself: 
#   What does it know? What does it do? What can it modify? How long does this information need to exist?