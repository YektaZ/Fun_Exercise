# coding: utf-8
def number_to_words(num_input):
    
    import Final_Words_fun as FW
    import Formating_fun as F
    
    num_input = num_input.replace('-','')

    Final_Words = FW.Final_Words_fun(num_input)
    
    #     :::: creat an output :::    
    
    One_Word = max(Final_Words, key=len) #pick the longest word
    
    if len(Final_Words)>0: # if there is any option
    
       output = F.Formating_fun(num_input, One_Word)
#         import pdb; pdb.set_trace()
    else: # no option
        print('no possible word')
        
    return output
