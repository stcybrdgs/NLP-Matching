# -*- coding: utf-8 -*-
"""
Created on Tue May 22 2019

@author: Stacy Bridges

rem: using SpaCy library NLP features    
"""
import spacy
from spacy.lang.en.examples import sentences

def main():
  nlp = spacy.load('en_core_web_sm')
  exDoc = nlp(sentences[0])
  myDoc = nlp()
if__name__=='__main__' : main()
    
    