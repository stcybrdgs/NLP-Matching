# -*- coding: utf-8 -*-
"""
Created on Fri May 24 2019
@author: Stacy Bridges

Comparing semantic similarity:
* spaCy can compare two objects and predict similarity
* Doc.similarity(), Span.similarity(), Token.similarity()

NEEDS A MODEL THAT HAS WORD VECTORS INCLUDED!  
en_core_web_lg (large model) - YES
en_core_web_md (medium model) - YES (20,000 WVs !)
en_core_web_sm (small model) - NO

this script looks at word vectors as well as 
the similarity rating between:
    - two docs
    - two tokens

"""
import spacy
# import the Doc and Span classes from spaCy tokens
# from spacy.tokens import Doc, Span  

def main():
  nlp = spacy.load('en_core_web_md') 
  doc1 = nlp('Two bananas in pyjamas')
  doc2 = nlp('Two oranges in shoes')  
  
  bananas_vector = doc1[1].vector
  pyjamas_vector = doc1[3].vector
  
  # print out vectors
  print('Banana Vector: ---------------------------')
  print(bananas_vector)
  print('\n')
  
  print('Pyjamas Vector: ---------------------------')
  print(pyjamas_vector)
  print('\n')
  
  # compare two docs (doc1 and doc2)
  print('Comparing doc1 and doc2: -------------------')
  print(doc1.similarity(doc2))
  print('\n')
  
  # compare two tokens
  print('Comparing tokens: -------------------')
  token1 = doc1[1]
  token2 = doc2[1]
  print(token1.similarity(token2))
  
  # end program
  print('\nDone.')
  
  # another similarity exercise
  # to reinforce how to create vars for 
  # tokens and spans...
  # Compare a document to a token
  print('Comparing doc to token: -----------------')
  doc = nlp("I like home-made pizza")
  token = nlp("onions")[0]
  print(doc.similarity(token))
    
  # Compare a span with a document
  print('Comparing doc to span: -----------------')
  span = nlp("I like salads with chicken fingers")[2:5]
  doc = nlp("Hutts sells hamburgers")
  print(span.similarity(doc))  
  
  # Compare a span with a document
  print('Comparing token to token: -----------------')
  doc = nlp("Hutts sells really good shakes and hamburgers")
  token1, token2 = doc[4], doc[6]
  print(token1.similarity(token2))  
  
if __name__ == '__main__' : main()
    
    