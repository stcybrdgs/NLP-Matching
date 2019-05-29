# -*- coding: utf-8 -*-
"""
Created on Tue May 28 2019
@author: Stacy Bridges

Sometimes it’s more efficient to match exact strings instead of 
writing patterns describing the individual tokens. 
This is especially true for finite categories of things (like countries).

"""
import spacy
import json
from spacy.lang.en import English

def main():
    with open('countries.json') as f:
        COUNTRIES = json.loads(f.read())
    
    nlp = English()
    doc = nlp('The United States of America says Czech Republic may help Slovakia protect its airspace.')
    
    # Import the PhraseMatcher and initialize it
    from spacy.matcher import PhraseMatcher
    
    matcher = PhraseMatcher(nlp.vocab)
    
    # Create pattern Doc objects and add them to the matcher
    # This is the faster version of: [nlp(country) for country in COUNTRIES]
    patterns = list(nlp.pipe(COUNTRIES))
    matcher.add('COUNTRY', None, *patterns)
    
    # Call the matcher on the test document and print the result
    matches = matcher(doc)
    print([doc[start:end] for match_id, start, end in matches])
  
if __name__ == '__main__' : main()  
    
    