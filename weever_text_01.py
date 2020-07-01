#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 09:58:16 2019

@author: matthewsillence
"""

# find relevant text in Weever text

F_IN = 'weever_text.txt'

with open(F_IN, 'r', encoding='utf-8', newline='\n') as f_in:
    lines = f_in.readlines()
    for line in lines:
        if 'Norfolk' in line:
            print(line)
