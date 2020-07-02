# antiquarian_texts
The files and Python scripts in this repository provide two steps to retrieving lines from the full text of digitized antiquarian publications that include a keyword. In this example, that keyword is 'Norfolk', the county in England.

## Retrieving texts from archive.org
The first scripts (archive_org_text_01.py and archive_org_text_02.py) use the urllib module to open a file from a URL. In both cases, these are plain text files from the site archive.org.

The Python script allows the user to read in these files and read out as .txt files to save locally.

## Returning lines with an assigned keyword
The second set of scripts (weever_text_01.py and browne_text.py) read in the local file and using the .readlines() method retrieves all lines from the text containing the assigned keyword ('Norfolk') and allows the user to print each line.

## Checking word frequencies
The script word_frequency.py is designed to check the frequency of tokens within the weever_text.txt file, although can be adapted for other files. This uses the NLTK (Natural Language Toolkit) stopwords package to filter out common stopwords in English, and then generate a dataframe of the top 50 tokens and their occurrence in the text. Further removal of punctuation and tokens that result from OCR errors will be required. 

## General guidance
Ensure that you have the Python scripts and the text files in the same directory that you have defined in your Python environment.
