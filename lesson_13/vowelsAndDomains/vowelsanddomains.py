import re 

def start_with_vowel(str):
    regex_pattern = '^[eE]\w*'
    string_output = re.findall(regex_pattern, str, flags = re.IGNORECASE)

    return string_output

print(start_with_vowel('Errors should never pass silently. Unless explicitly silenced.'))

# Write a function that uses a regex expression to return a list with all the words that start with a vowel.
# Exmaple:
# Input: 'Errors should never pass silently. Unless explicitly silenced.'
# Output: ['Errors', 'Unless', 'explicitly']



# Write another function that uses a regex expression to return a list of emails that all have the domain of gmail.com.
# Exmaple:
# Input: 'aa@xyz.com bbb@abc.com cccc@cisco.com'
# Output: ['aa@gmail.com', 'bbb@gmail.com', 'cccc@gmail.com']

