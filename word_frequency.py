#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 13:46:22 2020

@author: matthewsillence
"""

# Most frequent words

# Import NLTK and pandas packages
import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 

F_IN = 'weever_text.txt'

with open(F_IN, 'r', encoding='utf-8', newline='\n') as f_in:
    raw_text = f_in.read()  
    
# Set the stopwords list
    stop_words = set(stopwords.words('english')) 
    tokens = word_tokenize(raw_text) 
    stopped = [w for w in tokens if not w in stop_words] 
    stopped = [] 

# Run for loop on tokens with stopwords list condition  
for w in tokens: 
    if w not in stop_words: 
        stopped.append(w)  
        
# Set frequencies of all tokens 
freq_all = nltk.FreqDist(tokens)

# Set frequencies of tokens without stopwords
freq_dist = nltk.FreqDist(stopped)
    
# Print the 50 most common tokens in the stopped list
top50 = freq_dist.most_common(50)
    
# Create a dataframe of the most common tokens in the stopped list
df = pd.DataFrame(top50)
    
# Set the column headings in the dataframe
df.columns = ['token', 'occurrence']
    
#Print the frequencies of all tokens 
print(freq_all.most_common(50))

# Print the dataframe of tokens in the stopped list
print(df)




    
    
    