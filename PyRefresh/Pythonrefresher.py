#Python refresher

x = 15
#Primero se genera el quince y se le asigna el nombre de x 

print(x)
"""
que es una funcion: parte de codigo que realiza una accion o calcula un resultado

"""

name = "Bob"
greeting= f"hello, {name}"

print(greeting)

#template strings with .format()
name = "john"
greeting= "hello, {}"
with_name=greeting.format(name)
print(with_name)

#user input

name = input("Enter your name: ")
print(name)

size=input("your size: ")

sizebien = int(size)

eldoble = sizebien*2
print(eldoble)

"""
lists tuples and sets"
List and tuples maintain an order, sets dont have order
so it cant use subscript notation
"""

#List, modifiable
l=["bob","rolf","anne"]
#tuple, not modifiable
t=("bob","rolf","anne")
#set, no duplicates and modifiable
s={"bob","rolf","anne"}

#subscript notations
print(l[0])
print(t[1])

"""
List operations
.append()
.remove()
Set operations
.add()
.difference() - remueve elementos iguales entre 2 sets
.intersection() - opuesto a difference
.union() - une 2 sets

tuples dont have operations cause they are not modifiable
"""

#sets exercise
friends = {"john","lol","dan"}
abroad = {"lol","dan"}

local_friends=friends.difference(abroad)
print(local_friends)

friends = {"john","mike","dan"}
abroad = {"dustin","dan"}
total_friends=friends.union(abroad)
print(total_friends)

#Para hacer un tuple simple se tiene que hacer asi:

my_tuple=(15,) # o solo 15,
#por que si no lo detecta como una operacion