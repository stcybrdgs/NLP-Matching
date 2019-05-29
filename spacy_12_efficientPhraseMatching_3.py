# -*- coding: utf-8 -*-
"""
Created on Tue May 28 2019
@author: Stacy Bridges

This script does a few different things:
    it uses country matcher on a long text
    it analyzes the syntax 
    it updates doc entities with the matched countries

"""
import spacy
import json
from spacy.lang.en import English
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span

def main():
    with open('countries.json') as f:
        COUNTRIES = json.loads(f.read())

    with open('country_text.txt') as f:
        TEXT = f.read()
        
    nlp = English()
    matcher = PhraseMatcher(nlp.vocab)
    patterns = list(nlp.pipe(COUNTRIES))
    matcher.add('COUNTRY', None, *patterns)
    
    # Create a doc and find matches in it
    doc = nlp(TEXT)
    
    # test print of ents
    print('test print of ents: -----------------------------')
    print([(ent.text, ent.label_) for ent in doc.ents])
    print('\n')
    
    # Iterate over the matches
    print('iterate over the matches: -----------------------')
    for match_id, start, end in matcher(doc):
        # Create a Span with the label for 'GPE'
        span = Span(doc, start, end, label = 'GPE')
        
        # Overwire the doc.ents and add the span
        doc.ents = list(doc.ents) + [span]
        
        # Get the span's root head token
        span_root_head = span.root.head
        
        # Print the text of the span root's 
        # head token and the span text
        print(span_root_head.text, '-->', span.text)
        
    # print spacer    
    print('\n')
    
    # Print the entities in the document
    print('fin print of ents: -----------------------------')
    print([(ent.text, ent.label_) for ent in doc.ents if ent.label_ == 'GPE'])
    
if __name__ == '__main__' : main()  
    
    