# coding: utf-8 
#yz

def loadDictionary():
    
    import pandas as pd
    
    dicFile = pd.read_csv('dictionary.txt')
    EnglishWords = []
    for i in dicFile.iloc[7::,0]:
        EnglishWords.append(i.replace('\\',''))
    return EnglishWords
