# -*- coding: utf-8 -*-
"""
Created on Fri May 31 19:15:42 2019
@author: Stacy

jellyfish modules for use with the controller program

"""
import jellyfish

def levenshtein():
    print('Running Levenshtein Distance (similarity as a function of distance)')
    b1 = 'Ball Bearing'
    b2 = 'bll brng'
    c1 = 'Centrifugal' 
    c2 = 'centrifigal'
    p1 = 'PUmp'
    p2 = 'pmp'
    
    b = jellyfish.levenshtein_distance(b1, b2)
    c = jellyfish.levenshtein_distance(c1, c2)
    p = jellyfish.levenshtein_distance(p1, p2)
    
    print('Ball Bearing -> bll brng: ', b)
    print('Centrifugal -> centrifigal: ', c)
    print('PUmp -> pmp: ', p)
    
    # ----  end function  ----
    
def jaroWinkler():
    print('Running Jaro-Winkler Distance (similarity as a function of distance)')
    b1 = 'Ball Bearing'
    b2 = 'bll brng'
    c1 = 'Centrifugal' 
    c2 = 'centrifigal'
    p1 = 'PUmp'
    p2 = 'pmp'
    
    b = jellyfish.jaro_winkler(b1, b2)
    c = jellyfish.jaro_winkler(c1, c2)
    p = jellyfish.jaro_winkler(p1, p2)
    
    print('Ball Bearing -> bll brng: ', b)
    print('Centrifugal -> centrifigal: ', c)
    print('PUmp -> pmp: ', p)
    