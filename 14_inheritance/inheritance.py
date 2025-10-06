class Student:
    def __init__(self, name, student_id, major):
        self.__name = name
        self.__student_id = student_id
        self.__major = major

    def __str__(self):
        return f"Name: {self.__name}, ID: {self.__student_id}, {self.__major}"

# child class inherits parent
class UndergraduateStudent(Student):
    def __init__(self, name, student_id, major, year):
        # Student.__init__() # can call the base function if we know its name
        super().__init__(name, student_id, major) # call the method from the parent class regardless of its name
        self.__year = year
    
    def __str__(self):
        return super().__str__() + f", Year: {self.__year}"

    # Wouldn't work because child cannot access private variables of parent class. Move to Student to fix.
    # def getName(self):
    #     print(self.__name)

if __name__ == "__main__":
    student = Student("Will", "U1440", "Computer Science")
    print(student)
    ugrad = UndergraduateStudent("Mike", "U5443", "Computer Engineering", "Junior")
    print(ugrad)
    ugrad.getName()



class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

dog = Dog("Sumo", 7, "St. Bernard")
print(dog.name)
print(dog.age)
print(dog.breed)