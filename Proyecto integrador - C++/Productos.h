#include <iostream>
using namespace std;


class Productos{
    private:
        string nombre;
        float costo;
        int cat; 
    public: 
        Productos();
        Productos(string nombre, float costo, int cat);
        void setNombre(string nombre);
        void setCosto(float costo);
        void setCat(int cat);
        string getNombre();
        float getCosto();
        int getCat();
};
Productos::Productos(){
    nombre="Sin nombre";
    costo=0;
    cat=1;
}

Productos::Productos(string nombre, float costo, int cat){
    this->nombre=nombre;
    this->costo=costo;
    this->cat=cat;
}

void Productos::setNombre(string nombre){
    this->nombre=nombre;
}

void Productos::setCosto(float costo){
   this->costo=costo; 
}

void Productos::setCat(int cat){
    this->cat=cat;
}

string Productos::getNombre(){
    return nombre;
}

float Productos::getCosto(){
    return costo;
}

int Productos::getCat(){
    return cat;
}