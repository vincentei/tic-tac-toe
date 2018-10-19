# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 20:21:52 2018

@author: testadmin
"""

from board import Board
import random
import numpy as np
import pandas as pd

class Game(object):
    """
    Game object manages all aspects of the game. It contains a board object and
    ....TODO
    """
    
    def __init__(self, players):
        """
        Initialize the game
            
        Args:
            board (Board): game board
            turn (int): current turn number
            players: list of player objects
        """
        self.board = Board()
        self.turn = 0
        self.current_player_id = random.randint(0,1)
        self.players = players
        self.assign_players()    
        self.df_stats = pd.DataFrame(columns = ['turn','current_player','board'])
    
    def assign_players(self):
        """
        Have each player join the game.
        """
        for pid, player in enumerate(self.players):
            player.join(self,pid)
        
        return

    def winner(self):
        """
        Return the winning player, if any.
        
        Returns:
            Player/None: the winning player, or None if there is none.
        """
        id_winner = None
        for i in range(len(self.players)):
            if  self.board.has_won(i):
                id_winner = i
        return id_winner

    def has_ended(self):
        """
        Checks if the game has ended.
        
        Returns:
            bool: True if there is a winner, else False.
        """
        has_ended = False
        if np.sum(self.board.data != -1) == 9:
            has_ended = True
        elif self.winner() != None:
            has_ended = True
        
        return has_ended
    
    def play_turn(self):
        """
        
        Plays one turn of the game.
        """
        self.update_df_stats()
        self.turn += 1
        pid = self.current_player_id
        row_idx, col_idx = self.players[pid].put_piece_on_board()
        
        self.board.set_piece(pid,row_idx,col_idx)
        self.next_turn()
        
        return

    def next_turn(self):
        """
        Jump to the next turn.
        """
        if self.current_player_id == 0:
            self.current_player_id = 1
        else:
            self.current_player_id = 0
        return

    def update_df_stats(self):
        """
        update the dataframe with stats
        
        """
        
        self.df_stats = self.df_stats.append({'turn':self.current_player_id,
                              'current_player':self.current_player_id,
                              'board':str(self.board.data.flatten())},ignore_index=True)
        
    def get_games_stats(self):

      return self.df_stats        


######################################
if __name__ == '__main__':
    g = Game()
    #b.set_piece(1,0,0)
    print (g.get_current_player())
    #b.possible_piece_locations()
    
    
