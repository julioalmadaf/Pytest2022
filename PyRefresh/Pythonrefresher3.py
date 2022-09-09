#return es como un break 
#

#lambda functions: para funciones simples
#como una suma, pueden no tener un nombre, por que son usualmente una linea simple de codigo, nada mas

add = lambda x,y: x+y

print(add(5,7))

#map function returna a map object of the results
#after applyinh the given function to each item of an iterable object(list, etc.)
#syntax: map(fun,iter)

#EJERCICIO
#Dictionary comprehension
#igual que list comprehension pero con keys

# Create a variable called student, with a dictionary.
# The dictionary must contain three keys: 'name', 'school', and 'grades'.
# The values for each must be 'Jose', 'Computing', and a tuple with the values 66, 77, and 88.
student = {
    "name":"Jose",
    "school":"Computing",
    "grades":(66,77,88)
}

# Assume the argument, data, is a dictionary.
# Modify the grades variable so it accesses the 'grades' key of the data dictionary.
def average_grade(data):
    grades =  data["grades"]
    return sum(grades) / len(grades)


# Implement the function below
# Given a list of students (a list of dictionaries), calculate the average grade received on an exam, for the entire class
# You must add all the grades of all the students together
# You must also count how many grades there are in total in the entire list
def average_grade_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
        # Implement here
        total+=sum(student["grades"])
        count+=len(student["grades"])
    return total / count


'''
UNPACKING ARGUMENTS

el simbolo de * reune multiples argumentos en una sola variable(que es un tuple) cuando llamas a una funcion
puede igual usarse solo para un elemento tambien

se puede utilizar el asterisco para desestrucutrar argumentos en multiples parametros cuando se usa en una funcion

** se usa para diccionarios, que pasa argumentos con nombre 
'''

def multiply(*args):
    print(args)


'''
UNPACKING KEYWORDS ARGUMENT

**kwargs
 collects keyword arguments and put into a dictionary
'''
def named(**kwargs):
    print(kwargs)

named(name="bobo",age=25)


def named(name, age):
    print(name, age)

details = {"name": "bob", "age":25 }

named(**details)
