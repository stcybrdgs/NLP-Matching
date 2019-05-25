# -*- coding: utf-8 -*-
"""
Created on Fri May 24 2019
@author: Stacy Bridges

spaCy Data Structures:
shared vocabulary, lexemes, and string store

spaCy stores all data that's shared across multiple documents in a 
vocabulary -- the Vocab -- which includes words, but also the labels 
schemes for tags and entities.

spaCy encodes all strings to hash values to save memory and stores the
string only once in the string store. . . the string store is available
as nlp.vocab.strings. 

The string store is a lookup table that works in both directions, so you
can look up a string to get its hash or loook up a hash to get its 
string value, ie:
    
  coffee_hash = nlp.vocab.strings['coffee']
  coffee_string = nlp.vocab.strings[coffee_hash]

"""
import spacy
# from spacy.matcher import Matcher
from spacy.lang.en import English
from spacy.lang.de import German

def main():
  # create an English and German nlp object
  nlp = English() # spacy.load('en_core_web_sm')
  nlp_de = German() # nlp = spacy.load("de_core_news_sm")
  
  # look up a string and hash using in the Vocab
  print('\nShared vocab and String Store -----------------')
  doc = nlp("I love coffee")
  print('hash value:', doc.vocab.strings['coffee'])
  print('string value:', doc.vocab.strings[3197928453018144401])
  
  # lexemes: entries in the vocabulary
  # a lexeme object is an entry in the vocabulary that
  # conatins the context-independent information about a word
  # rem: orth means hash
  print('\nLexemes: entries in the Vocabulary -----------------')
  lexeme = doc.vocab['coffee']
  print('word: ', lexeme.text)
  print('hash: ', lexeme.orth)
  print('alphanumeric?: ', lexeme.is_alpha)
  
  # practice 1: look up a string in vocab to get the hash
  print('\npractice 1: English nlp obj ----------------------')
  doc = nlp('My favorite guitar is a parlor guitar by Art and Lutherie.')
  guitar_hash = doc.vocab.strings['guitar']
  print('guitar hash:\t', guitar_hash)
  
  guitar_string = doc.vocab.strings[13533102915073649304]
  print('guitar string:\t', guitar_string)  
  
  # practice 2: 
  print('\npractice 1: English & German nlp obj ----------------------')
  bowie_id = doc.vocab.strings['guitar']
  print('bowie_id: ', bowie_id)
  print('bowie hash:', doc.vocab.strings[13533102915073649304])
  
  
  # end program
  print('\nDone.')
    
  
if __name__ == '__main__' : main()
    
    