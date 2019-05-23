# -*- coding: utf-8 -*-
"""
Created on Tue May 22 2019
@author: Stacy Bridges

rem: using SpaCy library NLP features 
rem: export annotations to numpy arrays
rem: lu prodigy @ https://prodi.gy/

lu:  
(spacy POS distinctions)
JJ NN PRP MD VB IN NNP  

lu: NER returns which labels (token.label_) ? 
"""
import spacy
from spacy.lang.en.examples import sentences
# from spacy import displacy
# from spacy.lang.en.stop_words import STOP_WORDS
# spacy provides pre-trained models for syntax

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

  # close input data file
  infile.close()
  
  print('products example 2: ---------------------------')
  # print all data --------------------
  infile = open('products_DescriptionOnly.csv', 'rt')
  fData = infile.read()
  
  # the doc object is processed as it is passed
  # to the language object
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

  # examine additional spacy functions
  print('\nexplore additional spacy functions:')
  for token in nlpData[:6]:
      print('token.text: ', token.text) # the original string
      print('token.pos_: ', token.pos_) # the part of speech
      print('token.tag_: ', token.tag_) #
      print('token.dep_: ', token.dep_) # dependency
      print('token.head.text: ', token.head.text) # navigate up the tree
      print('token.lefts: ', token.lefts) # left child of head
      print('token.rights: ', token.rights) # right child of head
      print('\n-----------------')
  
  # apply more spacy features to a string
  nuDoc = nlp('This is an SKF product called Ball Bearing for $45 USD')
  for token in nuDoc:
      print('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}'.format(
          token.text,       # original string
          token.idx,        # index
          token.lemma_,     # base form of the word
          token.is_punct,   # bool: is it punctuation
          token.is_space,   # bool: is it a space
          token.shape_,     # visual signature ie: Xxxxx
          token.pos_,       # part of speech
          token.tag_        # ?  
      )
  )
  # end for
  
  # end program
  print('\nDone.')
    
  
if __name__ == '__main__' : main()
    
    