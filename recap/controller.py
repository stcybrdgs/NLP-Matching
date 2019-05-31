# -*- coding: utf-8 -*-
"""
Created on Fri May 31 04:10:06 2019
@author: Stacy

controller program for testing spacy nlp features

Phonetic Encoding
  American Soundex
  Metaphone
  NYSIIS
  Match Rating Approach (codex)

Stemming
  Porter Stemmer

String Comparison
  Levenshtein Distance
  Damerau-Levenshtein Distance
  Hamming Distance
  Jaro Distance
  Jaro-Winkler Distance
  Match Rating Approach (comparison)

convert us date to uk date

"""

# imports ------------------------------
# import spacy

# functions-----------------------------
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
    print('soundex')
    
    # ----  end function  ----    
    
def nysiis():
    print('nysiis')
    
    # ----  end function  ----
    
def levenshtein():
    print('levenshtein')
    
    # ----  end function  ----    
    
def jaroWinkler():
    print('jaroWinkler')
    
    # ----  end function  ----    
    
# main ---------------------------------
def main():
    # declare menu items
    menuItems = ['m','1','2','3','4','5','6','7','8','9']
    
    # print menu to console
    menu()
    
    # get menu selection from user
    choice = input('Select a menu item: ')
    
    # process menu selection
    while choice != 'e':
        # catch invalid user selection
        match = False
        for i in menuItems:
            if i == choice: match = True
        if match == False: print('Invalid selection.')
        
        # process valid user selection
        else:
            if choice == 'e': break
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
        
        # get new user selection
        choice = input('\nSelect a menu item: ')

     
    # end program
    print('\nExit program. Done.')

if __name__ == '__main__' : main()