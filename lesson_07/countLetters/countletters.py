def countLetter(str): 
    #split_str = str.split('') 
    word_dict = {} 
    st = list(str.upper()) 

    for char in st:
        print(char)
        if 'A' <= char <= 'Z':
            word_dict[char] += 1
            
    return word_dict


wordString = "AaBb"
print(countLetter(wordString))