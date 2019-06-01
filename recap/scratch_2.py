# -*- coding: utf-8 -*-
"""
Created on Fri May 31 17:20:09 2019
@author: Stacy

"""

import json
from spacy.lang.en import English
from spacy.tokens import Span
from spacy.matcher import PhraseMatcher

def main():
    with open("countries.json") as f:
        COUNTRIES = json.loads(f.read())
    
    with open("capitals.json") as f:
        CAPITALS = json.loads(f.read())
    
    nlp = English()
    matcher = PhraseMatcher(nlp.vocab)
    matcher.add("COUNTRY", None, *list(nlp.pipe(COUNTRIES)))
    
    
    def countries_component(doc):
        # Create an entity Span with the label 'GPE' for all matches
        matches = matcher(doc)
        doc.ents = [Span(doc, start, end, label="GPE") for match_id, start, end in matches]
        return doc
    
    
    # Add the component to the pipeline
    nlp.add_pipe(countries_component)
    print(nlp.pipe_names)
    
    # Getter that looks up the span text in the dictionary of country capitals
    get_capital = lambda span: CAPITALS.get(span.text)
    
    # Register the Span extension attribute 'capital' with the getter get_capital
    Span.set_extension("capital", getter=get_capital, force=True)
    
    # Process the text and print the entity text, label and capital attributes
    doc = nlp("Czech Republic says it may help Slovakia protect its airspace")
    print([(ent.text, ent.label_, ent._.capital) for ent in doc.ents])
    
    for ent in doc.ents:
        if ent.label_ == 'GPE': print('Found a GPE!')
        
    
    # end program
    print('Done.')
    
if __name__ == '__main__' : main()