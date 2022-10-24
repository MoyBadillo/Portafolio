#include <iostream>
#include "Vender.h"
#include "Productos.h"
#include "Categoria.h"
using namespace std;

// 3 clases completas con getters, setters, constructores y con composición: Ejemplo: Producto, Categoría y carrito de compras
//Diagrama de clase completo
//Arreglos vectores
//Calculo
//Menu principal
//Estilo

void venta(){
    string a,b,c;
    float h,i,j;

    cout<<"Ingrese el nombre del primer producto"<<endl;
    cin>>a;
    cout<<"Ingrese el precio del primer producto \n"<<endl;
    cin>>h;
    Vender producto1(a,h,1);
    cout<<"Ingrese el nombre del segundo producto"<<endl;
    cin>>b;
    cout<<"Ingrese el precio del segundo producto \n"<<endl;
    cin>>i;
    Vender producto2(b,i,1);
    cout<<"Ingrese el nombre del tercer producto"<<endl;
    cin>>c;
    cout<<"Ingrese el precio del tercer producto \n"<<endl;
    cin>>j;
    Vender producto3(c,j,1);
   float totalVendido=producto1.getPrecio()+producto2.getPrecio()+producto3.getPrecio();
   cout<<"!Muy bien!, vendiste un total de $"<<totalVendido<<" pesos"<<endl;
}

int main(){
    Productos n1("Xbox",12000,1);
    Productos n2("Play Station",15000,1);
    Productos n3("Iphone",29900,1);
    Productos n4("Samsung",16500,1);
    Productos n5("Airpods",6500,1);
    Productos n6("Camisa",700,2);
    Productos n7("Pantalon",375,2);
    Productos n8("Saco",2500,2);
    Productos n9("Calcetin",250,2);
    Productos n10("Short",400,2);
    Productos n11("Estufa",7000,3);
    Productos n12("Microondas",2500,3);
    Productos n13("Horno",9000,3);
    Productos n14("Refrigerador",12590,3);
    Productos n15("Licuadora",1200,3);
    Categoria c;
    c.totalProductos(n1,0);
    c.totalProductos(n2,1);
    c.totalProductos(n3,2);
    c.totalProductos(n4,3);
    c.totalProductos(n5,4);
    c.totalProductos(n6,5);
    c.totalProductos(n7,6);
    c.totalProductos(n8,7);
    c.totalProductos(n9,8);
    c.totalProductos(n10,9);
    c.totalProductos(n11,10);
    c.totalProductos(n12,11);
    c.totalProductos(n13,12);
    c.totalProductos(n14,13);
    c.totalProductos(n15,14);
    

    int opcion;
    cout<<"Bienvenido a nuestra tienda online \n¿Que deseas ver?"<<endl; 
    cout<<"1.- Categoria \n2.- Mostrar todos los productos \n3.- Vender producto"<<endl;
    cin>>opcion;
    switch(opcion){
        case 1:
            cout<<"¿Que categoria deseas revisar? \n1.- Electronicos \n2.- Prendas \n3.- Electrodomesticos"<<endl;
            int d;
            cin>>d;
            c.cate(d);
            cout<<"\n"<<endl;
            break;
        case 2:
            c.total();
            break;
        case 3:
            cout<<"¿Que productos desea vender?"<<endl;
            venta();
            break;
    }
    return 0;
}
