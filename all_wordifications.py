# coding: utf-8
def all_wordifications(num_input):
    
    import Final_Words_fun as FW
    import Formating_fun as F

    Final_Words = FW.Final_Words_fun(num_input)
    
    if len(Final_Words)>0:
        for w in Final_Words:
            i = num_input.replace('-','')
            print(F.Formating_fun(i, w))
