############################################################################################################

# Write 5 functions that perform the following tasks:

# 1. The function generate_student_dictionary(student_list) creates a dictionary of students
#    from a given list, initializing each student with a grade of 0.
#    Execute this function with a specific list of students and display the resulting dictionary.

# 2. The function register_grade(student_dict, student, grade) registers a grade for a specific
#    student in the dictionary. Execute this function to assign grades to students.

# 3. The function calculate_average_grade(student_dict) calculates the average grade
#    of all students. Execute this function and display the resulting average.

# 4. The function find_students_above_threshold(student_dict, threshold) finds all students
#    with a grade above a specific threshold. Execute this function and display the resulting set of students.

# 5. The function count_students_per_grade(student_dict) counts how many students
#    received each grade and returns a dictionary with the count per grade.


############################################################################################################


class Ex2Git():

    def __init__(self):
        self.student_list = ["Martinelli", "Saka", "Barella", "Lukaku", "Messi", "Ronaldo"]
        self.diz_student = {}
    
    def check_string_list(self):
        return all(isinstance(item, str) for item in self.student_list)
    
    def getDizStudente(self):
        return self.diz_student
    
    #make_dict_student: create dictionary from a list of a string
    def make_dict_student(self):

        if self.check_string_list():
            for student in self.student_list:
                self.diz_student[student] = 0
            
            return self.diz_student
        
        else:
            print("I cannot proceed with the creation of the dictionary, since the list elements are not all strings!")
        
    #register_vote: given a student and one of his or her grades I record it within the specific key
    def register_vote(self, name_student, grade_student):
        #Important: In this case I apply the Italian grade where schools are given a grade ranging from 1 to 10 (1 lowest and 10 highest)

        if grade_student > 0 and grade_student <= 10 and (name_student in self.student_list) :
                self.diz_student[name_student] = grade_student
                print(f"I updated the student's grade {name_student} to {grade_student}")
        else:
              print(
                    "I am sorry but I cannot continue. "
                    "The name or grade you entered does not meet the conditions! "
                    "Please enter a number from 1 to 10, and a student who is within our school!"
                )
              
    #average_grade: calculates grade point average of all students' grades
    def average_grade(self):
        
        sum_grade = 0
        for value_grade in self.getDizStudente().values():
            sum_grade += value_grade
        
        nAverage = format(sum_grade / len(self.getDizStudente()), ".2f")
        print(f"The total grade point average of all students, taking into account the grades of each boy is {nAverage}")
    
    #find_students_with_vote: method for finding students who have a grade higher than specified
    def find_students_with_vote(self, vote_to_find):
        lista_s = []

        if vote_to_find > 0 and vote_to_find <= 10:
            for nStudent, gStudente in self.getDizStudente().items(): 
                if gStudente > vote_to_find:
                    lista_s.append(nStudent)
            
            print(f"The number of people with a grade greater than {vote_to_find} is equal to {len(lista_s)}. Specifically, the students are as follows: {', ' .join(lista_s)}")
        else:
            print("The grade you entered is invalid, sorry but I cannot continue!")
    
    #student_count: counts the number of students for each grade and reports the student count for each grade in the dictionary.
    def student_count(self):
        diz_count = {}

        for name, grade in self.getDizStudente().items():

            if grade not in diz_count:
                diz_count[grade] = []
                diz_count[grade].append(name)
            else:
                diz_count[grade].append(name)
        
        for gradeStudente, list_studente in sorted(diz_count.items()):
            print(f"For the grade {gradeStudente} the number of the student(s) is {len(list_studente)}, specifically the name of the student(s) is {', '.join(list_studente)}")
        

def main():
    ex_2_obj = Ex2Git()
    print("-" * 45)

    print("Welcome to my program, i hope you enjoy and have a great day!")

    print("-" * 45)

    print("The dictionary just created with the students in the class is as follows!")
    print(ex_2_obj.make_dict_student())

    print("-" * 45)
    print("I update my students' grades!")

    ex_2_obj.register_vote("Barella", 6)
    ex_2_obj.register_vote("Saka", 6)
    ex_2_obj.register_vote("Martinelli", 7)
    ex_2_obj.register_vote("Lukaku", 8)
    ex_2_obj.register_vote("Messi", 8)
    ex_2_obj.register_vote("Ronaldo", 10)

    print("-" * 45)
    print("This is a printout of the dictionary populated with grades for each student!")
    print(ex_2_obj.getDizStudente())

    print("-" * 45)

    ex_2_obj.average_grade()

    print("-" * 45)

    ex_2_obj.find_students_with_vote(4)

    print("-" * 45)
    
    print("Let's go and see how many students have the same and more importantly who these students are!")
    ex_2_obj.student_count()

    print("-" * 45)

    
if __name__ == "__main__":
    main()

