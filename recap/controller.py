# -*- coding: utf-8 -*-
"""
Created on Fri May 31 04:10:06 2019
@author: Stacy

controller program for testing spacy nlp features

rem: use case: convert us date to uk date

"""

# IMPORTS  ------------------------------
import jellyfish
import spacy


# FUNCTIONS  -----------------------------
def menu():
    print('\n')
    print('----------------------  MENU  ----------------------')
    print('m  -  menu')
    print('e -  exit')
    print('\nWX MATCHING ENGINE:')
    print('1  -  Tokenizer')
    print('2  -  Tagger')
    print('3  -  Parser')
    print('4  -  NER')
    print('5  -  Matcher')
    print('\nPHONETIC ENCODING:\t STRING COMPARISON:')
    print('6  -  Soundex\t\t 8  -  Levenshtein Distance')
    print('7  -  NYSIIS\t\t 9  -  Jaro-Winkler Distance')
    print('              \t\t 0  -  Match Rating Codex')
    # print('\n')
    print('----------------------------------------------------')
    # ----  end function  ----

def tokenizer():
    print('tokenizer')
    
    # ----  end function  ----
    
def tagger():
    print('tagger')
    
    # ----  end function  ----

def parser():
    print('parser')
    
    # ----  end function  ----

def ner():
    print('ner')
    
    # ----  end function  ----

def matcher():
    print('matcher')
    
    # ----  end function  ----
    
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
    
def levenshtein():
    print('levenshtein')
    
    # ----  end function  ----    
    
def jaroWinkler():
    print('jaroWinkler')
    
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
        
    # german  -----------------------------
    tokens = ['Kugellager',
              'kugelagr', 
              'Zentrifugal', 
              'zentrifkl', 
              'PUmpe', 
              'pmp']
    
    print('\n\nRunning Match Rating Codex (DE)...')
    
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
    print('Kugellager, kugelagr: ', jellyfish.match_rating_comparison('Kugellager', 'kugelagr'))    
    print('Zentrifugal, zentrifkl: ', jellyfish.match_rating_comparison('Zentrifugal', 'zentrifkl')) 
    print('PUmpe, pmp: ', jellyfish.match_rating_comparison('PUmpe', 'pmp'))
    
    # ----  end function  ----    
    

# MAIN  ---------------------------------
# controller program for nlp functions
def main():
    # declare menu items
    menuItems = ['m','1','2','3','4','5','6','7','8','9', '0']
    
    # print menu to console
    menu()
    
    # get menu selection from user
    choice = input('Select a menu item: ')
    
    # process the user's menu selection
    while choice != 'e':
        # catch invalid user selection
        match = False
        for i in menuItems:
            if i == choice: match = True
        if match == False: print('Invalid selection.')
        
        # process valid user selection
        else:
            if choice == 'e': break # end program
            if choice == 'm': menu()
            if choice == '1': tokenizer()
            if choice == '2': tagger()
            if choice == '3': parser()
            if choice == '4': ner()
            if choice == '5': matcher()
            if choice == '6': soundex()
            if choice == '7': nysiis()
            if choice == '8': levenshtein()
            if choice == '9': jaroWinkler()
            if choice == '0': mrc()
        
        # get new user selection
        choice = input('\nSelect a menu item: ')

    # end program
    print('\nExit program. Done.')

if __name__ == '__main__' : main()