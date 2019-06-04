# -*- coding: utf-8 -*-
"""
Created on Fri May 31 04:10:06 2019
@author: Stacy

spacy functions

"""
# IMPORTS  ------------------------------
# py libs
import spacy
from spacy.matcher import PhraseMatcher

# GLOBALS  -------------------------------
nlp = spacy.load('en_core_web_sm')

# SPACY FUNCTIONS  -----------------------------
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
    
    print('Find dependency objects: ----------------------')
    '''
    for ent in nlpData.ents:
        print('{} --> {}'.format(ent.string, ent.label_))

    print('\n')
    '''
    
    for sent in nlpData.sents:
        for token in sent:
            print(token.text, token.dep_, token.head.text, token.head.pos_, [child for child in token.children])
    
    infile.close()
    # ----  end function  ----

def ner():
    # print('The ner module is disconnected...')
    print('Running Named Entity Recognizer...\n')
    
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