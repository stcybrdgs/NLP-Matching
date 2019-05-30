# -*- coding: utf-8 -*-
"""
Created on Thu May 30 16:14:46 2019
@author: Stacy

PIPELINES
You can customize the pipeline components to:
•	make a function execute automatically when you call nlp
•	add your own metadata to documents and tokens
•	update built-in-attributes like doc.ents
•   compute your own values based on tokens and their attributes
•   add named entities, for example based on a dictionary

PIPELINE:
load language model
create an nlp object by running a doc through the pipeline:
     tokenizer           tokenize he text
     custom compnents
     tagger              part-of-speech tagger
     parser              dependency parser
     ner                 named entity recognizer
    
a pipeline component is a function that takes a doc, modifies it, 
and returns it. A custom pipeline component can be added using 
the nlp.add_pipe method (the tokenizer always runs first, followed
by whichever component is at the head of the pipeline):

    ex:
    nlp.add_pipe(custom_component)	
   
    def custom_component(doc):
        # do something to the doc
        return doc
    ex: 
    nlp.add_pipe(component, last=True)  # add last in pipeline
    nlp.add_pipe(component, first=True)  # add first in pipeline
    nlp.add_pipe(component, before='ner')  # add before ner component
    nlp.add_pipe(component, after='tagger')  # add after tagger component


"""
import spacy


# CREATE A PIPELINE COMPONENT -----------------------------
def custom_component(doc):
    # print doc length (ie, number of tokens)
    print('doc length: ', len(doc))
    
    # return doc object
    return doc

# MAIN PROGRAM --------------------------------------------
def main():
    nlp = spacy.load('en_core_web_sm')
    
    # ADD A CUSTOM PIPELINE COMPONENT ----------------------
    # add the component to the front of the pipeline
    nlp.add_pipe(custom_component, first=True)
    
    # METHOD TO READ FILE INTO NLP DOC AND  ---------------
    # THEN PRINT SENTENCE BY SENTENCE
    # read products info into an nlp doc
    inFile = open('products_DescriptionOnly_short.csv', 'rt')
    doc = nlp(inFile.read())
    inFile.close()
    
    # store each record as an index in a list
    records = list(doc.sents)
    
    # print each record
    for record in records:
        print(record)
   
    # print a list of the pipeline component names
    print('\npipeline components: ', nlp.pipe_names)
    # print(nlp.pipeline)
    
    # print document entities:
    for ent in doc.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_)
    
    # end program
    print('\nDone.')
    
if __name__ == '__main__' : main()
