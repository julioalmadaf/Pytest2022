class Student:
    #Todas las clases deben de tener un self(o como quieras que se llame)
    # Se le llama method cuando esta dentro de una clase
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    
    def average(self):
        return sum(self.grades)/len(self.grades)

#Objeto creado
student = Student("bob", (100,90,89,99,92,78))
print(student.name)
print(student.average())


##magic methods
#cuando usan __lago__

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person{self.name}, {self.age} years old"

    def __repr__(self):
        return f"<Person('{self.name}', {self.age})>"

bob = Person("Bob", 35)


#CLASS METHODS and static methods

#Instance method necesitan el objeto(Lo que creas a partir de una clase) para ser utilizado
#class method que usa a la misma clase como un parametro
#staticmethod un metodo que no usa nada

class Classtest:
    def instance_method(self):
        print(f"Called instance method of {self}")
    
    @classmethod
    def class_method(cls):
        print(f"Called class method of {cls}")

    @staticmethod
    def static_method():
        print("called static_method")
