# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 20:26:53 2018

@author: testadmin
"""

import game
import player
import numpy as np
import pandas as pd

p1 = player.Player()
p2 = player.Player()

players = [p1, p2] 


g = game.Game(players)


#df_game = pd.DataFrame(columns = ['turn','current_player','board'])
df_all = []


for i in range(2):
    while not(g.has_ended()):
        g.play_turn()
    df_game = g.get_games_stats()
    df_game['winner'] = g.winner()
    df_game['game_id'] = g.winner()
    
    df_all.append(g.get_games_stats())   


df_all = pd.concat(df_all,ignore_index=True)




