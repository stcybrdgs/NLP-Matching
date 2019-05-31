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
from spacy.matcher import PhraseMatcher
nlp = spacy.load('en_core_web_sm')

# FUNCTIONS  -----------------------------
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

def tokenizer():
    print('Running Tokenizer...\n')
    
    # read in the product descriptions
    print('read product descriptions: --------')
    infile = open('products_DescriptionOnly_short.csv', 'rt')
    print(infile.read(), '\n')
    infile.seek(0) # reset cursor
    
    # demonstrate token functions
    # parse into tokens:
    for line in infile:
        nextLine = line.rstrip()
        nlpStr = nlp(nextLine)
     
        # token functions 1
        print('parse into tokens: ----------------------')
        for token in nlpStr:
            print(token.text)
        
        print('\n')
    
    infile.close()
    # ----  end function  ----
    
def tagger():
    print('Running Tagger...\n')
    
    # read in the product descriptions
    print('read product descriptions: --------')
    infile = open('products_DescriptionOnly_short.csv', 'rt')
    print(infile.read(), '\n')
    infile.seek(0) # reset cursor
    
    # print pos, tag, shape
    # infile.seek(0) # reset cursor
    for line in infile:
        nextLine = line.rstrip()
        nlpStr = nlp(nextLine)
     
        # token functions 1
        print('Create Tags: Token - POS - Shape - Dependency: ----------------------')
        for token in nlpStr:
            print(token.text,' - ',token.pos_,' - ',token.tag_,' - ',token.shape_, ' - ', token.dep_)
        
        print('\n')

    infile.close()
    # ----  end function  ----
    
    # ----  end function  ----

def parser():
    print('Running Entity Parser...\n')
    
    # read in the product descriptions
    print('read product descriptions: --------')
    infile = open('products_DescriptionOnly_short.csv', 'rt')
    print(infile.read(), '\n')
    infile.seek(0) # reset cursor
    
    # test
    infile.seek(0) # reset cursor
    data = infile.read()
    nlpData = nlp(data)
    print('Find entities and labels: ----------------------')
    for ent in nlpData.ents:
        print('{} --> {}'.format(ent.string, ent.label_))
        
    print('\n')
    
    infile.close()
    # ----  end function  ----

def ner():
    print('The ner module is disconnected...')
    
    # ----  end function  ----

def matcher():
    print('Running the Phrase Matcher...\n')
    matcher = PhraseMatcher(nlp.vocab)
    
    print('Input doc:')
    print('123 Deep grve bll brng 2710 Timken')
    print('456 Cylind rllr brng 4630 RHP')
    print('789 Bore Diameter 40mm inner ring width 23 mm spherial roller bearing')
    print('\n')
    
    print('add new string patterns to matcher: brng, bearing...')
    print('search doc and return matches...\n')
    
    pattern1 = nlp('brng')
    pattern2 = nlp('bearing')
    matcher.add('BEARING', None, pattern1)
    matcher.add('BEARING', None, pattern2)
    doc = nlp('123 Deep grve bll brng 2710 Timken, 456 Cylind rllr brng 4630 RHP, 789 Bore Diameter 40mm inner ring width 23 mm spherial roller bearing')
    
    # Iterate over the matches
    for match_id, start, end in matcher(doc):
        # Get the matched span
        span = doc[start:end]
        print('Matched span:', span.text)
    
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