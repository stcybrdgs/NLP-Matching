# -*- coding: utf-8 -*-
"""
Created on Thu May 30 12:25:18 2019
@author: Stacy

demo prep scripts

rem:
    A Doc is a sequence of Token objects. Access sentences and named entities, 
    export annotations to numpy arrays, losslessly serialize to compressed 
    binary strings. The Doc object holds an array of TokenC] structs. 
    
    The Python-level Token and Span objects are views of this array, 
    i.e. they don’t own the data themselves.
    
    token functions: ---------------------
    .sent    the sentence span that the token is a part of
    .text    verbatim text content
    .vocab   the vocab object of the parent doc
    .i       the index of the token within the parent document
    .lemma_  base form of the token with no inflectional suffixes
    .lower_  lowercase form of the token, equivqlent to token.text.lower()
    .shape   transform the token's string to show orthographic features, ie 'Xxxx'
    .pos_    coarse-grained part of speech
    .tag_    fine-grained part of speech
    .dep_    syntactic dependency relation
    .lang_   language of the parent document's vocabulary
    
    booleans: -----------------------------
    .is_alpha     does it consist of alphabetic chars?
    .is_digit     does it consist of digits?
    .is_lower     does it consist of all lowercase?
    .is_upper     does it consist of all uppercase
    .is_punct     is it punctuation?
    .is_space     is it whitespace?
    .is_bracket   is the token a bracket?
    .is_quote     is the token a quotation mark?
    .is_currency  is the token a currency symbol?
    .like_num     is it like a number?
    .is_oov       is the token out-of-vocabulary?
    
"""

import spacy
def main():
  nlp = spacy.load('en_core_web_sm')
  
  # basic read() 
  print('basic read: ---------------------------')
  infile = open('products_DescriptionOnly_short.csv', 'rt')
  print('py read: ')
  print(infile.read(), '\n')
  infile.seek(0) # reset cursor

  # read one description at a time and print token attr
  print('py parse: ')
  for line in infile:
      nextLine = line.rstrip()
      # nextStr = nextLine
      nlpStr = nlp(nextLine)
     
      # token functions 1
      print('token functions 1: ----------------------')
      for token in nlpStr:
          print(token.text, token.pos_, token.dep_, token.i, token.lemma_)
      
      print('\n')
      
      # token functions 2
      print('token functions 2: ----------------------')
      for token in nlpStr:
          print(token.text, token.lower_, token.shape_, token.pos_, token.tag_, token.lang_)
          
      print('\n')
      
      # token comparisons
      print('token comparisons: ----------------------')
      for token in nlpStr:
          if token.is_alpha: print(token.text, ' ALPHA')
          if token.is_digit: print(token.text, ' DIGITS')
          if token.like_num: print(token.text, ' LIKE NUM')

  # end for

  # close input data file
  infile.close()
  
  # end program
  print('Done.')
  
if __name__ == '__main__' : main()