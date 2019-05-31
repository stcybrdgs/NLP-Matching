# -*- coding: utf-8 -*-
"""
Created on Thu May 30 16:14:46 2019
@author: Stacy

PIPELINES
The processing pipeline always depends on the statistical model 
and its capabilities. For example, a pipeline can only include an 
entity recognizer component if the model includes data to make 
predictions of entity labels. This is why each model will specify 
the pipeline to use in its meta data, as a simple list containing 
the component names.


"""
# IMPORTS -------------------------------------------------
import csv
import spacy
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span

# GLOBALS -------------------------------------------------
nlp = spacy.load('en_core_web_sm')
matcher = PhraseMatcher(nlp.vocab)

# FUNCTIONS -----------------------------------------------
def product_component(doc):
    # apply the matcher to the doc
    matches = matcher(doc)
    
    # create a span for each match and assign the label 'PRODUCT'
    spans = [Span(doc, start, end, label="PRODUCT") for match_id, start, end in matches]

    # overwrite the doc.ents with the matched spans
    doc.ents = spans
    return doc

# MAIN PROGRAM ---------------------------------------------
def main():
    products = ['roller bearing',
                'bll brng',
                'Polishers',
                'Buffers'
                ]
    
    doc = nlp.pipe(products)
    product_patterns = list(doc)
    print('product_patterns: ', product_patterns)
    matcher.add('PRODUCT', None, *product_patterns)
   
    '''
    # test
    i = 0
    for item in product_patterns:
        print(product_patterns[i])
        i += 1
    '''
    
    # add the component to the pipeline after the'ner' component
    nlp.add_pipe(product_component, after='ner')
    print('\npipe names: ', nlp.pipe_names)
    
    # process the text 
    infile = open('products_DescriptionOnly_short.csv', 'rt')
    doc = nlp(infile.read())
    infile.close()
    
    # store each doc record as an index in a list
    records = list(doc.sents)
    
    # print each record
    print('\nproduct descriptions: ')
    for record in records:
        print(record)    
    
    # print the text and label for the doc.ents
    print('\ntext and labels for doc.ents: ')
    print([(ent.text, ent.label_) for ent in doc.ents])
    
    # end program
    print('\nDone.')
    
if __name__ == '__main__' : main()
