# -*- coding: utf-8 -*-
"""
Created on Thu May 30 16:14:46 2019
@author: Stacy

"""
# IMPORTS -------------------------------------------------
import csv

# MAIN PROGRAM ---------------------------------------------
def main():
    with open('products.txt') as f:
        reader = csv.reader(f, delimiter=',')
        products = list(reader)
        
    print(products)
    f.close()
    
if __name__ == '__main__' : main()
