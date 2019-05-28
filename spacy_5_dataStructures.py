# -*- coding: utf-8 -*-
"""
Created on Fri May 24 2019
@author: Stacy Bridges

the code in this script is trying to analyze a text and collect 
all proper nouns that are followed by a verb.

"""
import spacy
# import the Doc and Span classes from spaCy tokens
# from spacy.tokens import Doc, Span  

def main():
  nlp = spacy.load('en_core_web_sm') 
  doc = nlp('Berlin is a nice city')
  
  # get all tokens and pos tags
  # USE NATIVE TOKEN ATTRIBUTES INSTEAD OF
  # LISTS OF token_texts AND pos_tags
  # THEN, CONVERT THE RESULTS TO STRINGS AS 
  # LATE AS POSSIBLE... ie, avoid doing this:
  #     token_texts = [token.text for token in doc]
  #     pos_tags = [token.pos for token in doc]
  
  # iterate over the tokens:
  for token in doc:
      print(token.pos_)
      # check if the current token is a proper noun
      if token.pos_ == 'PROPN':
          # check if the next token is a verb
          if doc[token.i + 1].pos_ == 'VERB':
              print('Found proper noun before a verb: ', token.text)
  
  # end program
  print('\nDone.')
    
  
if __name__ == '__main__' : main()
    
    