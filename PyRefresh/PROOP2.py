"""
Class inheritance
para heredar tienes que poner como argumento la clase de la que hereda

class device()
class printer(Device)
    super().__init__
    super se utiliza para llamar un metodo de una clase padre

"""

"""
Composition

hacer clases que utilizan otras clases, que no necesariamente debe de heredar

"""

"""
Type hinting

especificar de que tipo va a ser una variable o lo que te va a devolver una funcion
Se usa mas que nada para que te salga en errores que tipo de dato es el esperado
ex:
class book:
    types = ("hd","pb")

...
    @classmethod
    def hd(cls, name:str,page_weight:int) -> "book": #Se usa "" por que la clase aun se esta creando mientras corre esto
        ...
    @classmethod
    def pb(cls, name:str,page_weight:int) -> bookshelf: #aca como ya es una clase aparte, no se ocupa ""
        ...

"""

"""
Imports
__name__ : Te da el nombre del archivo que estas corriendo

relative imports: cuando importas del mismo folder en el mayor nivel

"""
"""
Error
para levantar un error usa raise para que te salga en la consola

tambien puedes usar try except

para hacer clases de errores los haces heredar de alguna clase mayor como valueerror etc
"""

"""
First class objects

funciones las puedes usar como una variable para cualquier otra funcion
"""

def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    return dividend / divisor

def calculate(*values, operator):
    return operator(*values)

result = calculate(20,4, operator=divide)

