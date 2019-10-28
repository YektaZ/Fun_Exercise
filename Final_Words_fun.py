# coding: utf-8
def Final_Words_fun(num_input):
    
    import loadDictionary as D
    import number_to_options as NO
    
    num_input = num_input.replace('-','')
    
    #     :::: define Dictionary :::
    ENGLISH_WORDS = D.loadDictionary()
    
    #     :::: find all string options :::
    unique_options = NO.number_to_options(num_input)
    
    
    #     :::: find meaningful words in English Dictionary :::
    #     :::: using backtracking method
    
    def backtrack_forward(words,string): #drop first letter each step
        if len(string)<1:
            Final_Words.append(words)
        else:
            if string in ENGLISH_WORDS:
                words.append(string)
            words = backtrack_forward(words,string[1::])

    def backtrack_revers(words,string): #drop last letter each step
        if len(string)<1:
            Final_Words.append(words)
        else:
            if string in ENGLISH_WORDS:
                words.append(string)
            words = backtrack_revers(words,string[0:-1])

    Final_Words = []
    
    for string in unique_options:
        backtrack_forward([],string)
        
    for string in unique_options:
        backtrack_revers([],string)
        
#     import pdb; pdb.set_trace()
    
    Final_Words = sum(Final_Words, [])
    used = set()
    Final_Words = [x for x in Final_Words if x not in used and (used.add(x) or True)]

    return Final_Words
