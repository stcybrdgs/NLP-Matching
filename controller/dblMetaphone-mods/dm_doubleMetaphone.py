# -*- coding: utf-8 -*-
"""
Created on Tue 6/4
@author: Stacy

double metaphone modules for use with the controller program

"""
from metaphone import doublemetaphone

def dlbMetaphone():
    print('Running Double Metaphone:...')

    strings = ['Ball Bearing', 'bll brng', 'Centrifugal', 'centrifigal', 'PUmp', 'pmp']
    
    i = 0
    for item in strings:
        rStr = item + str(i)
        print(item, '->', doublemetaphone(rStr))
    
    # ----  end function  ----
    
