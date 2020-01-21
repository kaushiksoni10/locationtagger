import re

def clean(sentences):
    #removing non_ascii characters
    sentences = "".join(i for i in sentences if ord(i)<128)
    #changing non string to string.
    sentences = str(sentences)
    #1. Removing numbers.
    sentences_1 = re.sub("[^a-zA-Z&',.;-]"," ", sentences)
    #2. Removing multiple spaces with single space
    sentences_2 = re.sub(r'\s+', ' ',sentences_1, flags=re.I)
    words = sentences_2.split()
    newsentence = ' '.join(words)
    return(newsentence)
