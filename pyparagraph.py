#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 17:20:33 2018

@author: tegaileleji
"""


import re

# Files to load and output (Remember to change these)
#Input_file = "/Users/tegaileleji/Desktop/UCBSAN201805DATA1/02-Homework/03-Python/Instructions/solutions/PyParagraph/raw_data/paragraph_2.txt"
Input_file = "raw_data/paragraph_1.txt"
output_file = "paragraph_analysis.txt"
txt_paragraph = ""

with open(Input_file) as data_in_txt:

    txt_paragraph = data_in_txt.read().replace("\n", " ")
word_split = txt_paragraph.split(" ")
word_count = len(word_split)
letter_counts = []

for word in word_split:
    letter_counts.append(len(word))
    

average_letter_count = sum(letter_counts) / float(len(letter_counts))
sentence_split = re.split("(?<=[.!?]) +", txt_paragraph)
#sentence_split = re.sub("(?<=[.!?]) +", txt_paragrapha)
#print(letter_counts)



#print(sentence_split)
sentence_count = len(sentence_split)

words_in_sentence = []


for sentence in sentence_split:
    number_of_words_in_sentence = len(sentence.split(" "))
    words_in_sentence.append(number_of_words_in_sentence)

avg_sentence_len = sum(words_in_sentence) / float(len(words_in_sentence))

output = (
    f"\nParagraph Analysis\n"
    f"-----------------\n"
    f"Approximate Word Count: {word_count}\n"
    f"Approximate Sentence Count: {sentence_count}\n"
    f"Average Letter Count: {average_letter_count}\n"
    f"Average Sentence Length: {avg_sentence_len}\n")

print(output)

with open(output_file, "a") as txt_file:
    txt_file.write(output)
    
    