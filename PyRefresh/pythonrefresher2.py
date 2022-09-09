#Is Checa dos elementos si son exactamente iguales, que ocupan el mismo espacio en memoria

# In keyword to check if an element is inside a list, tuple or set

#list comprehensions, create lists from lists
numbers=[1,2,5]
doubled=[num*2 for num in numbers]

#is checa si son tal cual lo mismo

#Dictionaries another structure loke lists, etc., but it uses keys and values
#Es como los sets pero tienen una key y un valor
friends = {"rolf":4,"john":9}

friends["rolf"]=20

'''
Los tuples pueden ser () o sin ()
x= 5, 6
x=(5,6)

Destructuracion es separar algun elemento en varios
ejemplo:
x= 5,6 ---- es un tuple
y,z= x --- esto lo separa el tuple y lo convierte en dos variables
'''

#Cuando usas "_" como nombre para una variable, se lee como una variable que en realidad no importa, segun la comunidad


# "*" se usa para recolectar valores que pueda hasta o los que quedan"
head, *tail = [1,2,3,4,5]
print(head)
print(tail)

*head, tail = [1,2,3,4,5]
print(head)
print(tail)

'''
en una funcion si pones una variable que aun no existe
no pasa nada por que esa linea de codigo no corre hasta 
que se llama a la funcion
ex:
'''
def add_friend():
    friends.append("rolf") 
   
friends=[]
add_friend()

print(friends)

'''
en una funcion desde el espacio de parametros puedes asignar en el orden que uno quiere
ex:
def say_hello(name, surname):
    ...

say_hello(surname=johnson,name=john)
se le llama keyword arguments, y si usas tienes que usar para todos los argumentos a menos que los que le sigan tambien sean keyword parameters
'''

'''
default_y=3

def add(x,y=default_y):
    sum=x+y
    ...
add(2)
default_y=4
add(2)

en el segundo default no va a cambiar el valor de Y por que ya se le dio un valor

'''