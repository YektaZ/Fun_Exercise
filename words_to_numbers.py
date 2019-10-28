# coding: utf-8
def words_to_numbers(input):

    ph_num = ''
    for i in range(len(input)):
        if input[i].upper() in 'ABC':
            ph_num = ph_num + '2'
        elif input[i].upper() in 'DEF':
            ph_num = ph_num + '3'
        elif input[i].upper() in 'GHI':
            ph_num = ph_num + '4'
        elif input[i].upper() in 'JKL':
            ph_num = ph_num + '5'
        elif input[i].upper() in 'MNO':
            ph_num = ph_num + '6'
        elif input[i].upper() in 'PQRS':
            ph_num = ph_num + '7'
        elif input[i].upper() in 'TUV':
            ph_num = ph_num + '8'
        elif input[i].upper() in 'WXYZ':
            ph_num = ph_num + '9'
        else:
            ph_num = ph_num + input[i]

    ph_num = ph_num.replace('-','')
    ph_num = ph_num[0] + '-' + ph_num[1:4] + '-' + ph_num[4:7] + '-' + ph_num[7::]
    
    
    return(ph_num)
