def validAnagram(str1, str2):
    if len(str1) != len(str2):
        return False 
    
    
    str1_dict = {}

    for letter in str1:
        if letter in str1_dict:
            str1_dict[letter] += 1
        else:
            str1_dict[letter] = 1 

    for letter in str2:
        if letter in str1_dict and str1_dict[letter] > 0:
            str1_dict[letter] -= 1
           
        else:
            return False   
    
    return True 


print(validAnagram('aaz', 'zza')) # false
print(validAnagram('anagram', 'nagaram')) # true
print(validAnagram('rat', 'car')) # false
print(validAnagram('qwerty', 'qeywrt')) # true


