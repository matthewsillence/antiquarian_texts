#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 15:49:03 2020

@author: matthewsillence
"""

# find relevant text in Browne text

F_IN = 'browne_text.txt'

with open(F_IN, 'r', encoding='utf-8', newline='\n') as f_in:
    lines = f_in.readlines()
    for line in lines:
        if 'Norfolk' in line:
            print(line)