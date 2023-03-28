import random
# Game of Life in Python
class GameOfLife:

    def __init__(self, board):
        self.board = board
        self.n = len(board)
        
    def neighbourSum(self, i, j):
        neighbours = [self.board[(i-1+self.n)%self.n][(j-1+self.n)%self.n],
                      self.board[(i-1+self.n)%self.n][j],
                      self.board[(i-1+self.n)%self.n][(j+1)%self.n],
                      self.board[i%self.n][(j+1)%self.n],
                      self.board[(i+1)%self.n][(j+1)%self.n],
                      self.board[(i+1)%self.n][j],
                      self.board[(i+1)%self.n][(j-1+self.n)%self.n],
                      self.board[i][(j-1+self.n)%self.n]]
        return sum(neighbours)
    
    def nextPattern(self):
        if self.board is None or self.n == 0:
           raise ValueError("Board not initialized or has size 0")
        
        new_board = [[0 for j in range(self.n)] for i in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                live_neighbours = self.neighbourSum(i, j)
                if self.board[i][j] == 1:
                    if live_neighbours < 2:
                        new_board[i][j] = 0
                    elif live_neighbours == 2 or live_neighbours == 3:
                        new_board[i][j] = 1
                    elif live_neighbours > 3:
                        new_board[i][j] = 0
                else:
                    if live_neighbours == 3:
                        new_board[i][j] = 1
        
        self.board = new_board
        
    def printBoard(self):
        for i in range(self.n):
            for j in range(self.n):
                if  self.board[i][j] == 0:
                    print(" ", end=" ")
                else:
                    print("*", end=" ")
            print()
        print()
        

def generate_board(n):
    board = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(random.randint(0,1))
        board.append(row)
    return board



def main():
    # Create two initial patterns for the game
    n=2
    pattern1 = generate_board(n)
    pattern2 = generate_board(n)
    pattern3 = generate_board(n)
    
  
    # Ask the user to choose one of the patterns
    print("Choose one of the following patterns to start the game:")
    
    #pattern1
    obj1 = GameOfLife(pattern1);
    print("Pattern 1:")
    obj1.printBoard()
    
    #pattern2
    obj2 = GameOfLife(pattern2);
    print("Pattern 2:")
    obj2.printBoard()
    
    #pattern3
    obj3= GameOfLife(pattern3);
    print("Pattern 3:")
    obj3.printBoard()
    
    choice = int(input("Enter the number of the pattern you want to play with (1 or 2 or 3): "))
    if choice == 1:
        obj1 = GameOfLife(pattern1);
    elif choice == 2:
        obj1 = GameOfLife(pattern2);
    elif choice == 3:
        obj1 = GameOfLife(pattern3);
    else :
        print("Wrong Input! Input should be between 1-3")

    # Start the game
  
    print("The game starts now!")
   
    while True:
        # Print the current pattern
        obj1.printBoard()
          
        # Ask the user if they want to see the next pattern
        next_step = input("Do you want to see the next pattern? (y/Y). To end the game enter any other symbol ")
        if next_step.lower() != "y":
            break
        # Calculate and update the next pattern
        obj1.nextPattern()

if __name__ == "__main__":
    main()  




