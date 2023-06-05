mary_lyrics = ["Mary had a little lamb, little lamb, little lamb. Mary had a little lamb, its fleece was white as snow.", "And everywhere that Mary went. Mary went. Mary went. And everywhere that Mary went, the lamb was sure to go.", "It followed her to school one day, school one day, school one day. It followed her to school one day, which was against the rule.", "It made the children laugh and play, laugh and play, laugh and play. It made the children laugh and play to see the lamb at school."]

with open("Mary.txt", 'w') as outfile:
    for line in mary_lyrics:
        outfile.write(line + '\n')


with open('Mary.txt', 'r') as infile:
    for line in infile: 
        print(line.strip())
    infile.close() 

import json 

name_dict={
    1: 'William', 
    2: 'Patrick', 
    3: 'Jon', 
    4: 'Tom', 
    5: 'Peter', 
    6: 'Colin', 
    7: 'Sylvester', 
    8: 'Paul', 
    9: 'Chris', 
    10: 'David',
    11: 'Matt', 
    12: 'Peter', 
    13: 'Jodie'
}

with open ('name.json', 'w') as outfile:
    json.dump(name_dict, outfile)

with open('name.json', 'r') as infile:
    restored_list = json.load(infile)