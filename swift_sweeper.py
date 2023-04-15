import random
import numpy as np
from ..bot_control import Move

class SwiftSweeper:

    def __init__(self):
        self.state1 = 0
        self.state2 = 0
        self.target = [0, 0]

    def get_name(self):
        return "The Swift Sweeper"

    def get_contributor(self):
        return "Jerrel"

    def determine_next_move(self, grid, enemies, game_info):

        if self.state1 == 1 and np.array_equal(self.position, self.target) == False:
            return self.move_to_target()
        else:
            self.state1 = 0
            
        if self.state2 == 0:
            if self.check_move_possible(game_info,1):
                return Move.UP
            elif self.check_move_possible(game_info,2):
                self.state2 = 1
                return Move.RIGHT
            else:
                self.state1 = 1
                return self.move_to_target()
        elif self.state2 == 1:
            if self.check_move_possible(game_info,3):
                return Move.DOWN
            elif self.check_move_possible(game_info,2):
                self.state2 = 0
                return Move.RIGHT
            else:
                self.state1 = 1
                self.state2 = 0
                return self.move_to_target()
    
    def check_move_possible(self, game_info, move):
        if move == 1:
            if self.position[1] < game_info.grid_size-1:
                return True
            else:
                return False
                
        if move == 2:
            if self.position[0] < game_info.grid_size-1:
                return True
            else:
                return False
                
        if move == 3:
            if self.position[1] > 0:
                return True
            else:
                return False
                
        if move == 4:
            if self.position[0] > 0:
                return True
            else:
                return False


    def move_to_target(self):
        # Move in direction of target
        if self.target[0] > self.position[0]:
            return Move.RIGHT
        elif self.target[0] < self.position[0]:
            return Move.LEFT
        elif self.target[1] > self.position[1]:
            return Move.UP
        else:
            return Move.DOWN