# -*- coding: utf-8 -*-
"""
Created on Tue May 28 2019
@author: Stacy Bridges


"""
import spacy
# import the Doc and Span classes from spaCy tokens
# from spacy.tokens import Doc, Span  
from spacy.matcher import Matcher

def main():
    nlp = spacy.load('en_core_web_sm')
    matcher = Matcher(nlp.vocab)
    matcher.add('DOG', None, [{'LOWER': 'golden'}, {'LOWER': 'retriever'}])
    doc = nlp("I have a Golden Retriever")
    
    for match_id, start, end in matcher(doc):
        span = doc[start:end]
        print('Matched span:', span.text)
        
        # Get the span's root token and root head token
        print('Root token:', span.root.text)
        print('Root head token:', span.root.head.text)
        
        # Get the previous token and its POS tag
        print('Previous token:', doc[start - 1].text, doc[start - 1].pos_)
  
if __name__ == '__main__' : main()
    
    