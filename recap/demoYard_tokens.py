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
    
    token.sent    the sentence span that the token is a part of
    token.text    verbatim text content
    token.vocab   the vocab object of the parent doc
    token.i       the index of the token within the parent document
    token.lemma_  base form of the token with no inflectional suffixes
    token.lower_  lowercase form of the token, equivqlent to token.text.lower()

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
          print(token.text, token.lower_)
      print('\n')

  # end for

  # close input data file
  infile.close()
  
  # end program
  print('Done.')
  
if __name__ == '__main__' : main()