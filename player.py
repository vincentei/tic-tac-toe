# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 22:45:06 2018

@author: testadmin
"""

import numpy as np

class Player(object):
    """
    
    
    
    """
    
    def __init__(self):
        
        """
        
        
        """
        self.game = None
        self.player_id = None
    
    def join(self,game,player_id):
        
        self.game= game
        self.player_id = player_id

    def put_piece_on_board(self):
        
        possible_piece_locations = self.board.possible_piece_locations()
        
        coord = np.where(possible_piece_locations)
        
        idx = np.random.randint(len(coord[0]))
        
        row_idx = coord[0][idx]
        col_idx = coord[1][idx]
        
        return row_idx, col_idx

    @property
    def board(self):
        """
        Return the game board.

        Raises:
            ValueError if the player is not assigned.

        Returns:
            Board: the game board of the game assigned to.
        """
        
        return self.game.board


