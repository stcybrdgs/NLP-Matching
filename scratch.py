# -*- coding: utf-8 -*-
"""
Created on Tue May 28 2019
@author: Stacy Bridges

"""
import spacy
# from spacy import displacy
# from spacy.matcher import Matcher

def main():
    # import a language model
    nlp = spacy.load('en_core_web_sm')
    
    # import a text
    from spacy.lang.en.examples import sentences

    # print the text
    index = 0
    for i in sentences:
        doc = nlp(sentences[index])
        print(doc.text)
        index += 1
        
    # import product des riptions
    inFile = open('products.txt', 'rt')
    
    for line in inFile:
        nextLine =  nlp(line.rstrip())
        print(nextLine.text)
   
    inFile.close()    
        
    # end program
    print('Done.')
    
if __name__ == '__main__' : main()  
    
    