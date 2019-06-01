# -*- coding: utf-8 -*-
"""
Created on Fri May 31 19:15:42 2019
@author: Stacy

jellyfish modules for use with the controller program

"""
import jellyfish

def mrc():
    # english  -----------------------------
    tokens = ['Ball Bearing',
              'bll brng', 
              'Centrifugal', 
              'centrifigal', 
              'PUmp', 
              'pmp']
    
    print('Running Match Rating Codex (EN)...')
    
    # print tokens
    print('Tokens: ', end='')
    for i in tokens:
        print(i,' | ', end='')    
        
    # printcodes
    print('\n', end="")
    print('Codes: ', end='')
    for i in tokens:
        print(jellyfish.match_rating_codex(i), ' | ', end='')
        
    # print string match comparisons
    print('\n', end="")
    print('Comparisons: ', end='')
    print('Ball Bearing, bll brng: ', jellyfish.match_rating_comparison('Ball Bearing', 'bll brng'))    
    print('Centrifugal, centrifigal: ', jellyfish.match_rating_comparison('Centrifugal', 'centrifigal')) 
    print('PUmp, pmp: ', jellyfish.match_rating_comparison('PUmp', 'pmp'))
            
        
    # german  -----------------------------
    tokens = ['Kugellager',
              'kugelagr', 
              'Zentrifugal', 
              'zentrifkl', 
              'PUmpe', 
              'pmp']
    
    print('\n\nRunning Match Rating Codex Comparison (DE)...')
    
    # print tokens
    print('Tokens: ', end='')
    for i in tokens:
        print(i,' | ', end='')    
        
    # printcodes
    print('\n', end="")
    print('Codes: ', end='')
    for i in tokens:
        print(jellyfish.match_rating_codex(i), ' | ', end='') 
    
    # print string match comparisons
    print('\n', end="")
    print('Comparisons: ', end='')
    print('Kugellager,  kugelagr: ', jellyfish.match_rating_comparison('Kugellager', 'kugelagr'))    
    print('Zentrifugal, zentrifkl: ', jellyfish.match_rating_comparison('Zentrifugal', 'zentrifkl')) 
    print('PUmpe, pmp: ', jellyfish.match_rating_comparison('PUmpe', 'pmp'))
    
    # ----  end function  ----      