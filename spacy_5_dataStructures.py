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
  token_texts = [token.text for token in doc]
  pos_tags = [token.pos for token in doc]
  
  for index, pos in enumerate(pos_tags):
      # check if the current token is a proper noun
      if pos = 'PROPN':
          # check if the next token is a verb
          if pos_tags[index + 1] == 'VERB':
              result = token_texts[index]
              print('Found proper noun before a verb: ', result)
  
  # end program
  print('\nDone.')
    
  
if __name__ == '__main__' : main()
    
    