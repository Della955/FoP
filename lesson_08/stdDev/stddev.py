class Person: 

    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    def get_age(self):
        return self._age 


def std_dev(person_list):
    age_list = [] 
    get_mean = 0
    
    for person in person_list:
        age_list.append(person.get_age())
        get_mean += person.get_age()

    get_mean = get_mean // len(person_list)

    std_calc = 0 
    for age_calc in person_list:
        std_calc += (age_calc.get_age() - get_mean)**2
    
    std_calc = (std_calc / len(person_list)) ** 0.5
   
    return std_calc
    

p1 = Person("Kyoungmin", 73)
p2 = Person("Mercedes", 24)
p3 = Person("Beatrice", 48)
person_list = [p1, p2, p3]

answer = std_dev(person_list)
print(answer)