# -*- coding: utf-8 -*-
"""
Created on Tue May 28 2019
@author: Stacy Bridges

Efficient Phrase Matching
 - raseMatcher like regular expressions or keyword search – but with access to the tokens!
 - Takes Doc object as patterns
 - More efficient and faster than the Matcher
 - Great for matching large word lists

"""
import spacy
# import the Doc and Span classes from spaCy tokens
# from spacy.tokens import Doc, Span  
# from spacy.matcher import Matcher
from spacy.matcher import PhraseMatcher

def main():
    nlp = spacy.load('en_core_web_sm')
    matcher = PhraseMatcher(nlp.vocab)
    
    pattern = nlp("Golden Retriever")
    matcher.add('DOG', None, pattern)
    doc = nlp("I have a Golden Chicken and a Golden Retrievable Fish and a Golden Retriever")
    
    # Iterate over the matches
    for match_id, start, end in matcher(doc):
        # Get the matched span
        span = doc[start:end]
        print('Matched span:', span.text)
  
if __name__ == '__main__' : main()
    
    