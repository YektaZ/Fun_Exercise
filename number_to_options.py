# coding: utf-8
def number_to_options(num_input):
    
    import re
    
    num_input = num_input.replace('-','')
    
    mydic = {1:'0', 2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz', 0:'0'}
    
    def backtrack(combination, next_digits):
            if len(next_digits) == 0:
                Word_options_temp.append(combination)
            else:
                for letter in mydic[int(next_digits[0])]:
                    backtrack(combination + letter, next_digits[1:])
                    
    Word_options_temp = []
    if num_input:
        backtrack("", num_input)
        
    #     :::: split the words if 0 or 1 is in the middle :::
    Word_options = []
    for i in range(len(Word_options_temp)):
        Word_options = Word_options + re.split(r'0',Word_options_temp[i])

    #     :::: remove the 0's and 1's -- make all letters upper case -- find unique values :::
    Word_options = [i for i in Word_options if i!='t']
    Word_options = [i for i in Word_options if i!='']
    Word_options = [i.upper() for i in Word_options]
    used = set()
    unique_options = [x for x in Word_options if x not in used and (used.add(x) or True)]


    return unique_options
