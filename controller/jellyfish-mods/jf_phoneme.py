# -*- coding: utf-8 -*-
"""
Created on Fri May 31 19:15:42 2019
@author: Stacy

jellyfish modules for use with the controller program

"""
import jellyfish

def soundex():
    tokens = ['Ball Bearing',
              'bll brng', 
              'Centrifugal', 
              'centrifigal', 
              'PUmp', 
              'pmp']
    
    print('Running SOUNDEX...')
    
    # print tokens
    print('Tokens: ', end='')
    for i in tokens:
        print(i,' | ', end='')
    
    # printcodes
    print('\n', end="")
    print('Codes: ', end='')
    for i in tokens:
        print(jellyfish.soundex(i), ' | ', end='')
    
    # ----  end function  ----    
    
def nysiis():
    tokens = ['Ball Bearing',
              'bll brng', 
              'Centrifugal', 
              'centrifigal', 
              'PUmp', 
              'pmp']
    
    print('Running NYSIIS...')
    
    # print tokens
    print('Tokens: ', end='')
    for i in tokens:
        print(i,' | ', end='')
    
    # printcodes
    print('\n', end="")
    print('Codes: ', end='')
    for i in tokens:
        print(jellyfish.nysiis(i), ' | ', end='')
    
    # ----  end function  ----

