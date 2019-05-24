# -*- coding: utf-8 -*-
"""
Created on Tue May 22 2019
@author: Stacy Bridges

testing the matcher
"""
import spacy
from spacy.matcher import Matcher

def main():
  nlp = spacy.load('en_core_web_sm')
  
  # test missing entity
  print('\ntest missing entity 1 ----------------')
  text = "New iPhone X release date leaked as Apple reveals pre-orders by mistake"  
  doc = nlp(text) 
  for ent in doc.ents:
      print(ent.text, ent.label_)
  iphone_x = doc[1:3]
  print('Missing entity: ', iphone_x)
    
  
  # test the matcher 
  print('\ntest the matcher --------------')
  # when spacy cannot match an entity, you can write a new rule
  # to allow for future matches
  # 1. Import the Matcher from spacy.matcher (imported in header)
  nlp = spacy.load('en_core_web_sm')
  doc = nlp(text) # see text string above
  
  # 2. Initialize it with the nlp object’s shared vocab.
  matcher = Matcher(nlp.vocab)
  
  # 3. Create a pattern that matches the 'TEXT' values of two tokens: "iPhone" and "X".
  pattern = [{"TEXT": "iPhone"}, {"TEXT": "X"}]
  
  # 4. Use the matcher.add method to add the pattern to the matcher.
  matcher.add("IPHONE_X_PATTERN", None, pattern)
  
  # 5. Call the matcher on the doc and store the result in the variable matches.
  matches = matcher(doc)
  
  # 6. Iterate over the matches and get the matched span from the start to the end index.
  print("Matches:", [doc[start:end].text for match_id, start, end in matches])
  for ent in doc.ents:
      print(ent.text, ent.label_)
  
    
  # writing match patterns
  # you can write more complex match patterns using
  # different token attirbutes and operators
  print('\nwriting match patterns 1 --------------')   
  # write one pattern that only matches mentions
  # of the full iOS versions: iOS 7, iOS 10, iOS 11
  matcher = Matcher(nlp.vocab) # LU nlp.vocab
  
  doc = nlp(
      "After making the iOS update, you won't notice a radical system-wide redesign: nothing like the aesthetic upheaval we got with iOS 7 ."
      "Most of iOS 11's furniture remains the same as in iOS 10 ."
      "But, you will discover some tweaks once you delve a little deeper."
      "Testing: iOS 7, iOS 10, iOS 11, iOS 7 ."
      )
  
  # Write a pattern for full iOS versions ("iOS 7", "iOS 11", "iOS 10")
  pattern = [{"TEXT": "iOS"}, {"IS_DIGIT": True}]

  # Add the pattern to the matcher and apply the matcher to the doc
  matcher.add("IOS_VERSION_PATTERN", None, pattern)
  matches = matcher(doc)
  print("Total matches found:", len(matches))

  # Iterate over the matches and print the span text
  for match_id, start, end in matches:
      print("Match found:", doc[start:end].text)
  
    
  # writing match patterns
  print('\nwriting match patterns 2 --------------')   
  doc = nlp("I need to download some stuff. I need to download PIP and to download Py, but downloading other stuff is not necessary.")
  pattern = [{"LEMMA":"download"}, {"POS":"PROPN"}]
  matcher.add("DOWNLOAD_STUFF_PATTERN", None, pattern)
  matches = matcher(doc)
  print("Total matches found: ", len(matches))
  for match_id, start, end in matches:
      print("Match found: ", doc[start:end].text)
  
  # end program
  print('\nDone.')
    
  
if __name__ == '__main__' : main()
    
    