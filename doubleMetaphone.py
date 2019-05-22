# -*- coding: utf-8 -*-
"""
Created on Tue May 21 16:41:11 2019

@author: Stacy Bridges
"""

from metaphone import doublemetaphone
from enum import Enum

class Threshold(Enum):
    WEAK = 0
    NORMAL = 1
    STRONG = 2

def double_metaphone(value):
    print(doublemetaphone(value))
    return doublemetaphone(value)

def double_metaphone_compare(tuple1,tuple2,threshold):
    if threshold == Threshold.WEAK:
        if tuple1[1] == tuple2[1]:
            return True
    elif threshold == Threshold.NORMAL:
        if tuple1[0] == tuple2[1] or tuple1[1] == tuple2[0]:
            return True
    else:
        if tuple1[0] == tuple2[0]:
            return True
    return False

def main():
    print('Done.')

if__name__=='__main__' : main()
    
    