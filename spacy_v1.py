# -*- coding: utf-8 -*-
"""
Created on Tue May 22 2019

@author: Stacy Bridges

rem: using SpaCy library NLP features    
"""
import spacy
from spacy.lang.en.examples import sentences

def main():
  products = open('products.txt', 'rt')
  str = u"I can't imagine spending $3000 for a single bedroom apartment in N.Y.C."
  
  nlp = spacy.load('en_core_web_sm')
  sent = nlp(sentences[0])
  str = nlp(str)
  #prod = prod[0]
  
  # sent functions ----------------------  
  print(sent.text)
  
  for token in sent:
      print(token.text, token.pos_, token.dep_)

  # str functions ----------------------  
  print(str.text)
  
  for token in str:
      print(token.text, token.pos_, token.dep_)
   
  # prod functions ---------------------
  for line in products:
    print(line.rstrip())
  
  products.close()  
    
  
if __name__ == '__main__' : main()
    
    