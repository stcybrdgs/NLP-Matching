# -*- coding: utf-8 -*-
"""
Created on Thu May 23 20:33:36 2019
@author: Owner

testing jellyfish
"""

import jellyfish

def main():
    lv = jellyfish.levenshtein_distance(u'jellyfish', u'smellyfish')
    jaro = jellyfish.jaro_distance(u'jellyfish', u'smellyfish')
    mp = jellyfish.metaphone(u'Jellyfish')
    sdx = jellyfish.soundex(u'Jellyfish')
    nys = jellyfish.nysiis(u'Jellyfish')
    mr = jellyfish.match_rating_codex(u'Jellyfish')
    
    print('Levenshtein Distance: ', lv)
    print('Jaro Distance: ', jaro)
    print('Metaphone: ', mp)
    print('Soundex: ', sdx)
    print('NYSIIS: ', nys)
    print('Match Rating: ', mr)
    
    # end program
    print('Done.')
    
if __name__ == '__main__' : main()