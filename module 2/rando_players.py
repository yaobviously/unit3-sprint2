# -*- coding: utf-8 -*-
"""
Created on Wed May 12 23:59:45 2021

@author: yaobv
"""
import numpy as np
import pandas as pd

class Player:
    def __init__(self, speed = 50, strength = 50, shot = 50):
        
        self.speed = speed
        self.strength = strength
        self.shot = shot
        self.total = self.speed + self.strength + self.shot
        

    
def generate_players(n = 100):
    
    speed = np.random.normal(50, 5, n) 
    strength = np.random.normal(50, 5, n)
    shot = np.random.normal(50, 5, n)
    
    players = [Player(s, st, sh) for s, st, sh in zip(speed, strength, shot)]
    return players
    
    
draft = generate_players()

for player in draft:
    print(player.speed, player.strength, player.shot, player.total)