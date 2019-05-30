# -*- coding: utf-8 -*-
"""
Created on Thu May 30 15:44:25 2019
@author: Stacy


io read taxonomy into nlp doc
io read product descriptions into nlp doc
io read other custom model vocab

read in json files and look for matches:
    spacy_11_efficientPhraseMatching_2.py
    spacy_12_efficientPhraseMatching_3.py
use the Matcher to add patterns to vocab and look for matches
    spacy_2_theMatcher.py
    spacy_7_combiningModelsAndRules.py
    spacy_9.5_myMatcherNo1.py **************
do fuzzy matching w/ phonetic encoding (see jellyfish scripts):
    nysiis
compute string similarity:
    hellyfish.match_rating_comparison(str1, str2) # which one is best?
    token.similarity
    doc.similarity
    span.similarity
output:
    full matches
    partial matches
    no matches
write new patterns based on new info for partials and no matches
add new stuff to the custom model vocab

"""

