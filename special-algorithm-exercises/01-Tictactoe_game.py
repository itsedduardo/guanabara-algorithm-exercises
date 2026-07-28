class Tictactoe_game:
    def __init__(self):
        self.board = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"],
        ]
        self.horizontal = [
            [(0,0), (0,1), (0,2)],
            [(1,0), (1,1), (1,2)],
            [(2,0), (2,1), (2,2)]           
        ]
        self.vertical = [
            [(0,0), (1,0), (2,0)],
            [(0,1), (1,1), (2,1)],
            [(0,2), (1,2), (2,2)]          
        ]
        self.diagonal = [
            [(0,0), (1,1), (2,2)],
            [(0,2), (1,1), (2,0)]    
        ]
        #//
        self.board_state = self.board
        self.all_winning_lines = self.horizontal + self.vertical + self.diagonal
        pass
    #/
    def game_title(self):
        print("="*30),
        print(" "*9, "TicTacToe", " "*9),
        print("="*30)
        pass
    #/
    def show_menu(self, current_player):
        self.game_title()
        for row in self.board_state:
            print(*row)
        print("The current player is: ", current_player)
        pass
    #//
    def game_start(self):
        current_player = str(input("Who's going to start, X or O?: ").upper())
        
        while True:
            if not self.validate_player(current_player):
                break
            else:
                self.interface(current_player)
                winner = self.check_winner(current_player)
                if winner == True:
                    print(current_player," wins!!!")
                    break
                elif self.is_board_full():
                    print("Withdraw!!!")
                    break                    
                else:
                    current_player = self.player_switch(current_player)
        rematch = str(input("Rematch? [Y/N]: ").upper())
        if rematch == "N":
            print("\033[H\033[2J", end="") 
            return False
        else:
            print("\033[H\033[2J", end="") 
            return True
    #/
    def validate_player(self, current_player):
        if current_player not in ["X", "O"]:
            print("Invalid player. Try again.")
            return False
        else:
            return True
    #/
    def interface(self, current_player):
        self.show_menu(current_player)
        move_input = str(input("Enter with a coordinate (1-9): "))
        if not self.validate_coordinate(move_input):
            print("Invalid move. Try again")               
        else:
            self.place_move(move_input, current_player)
    #/
    def validate_coordinate(self, move_input):
        for row in self.board_state:
            if move_input in row:
                return True
        return False
    #/
    def place_move(self, move_input, current_player):
        for row in self.board_state:
            if move_input in row:
                column = row.index(move_input)
                row[column] = current_player
        pass
    #/
    def player_switch(self, current_player):
        if current_player == "X":
            current_player = "O"
        else: current_player = "X"
        return current_player
    #/
    def check_winner(self, current_player):
        for line in self.all_winning_lines:
            p1, p2, p3 = line
            if (self.board[p1[0]][p1[1]] == current_player and
                self.board[p2[0]][p2[1]] == current_player and
                self.board[p3[0]][p3[1]] == current_player):
                return True
        return False
    #/
    def is_board_full(self):
        for row in self.board_state:
            for cell in row:
                if cell not in ["X", "O"]:
                    return False
        return True
    #/
#----
if __name__ == "__main__":
    game = Tictactoe_game()
    game.game_title()
#/
while True:
    restart = game.game_start()
    if not restart:
        break
    else:
        game = Tictactoe_game()
