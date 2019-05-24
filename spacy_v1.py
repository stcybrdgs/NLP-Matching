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
iob tagging = IOB: inside/outside/beginning of entity 
"""
import spacy
from spacy.lang.en.examples import sentences
from spacy import displacy
from spacy.matcher import Matcher

# from spacy import displacy
# from spacy.lang.en.stop_words import STOP_WORDS
# spacy provides pre-trained models for syntax

def main():
  nlp = spacy.load('en_core_web_sm')
  
  
  # sentence functions 
  print('setence example: ---------------------------')
  sent = nlp(sentences[0])
  print(sent.text)
  
  for token in sent:
      print(token.text, token.pos_, token.dep_)

  print('\n')
  
  
  # string example functions 
  print('string example: ---------------------------')
  sampleString = u"I can't imagine spending $3000 for a single bedroom apartment in N.Y.C."
  str = nlp(sampleString)
  print(str.text)
  
  for token in str:
      print(token.text, token.pos_, token.dep_)
   
  print('\n')
  
  
  # product file functions 
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
  
  
  # product file functions (2)
  print('products example 2: ---------------------------')
  # print all data 
  infile = open('products_DescriptionOnly.csv', 'rt')
  fData = infile.read()
  
  # the doc object is processed as it is passed
  # to the language object
  nlpData = nlp(fData)
  print(nlpData)
  
  # print tokens
  print('\ntokens:')
  for tok in nlpData[:6]:
      print('{} -> {} -> {}'.format(tok.text, tok.pos_, tok.ent_type_))
  
  # print entities
  print('\nentities:')
  for ent in nlpData.ents:
      print('{} --> {}'.format(ent.string, ent.label_))
    
  # print persons
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
  print('\nexplore additional spacy functions: ---------------')
  for token in nlpData[:6]:
      print('token.text: ', token.text)             # the original string
      print('token.ent_type_: ', token.ent_type_)   # entity
      print('token.ent_iob_: ', token.ent_iob_)     # ?
      print('token.pos_: ', token.pos_)             # the part of speech
      print('token.tag_: ', token.tag_)             # ?
      print('token.dep_: ', token.dep_)             # dependency
      print('token.head.text: ', token.head.text)   # navigate up the tree
      print('token.lefts: ', token.lefts)           # left child of head
      print('token.rights: ', token.rights)         # right child of head
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
  
  
  # test displaCy
  # viewable in jupyter notebook
  print('\ndisplaCy snippet for jupyter notebook ---------------------------')
  doc = nlp('I just bought 2 shares at 9 a.m. because the stock went up 30% in just 2 days according to the WSJ')
  displacy.render(doc, style='ent', jupyter=True)
  
  
  # test the chunker
  print('\ntest the chunker 1 -----------')
  doc = nlp("Wall Street Journal just published an interesting piece on crypto currencies")
  for chunk in doc.noun_chunks:
      print(chunk.text, chunk.label_, chunk.root.text)
  
  
  # test the chunker  
  print('\ntest the chunker 2 -----------')
  doc = nlp('Bore Diameter 40mm inner ring width 23 mm spherial roller bearing')
  for chunk in doc.noun_chunks:
      print(chunk.text, chunk.label_, chunk.root.text)
      
      
  # test span object
  print('\ntest span object -----------')    
  span = doc[2:6] # 40mm inner ring   
  print(span.text)
  
  
  # test lexical attributes
  print('\ntest lexical attributes ---------------')
  doc = nlp("It costs $5.")
  print('Text:    ', 'It costs $5')
  print('Index:   ', [token.i for token in doc])
  print('Text:    ', [token.text for token in doc])
  print('is_alpha:', [token.is_alpha for token in doc])
  print('is_punct:', [token.is_punct for token in doc])
  print('like_num:', [token.like_num for token in doc])
  
  
  # test the dependency parcer
  print('\ntest the dependency parcer -----------')
  doc = nlp('Wall Street Journal just published an interesting piece on crypto currencies')
  for token in doc:
      print("{0}/{1} <--{2}-- {3}/{4}".format(token.text, token.tag_, token.dep_, token.head.text, token.head.tag_))
 
    
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
    
    