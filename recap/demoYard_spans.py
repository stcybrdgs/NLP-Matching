# -*- coding: utf-8 -*-
"""
Created on Thu May 30 12:25:18 2019
@author: Stacy

demo prep scripts

rem:
    you can import the Doc class and use it to build an nlp doc
    on the fly.

rem:
    a span is a user-specified slice from a doc object.
    .doc      the parent doc
    .sent     the sentence span that this span is part of
    .start    int  the index of the first token of the span
    .end      int  the index of the first token after the span
    .text     unicode representation of the span text
    .label_    the label to attach to the span
    .lemma_    the span's lemma
    .vector   a meaning representation of the span
    .ents     the named entities in the span
    .start    int the index of the first token of the span
    .end      int the index of the first token after the span
    .similarity  make a similarity estimate
    .as_doc   create a new Doc object corresponding to the Span
    
rem:
    see Span.to_array method at https://spacy.io/api/span

rem:
    if the model you are using has no word vectors loaded, the result of 
    Span.similarity will be based on the tagger, parser and NER, which may 
    not give useful similarity judgements. This may happen if you're using one of 
    the small models, e.g. `en_core_web_sm`, which don't ship with word 
    vectors and only use context-sensitive tensors. You can always add 
    your own word vectors, or use one of the larger models instead if 
    available.

ex:
    from spacy.attrs import LOWER, POS, ENT_TYPE, IS_ALPHA
    doc = nlp(u"I like New York in Autumn.")
    span = doc[2:3]
    # All strings mapped to integers, for easy export to numpy
    np_array = span.to_array([LOWER, POS, ENT_TYPE, IS_ALPHA])
    
    # application would be to port NLP strings into arrays for 
    # analysis in numPy
    
"""

import spacy
from spacy.tokens import Span, Doc

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
      for token in nlpStr:
          # create spans
          span1 = Span(nlpStr, 0, 2, label = 's1')
          span2 = Span(nlpStr, 3, 5, label = 's2')
          print('{0}\t{1}\t{2}\t{3}\t{4}\t{5}'.format(
                  token.text, 
                  span1.text, span1.label_,
                  span2.text, span2.label_,
                  # span1.ents,
                  span1.lemma_
                  )
          )
      # compare = span1.similarity(span2)
      # print(compare)
          
      print('\n')

   

  # end for

  # close input data file
  infile.close()
  
  # end program
  print('Done.')
  
if __name__ == '__main__' : main()