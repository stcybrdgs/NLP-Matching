# -*- coding: utf-8 -*-
"""
Created on Fri May 31 17:20:09 2019

@author: Stacy
this script demonstrates:
    add pipe components
    set custom attributes
"""

import spacy
# import global classes
from spacy.tokens import Doc, Token, Span

# Define the custom component
def length_component(doc):
    # Get the doc's length
    doc_length = len(doc)
    print("This document is {} tokens long.".format(doc_length))
    # Return the doc
    return doc

def preprocessor(doc):
    print('Running the preprocessor...')
    return doc


def main():
    # Load the small English model
    nlp = spacy.load("en_core_web_sm")
    
    # Add the component first in the pipeline and print the pipe names
    nlp.add_pipe(length_component, first=True)
    print(nlp.pipe_names)
    
    nlp.add_pipe(preprocessor, first=True)
    print(nlp.pipe_names)
    
    # Process a text
    doc = nlp("This is a sentence.")
    
    # add custom metadata
    Doc._.title = 'My document'
    Token._.is_color = True
    Span._.has_color = False

    # set extensions on fht eDoc, Token, and Span
    Doc.set_extension('title', default=None)
    Token.set_extension('is_color', default=False)
    Span.set_extension('has_color', default=False)
    
    
    # end program
    print('Done.')
    
if __name__ == '__main__' : main()