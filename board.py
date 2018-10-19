# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 14:31:48 2018

@author: testadmin
"""

import numpy as np

class Board(object):
    """
    
    Board object keeps track of all positions of p1 and p2
    
    """
    
    def __init__(self):
        
        """
        Initializes the board. This is a 3x3 numpy array with zeros.
        If p1 puts an 'X' than 1. If p2 puts an 'O' then 2
        
        """
        self.data = np.ones((3,3))*-1

    def set_piece(self,player_id,row_idx,col_idx):
        """
        Puts piece on board. 
        
        Args:
            player_id: ID of the player (1 of 2)
            row_id: Row on the board. Is zero indexed
            col_id: Column on the board. Is zero indexed
            
        Returns:
            numpy array: Updated board.
        """
        self.data[row_idx,col_idx] = player_id
        
    def possible_piece_locations(self):
        """
        Get locations where piece can be placed

        Returns:
            numpy array: value is 1 when piece can be placed
        """
        return self.data == -1

    def has_won(self,player_id):
        """
        Determines whether player has won
        
        Args:
            player_id: ID of the layer (1 or 2)
        
        Returns:
            boolean: True if player has won else False
        
        """
        mask = self.data == player_id
        horz = any(np.sum(mask,axis=1) == 3)
        vert = any(np.sum(mask,axis=0) == 3)
        trace = np.trace(mask) == 3
        trace90deg = np.trace(np.fliplr(mask)) == 3
        
        return horz | vert | trace | trace90deg


######################################
if __name__ == '__main__':
    b = Board()
    print(b.data)
    b.set_piece(1,0,0)
    print(b.data)
    print(b.possible_piece_locations())
     





