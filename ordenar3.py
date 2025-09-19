"""
Inserta el encabezado aquí y escribe tu código abajo

Dados tres números, ordenarlos de mayor a menor.
    
    Args:
        a (float): Primer número real.
        b (Float): Segundo número real.
        c (float): Tercer número real.


    Returns:
        Tuple: lista de números ordenada del mayor al menor




"""

# Declaraciones
#CONSTANTE = valor
a=float(input("Primer número "))
b=float(input("Segundo número "))
c=float(input("Tercer número "))


# Entradas

a_str=str(a)
b_str=str(b)
c_str=str(c)

# Proceso

if (a==b and b==c) or(a>=b and b>=c):
    print(("Números ordenados: ")+(a_str)+(", ")+(b_str)+(", ")+(c_str))
elif (a<b and b<=c):
    print(("Números ordenados: ")+(c_str)+(", ")+(b_str)+(", ")+(a_str))

elif(b<a and a<=c):
    print(("Números ordenados: ")+(c_str)+(", ")+(a_str)+(", ")+(b_str))

elif(a>=c and c>b):
    print(("Números ordenados: ")+(a_str)+(", ")+(c_str)+(", ")+(b_str))
    
elif(b>=a and a>c):
    print(("Números ordenados: ")+(b_str)+(", ")+(a_str)+(", ")+(c_str))
    
elif(b>=c and c>a):
    print(("Números ordenados: ")+(b_str)+(", ")+(c_str)+(", ")+(a_str))



else:
        print("nada")



# Salidas
#print(salida)
