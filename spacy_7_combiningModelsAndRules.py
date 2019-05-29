# -*- coding: utf-8 -*-
"""
Created on Fri May 24 2019
@author: Stacy Bridges

           Statistical Models                 Rules-Based Systems
           -------------------------------    -------------------------------
Use cases: application needs to generalize    dictionary with finite
           based on examples                  number of examples

Examples:  product names, person names,       countries of the world,    
           subject/object relationships       cities, drug names, dog breeds

spaCy:     entity recognizer,                 tokenizer, Matcher,  
           dependency parser,                 phraseMatcher
           pos tagger

"""
import spacy
# import the Doc and Span classes from spaCy tokens
# from spacy.tokens import Doc, Span  
from spacy.matcher import Matcher

def main():
  nlp = spacy.load('en_core_web_md') 
    
  # recap of Rules-Based Matching
  # Initialize with the shared vocab
  matcher = Matcher(nlp.vocab)

  # Patterns are lists of dictionaries describing the tokens
  pattern = [{'LEMMA': 'love', 'POS': 'VERB'}, {'LOWER': 'cats'}]
  matcher.add('LOVE_CATS', None, pattern)

  # Operators can specify how often a token should be matched
  pattern = [{'TEXT': 'very', 'OP': '+'}, {'TEXT': 'happy'}]

  # Calling matcher on doc returns list of (match_id, start, end) tuples
  doc = nlp("I love cats and I'm very very happy")
  matches = matcher(doc)  
  print(matches)
  
if __name__ == '__main__' : main()
    
    