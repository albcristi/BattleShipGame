from board_repo.board_repository import *

class ui:

    def mainMenu(self):
        print('play')
        print('x')

    def mainCommand(self):
        command = input('Enter your command\n>>>')
        command = command.split(' ')
        return command

    def placementInstructions(self):
        print('You will have to place one battleship,one cruiser')
        print('and one destroyer...The ships can not overlap and ')
        print('can be placed only on unoccupied squares')
        print('Place them with attention!')

    def placementCommand(self,type):
        command = input(type+'>')
        command = command.split(' ')
        return command

    def shipPlacement(self,game_board):
        '''
        The placement of the ships will take
        place here...Any kind of error that
        might occur during placement will
        be printed here
        '''
        self.placementInstructions()
        ships = ['battleship','cruiser','destroyer']
        index = 0
        while True:
            try:
                command = self.placementCommand(ships[index])
                if len(command) != 3:
                    raise ValueError('Invalid command')

                if command[2].lower() != 'vertical' and command[2].lower() != 'horizontal':
                    raise ValueError('Position can be: vertical or horizontal')
                if game_board.validate_placement(command[0],command[1],command[2],ships[index]) == 0:
                    raise ValueError('Make sure the coordinates are good and that the ship can be placed')
                game_board.place_ship(command[0],command[1],ships[index],command[2])
                print('Boards looks like')
                print(game_board.str())
                index += 1
                if index == 3:
                    return 0
            except ValueError as error:
                print(error)

    def getHit(self):
        command = input('hit > ')
        command = command.split(' ')
        return command

    def hit_time(self,human_board,computer_board):
        '''
        The second part of the game will take place here
        '''
        print('Let the war begin!')
        human_hits = 0
        computer_hits = 0
        while True:
            try:
                command = self.getHit()

                if len(command) != 2:
                    raise  ValueError('Invalid hit!')
                if computer_board.validateHit(command[0],command[1]) == 0:
                    raise ValueError('Make sure you make a valid hit, coordinates are valid and spot \n was not hit before')
                hit_data = computer_board.makeHit(command[0],command[1])
                human_hits = computer_board.analyseHit(hit_data,human_hits,'human')
                if human_hits == 9:
                    print('You win')
                    print(computer_board.str())
                    return 0
                else:
                    print('Computer board:')
                    print(computer_board)

                hit_data = human_board.computerHit()
                computer_hits = human_board.analyseHit(hit_data,computer_hits)
                if computer_hits == 9:
                    print('Computer wins!')
                    print(human_board.str())
                else:
                    print('YourBoard')
                    print(human_board)

            except ValueError as error:
                print(error)

    def gamePlay(self):
        human_board = Board()
        computer_board = Board()
        self.shipPlacement(human_board)
        computer_board.computer_placement()
        print(computer_board.str())
        self.hit_time(human_board,computer_board)


    def main_exe(self):
        #self.mainMenu()
        while True:
            try:
               self.mainMenu()
               command = self.mainCommand()
               if len(command) != 1:
                   raise ValueError('Invalid Command')
               else:
                   if command[0].lower() == 'play':
                       self.gamePlay()
                   elif command[0].lower() == 'x':
                       return 0
                   else:
                       raise ValueError('Invalid Command')
            except ValueError as error:
                print(error)