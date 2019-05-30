# -*- coding: utf-8 -*-
"""
Created on Tue May 28 2019
@author: Stacy Bridges

this script demonstrates method for reading external
doc into an nlp object
"""
import spacy
# from spacy import displacy
# from spacy.matcher import Matcher

def main():
    # import a language model
    nlp = spacy.load('en_core_web_sm')
    
    # import a text
    print('imported sentences document ----------------')
    from spacy.lang.en.examples import sentences

    # print the text
    index = 0
    for i in sentences:
        doc = nlp(sentences[index])
        print(doc.text)
        index += 1
        
    # import product descriptions
    print('\n')
    print('imported products doc ----------------')
    inFile = open('products.txt', 'rt')
    
    for line in inFile:
        nextLine =  nlp(line.rstrip())
        print(nextLine.text)
   
    inFile.close()    
        
    # import product descriptions
    print('\n')
    print('imported products doc to nlp obj ----------------')
    inFile = open('products.txt', 'rt')
    doc = nlp(inFile.read())
    inFile.close()
    
    # print method
    for token in doc:
        print(token.text, '-->', token.pos_)
        #index += 1
    
    # end program
    print('Done.')
    
if __name__ == '__main__' : main()  
    
    