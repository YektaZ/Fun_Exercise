# coding: utf-8
def Formating_fun(num_input, One_Word):
    
    import words_to_numbers as W
    
    output = ''
    
    num = W.words_to_numbers(One_Word).replace('-','') # get the numbers back again
        
    id = num_input.find(str(num)) # find the id for the starting letter
        
    output = output + num_input[0:id] + One_Word # get the output partially
    
    l = len(output)
    
    if l == 11:
        output = output[0] + '-' + output[1:4] + '-' + output[4:7] + output[7::]
    elif 7<l:
        output = output[0] + '-' + output[1:4] + '-' + output[4:7] + output[7::] + num_input[l::]
    elif 4<l<8:
        output = output[0] + '-' + output[1:4] + '-' + output[4::] + num_input[l:7] + '-' + num_input[7::]
    else:
        output = output[0] + '-' + output[1:l] +  num_input[l:4] + '-' + num_input[4:7] + '-' + num_input[7::]
        
    return output
