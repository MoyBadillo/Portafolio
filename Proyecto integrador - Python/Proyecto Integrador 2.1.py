# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 12:35:15 2021

@author: samud
"""
import matplotlib.pyplot as plt
import numpy as np
import csv

matriz = []


with open ('Base.csv',newline="") as csvfile:
   variable_csv = csv.reader(csvfile, delimiter=',', quotechar='|')
   for row in variable_csv:
        matriz.append(row)
        


    

        
        
def ubicacion():
    contp = 0
    cont2 = 0
    cont3 = 0
    cont4 = 0
    cont5 = 0
    filtrado= []
    print("¿En que ciiudad desea filtrar la informacion?")
    print("Veracruz, Coatzacoalcos, Minatitlan o Xalapa")
    ciu = input()
    ciu = ciu.title()
    for a in range (0,len(matriz)):
        if ciudad[a] == ciu:
            fila = [referencia[a],tipo[a],operacion[a],ciudad[a],superficie[a],precio_venta[a],precio_renta[a],estatus[a],apellido[a]]
            filtrado.append(fila)
            contp += 1
            print (fila)
            print (contp)
        if ciudad[a] == 'Coatzacoalcos':
            cont2 += 1
        if ciudad[a] == 'Veracruz':
            cont3 += 1   
        if ciudad[a] == 'Minatitlan':
            cont4 += 1
        if ciudad[a] == 'Xalapa':
            cont5 += 1
    x= ['Coatzacoalcos', 'Veracruz', 'Minatitlan', 'Xalapa']
    y= [cont2, cont3, cont4, cont5]
    plt.plot(x,y)
    plt.show()
    porcent2 = cont2/100
    print('En Coatzacoalcos= ', porcent2, 'por ciento')
    porcent3 = cont3/100
    print('En Veracruz= ', porcent3, 'por ciento')
    porcent4 = cont4/100
    print('En Minatitlan= ', porcent4, 'por ciento')
    porcent5 = cont5/100
    print('En Xalapa= ', porcent5, 'por ciento')
    return filtrado

def oper():
    contventa = 0
    contrenta = 0
    cont = 0
    filtrado= []
    print("¿Que tipo de operacion desea filtrar?")
    print("Renta o Venta")
    ope = input()
    ope = ope.title()
    for a in range (0,len(matriz)):
        if operacion[a] == ope:
            fila = [referencia[a],tipo[a],operacion[a],ciudad[a],superficie[a],precio_venta[a],precio_renta[a],estatus[a],apellido[a]]
            filtrado.append(fila)
            cont += 1
            print (fila)
            print (cont)
        if operacion[a] == 'Rentado':
            cont += 1
        if operacion[a] == 'Venta':
            cont += 1
    x= ['Venta', 'Renta']
    y = [contventa, contrenta]
    plt.plot(x,y)

    return filtrado
                               
def est():
    cont=0
    cont1=0
    cont2=0
    cont3=0
    cont4=0
    filtrado= []
    print("¿En que estatus de propiedad desea filtrar la informacion?")
    print("En Venta, En Renta, Rentado o Vendido")
    es = input()
    es = es.title()
    for a in range (0,len(matriz)):
        if estatus[a] == 'En Renta':
            cont1 += 1
        if estatus[a] == 'En Venta':
            cont2 += 1
        if estatus[a] == 'Rentado':
            cont3 += 1 
        if estatus[a] == 'Vendido':
            cont4 +=1
        if estatus[a] == es:
            fila = [referencia[a],tipo[a],operacion[a],ciudad[a],superficie[a],precio_venta[a],precio_renta[a],estatus[a],apellido[a]]
            filtrado.append(fila)
            cont += 1
            print (fila)
            print(cont)
            
    porcent1 = cont1/100
    print('En renta= ', porcent1, 'por ciento')
    porcent2 = cont2/100
    print('En venta= ', porcent2, 'por ciento')
    porcent3 = cont3/100
    print('rentado= ', porcent3, 'por ciento')
    porcent4 = cont4/100
    print('vendido= ', porcent4, 'por ciento')
     
    return filtrado
    
def medidas():
    cont= 0
    cont1= 0
    cont2= 0
    cont3= 0
    filtrado= []
    max1 = 1
    print("Seleccione el rango de superficie ")
 
    min1 = float(input("Rango minimo de metros cuadrados:"))
    max1 = float(input('Rango maximo de metros cuadrados: '))
    
    for a in range(0, len(matriz)):
        superficie[a] = float(superficie[a])
        if superficie[a] in 'NA': break
        if float(superficie[a]>=min1 and superficie[a]<max1):
            fila = [referencia[a],tipo[a],operacion[a],ciudad[a],superficie[a],precio_venta[a],precio_renta[a],estatus[a],apellido[a]]
            filtrado.append(fila)
            print(fila)
        if superficie[a]>= 40 and superficie[a]<100:
            cont1 +=1
        if superficie[a]>= 100 and superficie[a]<200:
            cont2 +=1
        if superficie[a]>= 200 and superficie[a]<300:
            cont3 +=1
    x= [40,100,200,300]
    y= [cont,cont1,cont2,cont3]
    plt.plot(x,y)
    plt.show()

    return filtrado
                    
def vend():
    cont = 0
    cont1 = 0
    cont2=0
    cont3 = 0
    cont4 = 0
    cont5 = 0
    cont6 =0
    filtrado= []
    print("¿En que propietario desea filtrar la informacion?")
    print("Badillo, Lane, Ochoa, Pascal, Phoenix o Sandiego")
    v = input()
    v = v.title()
    for a in range (0,len(matriz)):
        if apellido[a] == v:
            fila = [referencia[a],tipo[a],operacion[a],ciudad[a],superficie[a],precio_venta[a],precio_renta[a],estatus[a],apellido[a]]
            filtrado.append(fila)
            print (fila)
            cont += 1
        if apellido[a] == 'Badillo':
            cont1 += 1
        if apellido[a] == 'Lane':
            cont2 += 1
        if apellido[a] == 'Ochoa':
            cont3 += 1
        if apellido[a] == 'Pascal':
            cont4 += 1
        if apellido[a] == 'Phoenix':
            cont5 += 1
        if apellido[a] == 'Sandiego':
            cont6 += 1
    x= ['Badillo', 'Lane', 'Ochoa', 'Pascal', 'Phoenix', 'Sandiego']
    y= (cont1, cont2, cont3, cont4, cont5, cont6)
    plt.plot(x,y)
    plt.show()
    return filtrado
                         
def precio():
    cont = 0
    cont1 = 0
    cont2 = 0
    cont3 =0
    cont4 =0
    suma=0
    filtrado= []
    print ("Que precios desea filtrar")
    x = input("Venta o Renta: ")
    # x = x.upper()
    mn = float(input("Rango minimo: "))
    print('de preferencia, valores mayores a un millon ochocientos en ventas, en rentas 3000')
    mx = float(input("Rango maximo: "))
    print('de preferencia valores maximos a 20000 en rentas')
    if x == "Venta":
        variable = precio_venta
    elif x == 'Renta':
        variable = precio_renta
    else: 
        print('error')
    print("Referencia, Tipo, Operacion, Ubicacion, Superficie, Precio, Estatus, Vendedor")
    for a in range (1,len(matriz)):
        if float(variable[a])>mn and float(variable[a])<=mx:
            fila = [referencia[a],tipo[a],operacion[a],ciudad[a],superficie[a],precio_venta[a],precio_renta[a],estatus[a],apellido[a]]
            filtrado.append(fila)
            cont += 1
            print (fila)
            print(cont)
            suma += a
    promedio = suma/100
    print('el porcentaje del rango es:', promedio)
    if x == "Venta":
        if float(variable[a])>2000000 and float(variable[a])<=2250000:
            cont1 += 1
        if float(variable[a])>2250000 and float(variable[a])<=2750000:
            cont2 += 1
        if float(variable[a])>1750000 and float(variable[a])<=2000000:
            cont3 += 1
        if float(variable[a])<=1000000:
            cont4 += 1
    else:
        if float(variable[a])>1000 and float(variable[a])<=3000:
            cont1 += 1
        if float(variable[a])>3000 and float(variable[a])<=6000:
            cont2 += 1
        if float(variable[a])>6000:
            cont3 += 1
        if float(variable[a])<=1000:
            cont4 += 1   
    x1= [0,1000,3000,6000]
    y1= [cont1,cont2,cont3,cont4] 
    plt.plot(x1,y1)
    plt.show()       
    
    x= [1000000,1250000,1750000,2000000]
    y= [cont1,cont2,cont3,cont4]
    plt.plot(x,y)
    plt.show()

    return filtrado
                   

def total():
    for a in range (0,len(matriz)):
        todo =f"{referencia[a]}, {tipo[a]}, {operacion[a]}, {ciudad[a]}, {superficie[a]}, {precio_venta[a]}, {precio_renta[a]}, {estatus[a]}, {apellido[a]}"
        print(todo)
        
                    

print ("Como desea filtrar la información de las propiedades")
fin = "SI"
while fin == "SI":
    referencia = []
    tipo = []
    operacion= []
    ciudad= []
    superficie=[]
    precio_venta=[]
    precio_renta=[]
    estatus=[]
    apellido =[]
    for renglon in matriz:
        referencia.append(renglon[0])
        tipo.append(renglon[1])
        operacion.append(renglon[2])
        ciudad.append(renglon[3])
        superficie.append(renglon[4])
        precio_venta.append(renglon[5])
        precio_renta.append(renglon[6])
        estatus.append(renglon[7])
        apellido.append(renglon[8])

            
        
    print ("Ubicacion = 1")
    print ("Estatus = 3")
    print ("Propietario = 5")
    print ("Precio = 6")
    print ("Ver toda la base de datos = 0")
    des = int(input())

    if des == 1:
        matriz = ubicacion()
    elif des == 3:
        matriz = est()
    elif des == 5:
        matriz = vend()
    elif des == 6:
        matriz = precio()
    elif des == 0:
        matriz = total()
    else:
        print(matriz)
    print("¿Desea seguir filtrando?")
    fin = input("¿Si o No?: ").upper()

#Solo Dios y mi yo de ese entonces saben como se hizo este codigo. 
#Pero, al final se pudo. :))

