# print (referencia[0])
# print (tipo[0])
# print (operacion[0])
# print (ciudad[0])
# print (superficie[0])
# print (precio_venta[0])
# print (precio_renta[0])
# print (estatus[0])
# print (apellido[0])
import csv

matriz = []


with open ('Base.csv',newline="") as csvfile:
   variable_csv = csv.reader(csvfile, delimiter=',', quotechar='|')
   for row in variable_csv:
        matriz.append(row)
        


    

        
        
def ubicacion():
    
    filtrado= []
    print("¿En que ciiudad desea filtrar la informacion?")
    print("Veracruz, Coatzacoalcos, Minatitlan o Xalapa")
    ciu = input()
    ciu = ciu.title()
    for a in range (0,len(matriz)):
        if ciudad[a] == ciu:
            fila = [referencia[a],tipo[a],operacion[a],ciudad[a],superficie[a],precio_venta[a],precio_renta[a],estatus[a],apellido[a]]
            filtrado.append(fila)
            print (fila)
    return filtrado
                    #Grafica de barras donde el eje x sea la ciudad filtrada y el eje y sean los precios de venta y renta 

def oper():
    filtrado= []
    print("¿Que tipo de operacion desea filtrar?")
    print("renta o venta")
    ope = input()
    ope = ope.title()
    for a in range (0,len(matriz)):
        if operacion[a] == ope:
            fila = [referencia[a],tipo[a],operacion[a],ciudad[a],superficie[a],precio_venta[a],precio_renta[a],estatus[a],apellido[a]]
            filtrado.append(fila)
            print (fila)
    return filtrado
                      #Grafica donde el eje x sea (venta o renta) y se compare con el precio de venta o renta         
def est():
    filtrado= []
    print("¿En que estatus de propiedad desea filtrar la informacion?")
    print("En Venta, En Renta, Rentado o Vendido")
    es = input()
    es = es.title()
    for a in range (0,len(matriz)):
        if estatus[a] == es:
            fila = [referencia[a],tipo[a],operacion[a],ciudad[a],superficie[a],precio_venta[a],precio_renta[a],estatus[a],apellido[a]]
            filtrado.append(fila)
            print (fila)
    return filtrado
                        #Grafica donde el eje x sea (En renta, en venta, vendido, rentado) y se compare con el precio de renta o venta         
def medidas():
    filtrado= []
    max = 1
    print("Seleccione el rango de superficie ")
 
    min = float(input("Rango minimo de metros cuadrados:"))
    while max < 40:
        max = float(input("Rango maximo de metros cuadrados:"))
        print ("El rango minimo es de 40 metros cuadrados")
        print("")
    for a in range (1,len(matriz)):
        if float(superficie[a])>min and float(superficie[a])<=max:
            fila = [referencia[a],tipo[a],operacion[a],ciudad[a],superficie[a],precio_venta[a],precio_renta[a],estatus[a],apellido[a]]
            filtrado.append(fila)
            print (fila)
    return filtrado
                    #Grafica que se muestren las medidas el eje x vendria siendo la referencia de 1 a ...
def vend():
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
    return filtrado
                          #Grafica donde se muestre la cantidad de propiedades que tiene esa persona    
def precio():
    filtrado= []
    print ("Que precios desea filtra")
    x = input("Venta o renta: ")
    x = x.upper()
    mn = float(input("Rango minimo: "))
    mx =float(input("Rango maximo: "))
    if x == "VENTA":
        variable = precio_venta
    else:
        variable = precio_renta
    print("Referencia, Tipo, Operacion, Ubicacion, Superficie, Precio, Estatus, Vendedor")
    for a in range (1,len(matriz)):
        if float(variable[a])>mn and float(variable[a])<=mx:
            fila = [referencia[a],tipo[a],operacion[a],ciudad[a],superficie[a],precio_venta[a],precio_renta[a],estatus[a],apellido[a]]
            filtrado.append(fila)
            print (fila)
    return filtrado
                    #Grafica donde se compare el precio de (venta o renta) el eje x vendria siendo las referencias del 1 al ...

def total():
    for a in range (0,len(matriz)):
        todo =f"{referencia[a]}, {tipo[a]}, {operacion[a]}, {ciudad[a]}, {superficie[a]}, {precio_venta[a]}, {precio_renta[a]}, {estatus[a]}, {apellido[a]}"
        print(todo)
                    #Grafica donde se compare el precio de venta y renta totales
                    #Grafica donde se compare cuantas propiedades tiene cada vendedor
                    #Grafica del estatus cuantas propiedades estan en renta, en venta, vendidas y rentadas


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
    print ("Operacion = 2")
    print ("Estatus = 3")
    print ("Medida de la superficie = 4")
    print ("Propietario = 5")
    print ("Precio = 6")
    print ("Ver toda la base de datos = 0")
    des = int(input())

    if des == 1:
        matriz = ubicacion()
    elif des == 2:
        matriz = oper()
    elif des == 3:
        matriz = est()
    elif des == 4:
        matriz = medidas()
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


