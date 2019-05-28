# -*- coding: utf-8 -*-
"""
Created on Fri May 24 2019
@author: Stacy Bridges


"""
import spacy
# import the Doc and Span classes from spaCy tokens
from spacy.tokens import Doc, Span  


def main():
  nlp = spacy.load('en_core_web_sm') 
  
  # create lists for building a doc
  print('Create Doc #1: -------------------------')
  words = ['spaCy', 'is', 'useful', 'for', 'NLP', '!']
  spaces = [True, True, True, True, False, False]
  
  # create a doc from the words and spaces lists
  # and pass in the vocab
  doc = Doc(nlp.vocab, words=words, spaces=spaces)
  print(doc.text)
  print('\n')
  
  # create lists for building another doc
  print('Create Doc #2: -------------------------')
  words2 = ['Jazz', 'Winston', 'is', 'the', 'best', '!']
  spaces2 = [True, True, True, True, False, False]
  
  # create a doc from the words and spaces lists
  # and pass in the vocab
  doc2 = Doc(nlp.vocab, words=words2, spaces=spaces2)
  print(doc2.text)
  print('\n')
  
  # create a span for 'Jazz Winston' from the doc
  # and assign it the label 'DOG'
  span = Span(doc2, 0, 2, label = 'DOG')
  print(span.text, span.label_)
  
  # add the span to the doc's entities
  doc2.ents = [span]
  
  # print entities' text and labels
  print([(ent.text, ent.label_) for ent in doc2.ents])
  
  # end program
  print('\nDone.')
    
  
if __name__ == '__main__' : main()
    
    