# -*- coding: utf-8 -*-
"""
Created on Thu May 23 20:33:36 2019
@author: Owner

testing jellyfish
"""

import jellyfish

def main():
    # declare test strings
    # rem: u prefix is required jellyfish convention
    str1 = u'Jellyfish' 
    str2= u'Smellyfish'
    
    # test Phonetic Encoding ------------------------------
    # Metaphone
    r1 = jellyfish.metaphone(str1)
    r2 = jellyfish.metaphone(str2)
    print('Metaphone: ', r1, ", ", r2)
    
    # American Soundex
    r1 = jellyfish.soundex(str1)
    r2 = jellyfish.soundex(str2)
    print('Soundex: ', r1, ", ", r2)
    
    # NYSIIS
    r1 = jellyfish.nysiis(str1)
    r2 = jellyfish.nysiis(str2)
    print('NYSIIS: ', r1, ", ", r2)

    # Match Rating Codex    
    r1 = jellyfish.match_rating_codex(str1)
    r2 = jellyfish.match_rating_codex(str2)
    print('Match Rating Codex: ', r1, ", ", r2)
    
    # test Stemming ---------------------------------------
    
    
    # test String Comparison ------------------------------
    # Levenshtein Distance
    r = jellyfish.levenshtein_distance(str1, str2)
    print('Levenshtein Distance: ', r)

    # Damerau-LevenshteinDistance
        
    # Hamming Distance
    result = jellyfish.hamming_distance(str1, str2)
    print('Hamming Distance: ', r)

    # Jaro Distance
    result = jellyfish.jaro_distance(str1, str2)
    print('Jaro Distance: ', r)
    
    # Jaro-Winkler Distance
    result = jellyfish.jaro_winkler(str1, str2)
    print('Jaro-Winkler Distance: ', r)
    
    # Match Rating Approach (comparison)
 
    
    
    
    # end program
    print('Done.')
    
if __name__ == '__main__' : main()