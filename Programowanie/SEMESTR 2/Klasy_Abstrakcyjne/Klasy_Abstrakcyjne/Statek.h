#pragma once
#include <string>
#include <iostream>
using namespace std;

class Statek{
    int numerStatku{0};
    int wypornosc{0};
    int zaloga{0};
    int ladownosc{0};
    int trasa{0};
public:
    Statek(){}
    virtual~Statek(){}
    virtual void droga()=0;
    void set_numerStatku(int _numerStatku){numerStatku = _numerStatku;}
    void set_wypornosc(int _wypornosc){wypornosc = _wypornosc;}
    void set_zaloga(int _zaloga){zaloga = _zaloga;}
    void set_ladownosc(int _ladownosc){ladownosc = _ladownosc;}
    void set_trasa(int _trasa){trasa = _trasa;}

    int get_numerStatku(){return numerStatku;}
    int get_wypornosc(){return wypornosc;}
    int get_zaloga(){return zaloga;}
    int get_ladownosc(){return ladownosc;}
    int get_trasa(){return trasa;}
    
};
class Wycieczkowiec:public Statek{
public:
    virtual void droga(){
        set_trasa((get_ladownosc()+get_zaloga())*5);
        cout<<get_trasa()<<"km"<<endl;
    };
    
};
class Transportowiec:public Statek{
public:
    virtual void droga(){
        set_ladownosc((get_trasa()+get_zaloga())*8);
        cout<<get_ladownosc()<<"kg"<<endl;

    };
    
};
void stworz(Statek**& statek);
void stworz(Statek**& statek, const size_t size);
//void usun(Statek**& statek);
void usun(Statek**& statek, size_t& size);
void usun(Statek**& statek, size_t& size, int index);
void wpisz(Statek**& statek, size_t& size);
void wprowadz(Statek** statek, size_t size);
void print(Statek** statek, const size_t size);
void WiekStoczni(Statek** statek, size_t size);
