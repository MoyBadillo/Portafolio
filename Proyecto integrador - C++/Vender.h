#include <iostream>
using namespace std;

class Vender{
    private:
        string product;
        float precio;
        int cate;
    public:
        Vender();
        Vender(string product, float precio,int cate);
        void setProduct(string product);
        string getProduct();
        void setPrecio(float precio);
        float getPrecio();
        void setCate(int cate);
        int getCate();
};

Vender::Vender(){
    product = "Sin producto";
    precio = 0;
    cate = 1;
}

Vender::Vender(string product,float precio, int cate){
    this->product=product;
    this->precio=precio;
    this->cate=cate;
}

void Vender::setProduct(string product){
    this->product=product;
}

string Vender::getProduct(){
    return product;
}


void Vender::setPrecio(float precio){
    this->precio=precio;
}

float Vender::getPrecio(){
    return precio;
}

void Vender::setCate(int cate){
    this->cate=cate;
}

int Vender::getCate(){
    return cate;
}



