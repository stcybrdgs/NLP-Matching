# -*- coding: utf-8 -*-
"""
Created on Fri May 31 04:10:06 2019
@author: Stacy

controller program for testing spacy nlp features

rem: use case: convert us date to uk date
    
"""
# IMPORTS  ------------------------------
# py files
import sys
sys.path.append('jellyfish-mods/')
sys.path.append('spacy-mods/')

import jf_distance
import jf_phoneme
import jf_match
import spacy_modules

# py libs
import spacy

# GLOBALS  -------------------------------
nlp = spacy.load('en_core_web_sm')

# LOCAL FUNCTIONS  -----------------------------
def menu():
    print('\n')
    print('----------------------  MENU  ----------------------')
    print('m  -  menu')
    print('e -  exit')
    print('\nWX MATCHING ENGINE:')
    print('1  -  Tokenizer')
    print('2  -  Tagger')
    print('3  -  Entity Parser')
    print('4  -  NER')
    print('5  -  Matcher')
    print('\nPHONETIC ENCODING:\t STRING COMPARISON:')
    print('6  -  Soundex\t\t 8  -  Levenshtein Distance')
    print('7  -  NYSIIS\t\t 9  -  Jaro-Winkler Distance')
    print('              \t\t 0  -  Match Rating Codex')
    # print('\n')
    print('----------------------------------------------------')
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
            if choice == '1': spacy_modules.tokenizer()
            if choice == '2': spacy_modules.tagger()
            if choice == '3': spacy_modules.parser()
            if choice == '4': spacy_modules.ner()
            if choice == '5': spacy_modules.matcher()
            if choice == '6': jf_phoneme.soundex()
            if choice == '7': jf_phoneme.nysiis()
            if choice == '8': jf_distance.levenshtein()
            if choice == '9': jf_distance.jaroWinkler()
            if choice == '0': jf_match.mrc()
        
        # get new user selection
        choice = input('\nSelect a menu item: ')

    # end program
    print('\nExit program. Done.')

if __name__ == '__main__' : main()