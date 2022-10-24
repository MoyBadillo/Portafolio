#include <iostream>
using namespace std;

class Categoria{
    private:
        Productos prod[15];
    public:
        void totalProductos(Productos produ,int pos);
        void cate(int x);
        void total();
};

void Categoria::totalProductos(Productos produ,int pos){
    prod[pos]=produ;
};

void Categoria::cate(int x){
    int cont=0;
    int suma=0;
    string y;
    if(x==1){
        y = "Electronicos";
    }
    else if(x==2){
        y = "Prendas";
    }
    else{
        y="Electrodomesticos";
    }
    cout<<y<<"\n"<<endl;
    for(int i=0; i<15; i++){
        if(prod[i].getCat()==x)
        {
            cout<<prod[i].getNombre()<<" ---> $"<<prod[i].getCosto()<<endl;
            cont = cont + 1;
            suma = suma + prod[i].getCosto();
        }
        
    }
    cout<<"\nLa categoria de "<<y<<" tiene un promedio de "<<suma/cont<<" por producto"<<endl;
}

void Categoria::total(){
    int suma = 0;
    for(int i=0;i<15;i++){
        cout<<i+1<<". "<<prod[i].getNombre()<<" ---> $"<<prod[i].getCosto()<<"\n"<<endl; 
        suma = suma + prod[i].getCosto();
    }
    cout<<"\nCon una suma total de: $"<<suma<<endl;
}



