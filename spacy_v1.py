# -*- coding: utf-8 -*-
"""
Created on Tue May 22 2019

@author: Stacy Bridges

rem: using SpaCy library NLP features    
"""
import spacy
from spacy.lang.en.examples import sentences

def main():
  nlp = spacy.load('en_core_web_sm')
  
  # sent functions ----------------------  
  print('setence example: ---------------------------')
  sent = nlp(sentences[0])
  print(sent.text)
  
  for token in sent:
      print(token.text, token.pos_, token.dep_)

  print('\n')
  
  # str functions ----------------------  
  print('string example: ---------------------------')
  sampleString = u"I can't imagine spending $3000 for a single bedroom apartment in N.Y.C."
  str = nlp(sampleString)
  print(str.text)
  
  for token in str:
      print(token.text, token.pos_, token.dep_)
   
  print('\n')
  
  # product file functions ---------------------
  print('products example 1: ---------------------------')
  infile = open('products_DescriptionOnly_short.csv', 'rt')
  print(infile.read(), '\n')
  
  # reset cursor
  infile.seek(0)
  
  # start for
  for line in infile:
      nextLine = line.rstrip()
      # nextStr = nextLine
      nlpStr = nlp(nextLine)
     
      for token in nlpStr:
          print(token.text, token.pos_, token.dep_)
  
      print('\n')
  # end for
  
  infile.close()
  
  print('products example 2: ---------------------------')
  # print all data --------------------
  infile = open('products_DescriptionOnly.csv', 'rt')
  fData = infile.read()
  nlpData = nlp(fData)
  print(nlpData)
  
  # print tokens ----------------------
  print('\ntokens:')
  for tok in nlpData[:6]:
      print('{} -> {} -> {}'.format(tok.text, tok.pos_, tok.ent_type_))
  
  # print entities --------------------
  print('\nentities:')
  for ent in nlpData.ents:
      print('{} --> {}'.format(ent.string, ent.label_))
    
  # print persons ---------------------
  # rem: NLTK comes with pre-trained models for splitting text 
  #      to sentences and sentences to words
  print('\n')
  orgNum = 0
  carNum = 0
  perNum = 0
  print('ORGs:')
  for ent in nlpData.ents:
      if ent.label == spacy.symbols.ORG:
          orgNum += 1
          print(ent.text)
      if ent.label == spacy.symbols.CARDINAL:
          carNum += 1
      if ent.label == spacy.symbols.PERSON:
          perNum += 1
      # end if   
  print('\n')
  print('# of ORG: ', orgNum)
  print('# of CARDINAL: ', carNum)
  print('# of PERSON: ', perNum)
  infile.close() 

  # end program
  print('\nDone.')
    
  
if __name__ == '__main__' : main()
    
    