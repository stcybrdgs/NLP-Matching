# -*- coding: utf-8 -*-
"""
Created on Tue May 28 2019
@author: Stacy Bridges

Efficient Phrase Matching
 - raseMatcher like regular expressions or keyword search – but with access to the tokens!
 - Takes Doc object as patterns
 - More efficient and faster than the Matcher
 - Great for matching large word lists
 
 - pumps and ball bearings taxonomies
 - use the taxonomies as new patterns for the matcher
 - consider each product entry to be a separate doc OR
 - make sure the product id and it's description are coupled in 
   sequence, and then take an entire set of product descriptions as a 
   single doc, where the processor uses the ID as a delimiter

 - PhraseMatcher performs keyword search on a doc, but instead
   of only finding strings, it gives you direct access to 
   the tokens in context.
 - PhraseMatcher takes Doc objects as patterns.
 - It is great for matching large dictionaries and word lists
   on large volumes of text.

"""
import spacy
# import the Doc and Span classes from spaCy tokens
# from spacy.tokens import Doc, Span  
# from spacy.matcher import Matcher
from spacy.matcher import PhraseMatcher

def main():
    nlp = spacy.load('en_core_web_sm')
    matcher = PhraseMatcher(nlp.vocab)
    
    pattern1 = nlp('brng')
    pattern2 = nlp('bearing')
    matcher.add('BEARING', None, pattern1)
    matcher.add('BEARING', None, pattern2)
    doc = nlp('123 Deep grve bll brng 2710 Timken, 456 Cylind rllr brng 4630 RHP, 789 Bore Diameter 40mm inner ring width 23 mm spherial roller bearing')
    
    # Iterate over the matches
    for match_id, start, end in matcher(doc):
        # Get the matched span
        span = doc[start:end]
        print('Matched span:', span.text)

  
if __name__ == '__main__' : main()  
    
    