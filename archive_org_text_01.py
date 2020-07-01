#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 09:26:21 2019

@author: matthewsillence
"""


# Download text from archive.org site and save as a .txt file

from urllib.request import urlopen

URL = 'https://archive.org/stream/b30334330/b30334330_djvu.txt'
SAVE_FILE = 'weever_text.txt'

with urlopen(URL) as f_in:
    text_file = f_in.read()

with open(SAVE_FILE, 'wb') as f_out:
    f_out.write(text_file)