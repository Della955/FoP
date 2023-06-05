import statistics

class Student():
    def __init__(self, name, grade):
        self._name = name 
        self._grade = grade 

    def get_grade(self):
        return self._grade 



def basic_stats(student_object_list):
    li_stats = [] 
    for elem in student_object_list:
        li_stats.append(elem.get_grade())
    
    return (statistics.mean(li_stats), statistics.median(li_stats), statistics.mode(li_stats))

s1 = Student("Kyoungmin", 73)
s2 = Student("Mercedes", 74)
s3 = Student("Avanika", 78)
s4 = Student("Marta", 74)

student_list = [s1, s2, s3, s4]
print(basic_stats(student_list))