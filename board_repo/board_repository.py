from random import choice
'''
A ship will be marked on the map with 0
A component of the ship will be marked
on the map with 1 if it has been hit
A miss hit will be marked on the map
with 2
'''
from texttable import  Texttable

class Board:

    def __init__(self):
        '''
        THE GAME BOARD WILL BE AN 8X8
        MATRIX,INITIALIZED WITH ' '
        '''
        self._board = []
        for i in range(8):
            lst = []
            for j in range(8):
                lst.append(' ')
            self._board.append(lst)

    def str(self):
        '''
        Internal function that shows the
        map with ships discovered...
        '''
        board  = Texttable()
        header = [' ','A','B','C','D','E','F','G','H']
        board.header(header)

        for i in range(8):
            lst = []
            lst.append(i+1)
            for j in range(8):
                if self._board[i][j] == 0:
                    lst.append('[]')
                elif self._board[i][j] == 1:
                    lst.append('H')
                elif self._board[i][j] == 2:
                    lst.append('M')
                else:
                    lst.append(' ')
            board.add_row(lst)

        return board.draw()


    def __str__(self):
        '''
        How the user will see the board during
        the game play
        '''

        board  = Texttable()
        header = [' ','A','B','C','D','E','F','G','H']
        board.header(header)

        for i in range(8):
            lst = []
            lst.append(i+1)
            for j in range(8):
                if self._board[i][j] == 0:
                    lst.append(' ')
                elif self._board[i][j] == ' ':
                    lst.append(' ')
                elif self._board[i][j] == 1:
                    lst.append('H')
                elif self._board[i][j] == 2:
                    lst.append('M')
            board.add_row(lst)

        return board.draw()

    def battleship_shape(self,x,y,position):
        '''
        battleship (4 squares)
        The position describes the way the
        battle ship will be placed on the
        board...Position: vertical or
        horizontal...
        Input: x,y the head of the battle ship
               position - vert or hor
        Output: the shape of the battleship
        starting from the point described by
        x and y
        '''
        if position.lower() == 'vertical':
            shape = [[x,y],[x+1,y],[x+2,y],[x+3,y]]
            return shape
        if position.lower() == 'horizontal':
            shape = [[x,y],[x,y+1],[x,y+2],[x,y+3]]
            return shape

    def cruiser_shape(self,x,y,position):
        '''
         1 cruiser (3 squares)
         Same functionality as battleship_shape,but
         only for 3 squares
        '''
        shape = self.battleship_shape(x,y,position)
        shape = shape[:-1]
        return shape

    def destroyer_shape(self,x,y,position):
        '''
        1 destroyer (2 squares)
        Same as battleship_shape
        '''
        shape = self.battleship_shape(x,y,position)
        shape = shape[:-2]
        return shape

    def isNumber(self,x):
        '''
        Checks if x can be a number
        '''
        try:
            x = int(x)
            return 1
        except ValueError:
            return 0

    def fromLetterToNumber(self,x):
        '''
        Returns the index of x from a list,
        in case x is not in the list, fct.
        returns -1
        '''
        lst =  ['A','B','C','D','E','F','G','H']

        if x.upper() not in 'ABCDEFGH':
            return -1

        for index in range(8):
            if lst[index] == x.upper():
                return index

    def isFree(self,x,y):
        '''
        Returns 1 if the cell (x,y) is free
        and 0 otherwise
        '''
        if self._board[x][y] == ' ':
            return 1
        return 0

    def isInBoard(self,x,y):
        '''
        Return 1 if (x,y) describes a point
        from the board and 0 otherwise
        '''
        if x < 0:
            return 0
        if y < 0:
            return 0
        if x > 7:
            return 0
        if y > 7:
            return 0
        return 1

    def validate_placement(self,x,y,position,type):
        '''
        This function will validate the placement of
        a ship on the map..
        Input: x,y - head of the ship
               position - vertical/horizontal
               type - battleship,cruiser,destroyer
        Output: 1 if placement is possible and 0 oth.

        Checks:
             o x to be a number
             o y to be in 'ABCDEFGH'
             o (x,y) to represent a valid point on board
             o ship to fit in the board
             o ship to be placed only on free cells
        '''
        if self.isNumber(x) == 0:
            return 0
        if self.fromLetterToNumber(y) == -1:
            return 0
        x = int(x)-1
        y = self.fromLetterToNumber(y)

        if self.isInBoard(x,y) == 0:
            return 0

        if type.lower() == 'battleship':
            shape = self.battleship_shape(x,y,position)
        elif type.lower() == 'cruiser':
            shape = self.cruiser_shape(x,y,position)
        else:
            shape = self.destroyer_shape(x,y,position)


        for cell in shape:
            if self.isInBoard(cell[0],cell[1]) == 0:
                return 0

        for cell in shape:
            if self.isFree(cell[0],cell[1]) == 0:
                return 0

        return 1

    def place_ship(self,x,y,type,position):
        '''
        Places a certain ship on the board
        '''
        x = int(x)-1
        y = self.fromLetterToNumber(y)

        if type.lower() == 'battleship':
            shape = self.battleship_shape(x,y,position)
        elif type.lower() == 'cruiser':
            shape = self.cruiser_shape(x,y,position)
        else:
            shape = self.destroyer_shape(x,y,position)

        for cell in shape:
            self._board[cell[0]][cell[1]] = 0

    def random_coordinates(self):
        '''
        Return random coordinates for the head
        of a possible ship
        '''
        numbers = []
        for i in range(1,9):
            numbers.append(i)

        number = choice(numbers)

        letters = ['A','B','C','D','E','F','G','H']
        letter = choice(letters)
        return  number,letter

    def computer_placement(self):
        index = 0
        ship = ['battleship','cruiser','destroyer']
        position = ['vertical','horizontal']

        while True:
            x,y = self.random_coordinates()
            pos = choice(position)
            if self.validate_placement(x,y,pos,ship[index]) == 1:
                self.place_ship(x,y,ship[index],pos)
                index += 1
            if index == 3:
                return 0

    def validateHit(self,x,y):
        '''
        A hit is valid if:
         o x is a number
         o y is in 'ABCDEFGH'
         o (x,y) describes a
         cell from the board
         o cell (x,y) has value
         ' ' or 1
        Output: 1 if valid and
        0 otherwise
        '''
        if self.isNumber(x) == 0:
            return 0
        if self.fromLetterToNumber(y) == -1:
            return 0
        x = int(x) - 1
        y = self.fromLetterToNumber(y)

        if self.isInBoard(x,y) == 0:
            return 0

        if self._board[x][y] != ' ' and self._board[x][y] != 0:
            return 0

        return 1

    def makeHit(self,x,y):
        '''
        This function makes a hit
        Returns 1 if a component
        of a ship is hit and 0
        otherwise.
        It also marks the cell
        with 1 if it is a hit and
        2 if it is a miss
        '''
        x = int(x) - 1
        y = self.fromLetterToNumber(y)

        if self._board[x][y] == ' ':
            self._board[x][y] = 2
            return 0
        else:
            self._board[x][y] = 1
            return 1

    def analyseHit(self,hit,dead_components,player = 'computer'):
        if hit == 0:
            print(player+' has missed')
            return dead_components
        else:
            print(player+' hits the component of a ship')
            return dead_components + 1

    def computerHit(self):
         '''
         The computer will randomly hit
         a certain type of cell
         1 - hit
         2 - miss
         '''
         hit_type = choice([1,2])
         if hit_type == 1:
            while True:
                x,y = self.random_coordinates()
                x = int(x) - 1
                y = self.fromLetterToNumber(y)
                if self._board[x][y] == 0:
                    self._board[x][y] = 1
                    return 1
         else:
            while True:
                x,y = self.random_coordinates()
                x = int(x) - 1
                y = self.fromLetterToNumber(y)
                if self._board[x][y] == ' ':
                    self._board[x][y] = 2
                    return 0