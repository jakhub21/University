#include <iostream>
#include <stdlib.h>
#import <locale>
#include <ctime>
#include "Stocznia.h"
using namespace std;

//Opcje tworzenia
void stworz(Stocznia**& stocznia)
{
    stocznia = new Stocznia*;
    
}
void Stocznia::stworz(Pracownik**& pracownicy,size_t size)
{
    pracownicy = new Pracownik*[size];
    for (int i = 0; i < size; i++)
    {
        pracownicy[i] = new Pracownik;
    }
}
void stworz(Stocznia**& stocznia, const size_t size)
{
    stocznia = new Stocznia*[size];
    for (int i = 0; i < size; i++)
    {
        stocznia[i] = new Stocznia;
    }
}

//Opcje usuwania
void Stocznia::usun(Pracownik**& pracownicy,size_t size)
{
    if(pracownicy!=nullptr)
    {
        for(int i = 0;i<size;i++)
            delete pracownicy[i];
        delete [] pracownicy;
        pracownicy = nullptr;
            
    }else
    {
        cout<<"Tablica jest pusta"<<endl;
    }
}
void usun(Stocznia**& stocznia,size_t& size)
{
    if(stocznia!=0){
        for(int i=0;i < size;i++)
            delete stocznia[i];
        delete [] stocznia;
        stocznia = NULL;
        size = 0;
    }else
    {
        cout<<"Tablica jest pusta"<<endl;
    }
}

void Stocznia::usun(int index) {
    for(int i =0;i<pracownicy_size;i++){
        if(i == index){
            auto temp = new Pracownik*[pracownicy_size+1];
            copy(pracownicy,pracownicy+i,temp);
            copy(pracownicy+i+1,pracownicy+pracownicy_size,temp+i);
            delete[] pracownicy;
            pracownicy = temp;
            --pracownicy_size;
        }
    }
}

void usun(Stocznia**& stocznia, size_t& size, int index) {
    if (index < size) {
        Stocznia** temp = new Stocznia * [size - 1];
        short int j{ -1 };
        for (int i = 0; i < size; ++i)
            if (i != index) {
                ++j;
                temp[j] = stocznia[i];
            }
        delete[] stocznia;
        stocznia = temp;
        --size;
    }
    else
        cout <<"Index nieprawidłowy" << endl;
}


//Opcja wpisywania
void Stocznia::wpisz()
{
    int tempi;
    string temps;
    auto temp = new Pracownik*[pracownicy_size + 1];
        if (pracownicy_size == 0) {
            temp [pracownicy_size]= new Pracownik;
        }
        else {
            for (int i = 0; i < pracownicy_size; ++i){
                temp[i]=pracownicy[i];

            }
            temp[pracownicy_size]=new Pracownik;
            delete[] pracownicy;
        }
   pracownicy= temp;
    cout<<"Imie:"<<endl;
    cin>>temps;
    pracownicy[pracownicy_size]->set_imie(temps);
    cout<<"Nazwisko:"<<endl;
    cin>>temps;
    pracownicy[pracownicy_size]->set_nazwisko(temps);
    cout<<"Rocznik:"<<endl;
    cin>>tempi;
    pracownicy[pracownicy_size]->set_rocznik(tempi);
    cout<<"Zawód:"<<endl;
    cin>>temps;
    pracownicy[pracownicy_size]->set_zawod(temps);
    pracownicy_size++;
}

void wpisz(Stocznia**& stocznia, size_t& size) {
    int tempi;
    string temps;
    Stocznia** temp = new Stocznia * [size + 1];
    if (size == 0) {
        temp[size] = new Stocznia;
    }
    else {
        for (int i = 0; i < size; ++i)
            temp[i] = stocznia[i];
        temp[size] = new Stocznia;
        delete[] stocznia;
    }
    stocznia = temp;
    cout<<"Nazwa stoczni:"<<endl;
    cin>>temps;
    stocznia[size]->set_nazwaStoczni(temps);
    cout<<"Kraj:"<<endl;
    cin>>temps;
    stocznia[size]->set_kraj(temps);
    cout<<"Adres:"<<endl;
    cin>>temps;
    stocznia[size]->set_adres(temps);
    cout<<"Numer adres:"<<endl;
    cin>>tempi;
    stocznia[size]->set_numerAdres(tempi);
    cout<<"Rok zalozenia:"<<endl;
    cin>>tempi;
    stocznia[size]->set_rokZalozenia(tempi);
    size++;
}

//Inicjalizacja
void Stocznia::wprowadz()
{
    for (int i = 0; i < pracownicy_size; i++)
    {
        pracownicy[i]->set_imie("Hubert");
        pracownicy[i]->set_nazwisko("Jakubiak");
        pracownicy[i]->set_rocznik(rand() % 120 + 1900);
        pracownicy[i]->set_zawod("Pyper");
        
    }
}
void wprowadz(Stocznia** stocznia, size_t size)
{
    for (int i = 0; i < size; i++)
    {
        stocznia[i]->set_nazwaStoczni("Kleven");
        stocznia[i]->set_kraj("Norwegia");
        stocznia[i]->set_adres("Topolowa");
        stocznia[i]->set_numerAdres(rand() % 100 + 0);
        stocznia[i]->set_rokZalozenia(rand() % 100 + 1900);
        
    }
}

//Opcje wypisywania


void Stocznia::print() {
    if(pracownicy!=0){
        cout << "Pracownicy:" << endl;
        for (int i = 0; i < pracownicy_size; i++) {
            cout << pracownicy[i]->get_imie() << "\t" << pracownicy[i]->get_nazwisko()<< "\t" << pracownicy[i]->get_rocznik()<< "\t" << pracownicy[i]->get_zawod()<<"\t"<<pracownicy[i]->get_pesel()<< endl;
        }
    }else
    {
        cout<<"Tablica jest pusta"<<endl;
    }
}


void print(Stocznia** stocznia, const size_t rozmiar) {
    if(stocznia!=0){
        cout << "Stocznie:" << endl;
        for (int i = 0; i < rozmiar; i++) {
            cout<<*stocznia[i]<<endl;
            //cout<<stocznia[i]->get_nazwaStoczni()<<"\t"<<stocznia[i]->get_kraj()<<"\t"<<stocznia[i]->get_adres()<<"\t"<<stocznia[i]->get_numerAdres()<<"\t"<<stocznia[i]->get_rokZalozenia()<<"\t"<<stocznia[i]->get_Nip()<<endl;
        }
    }else
    {
        cout<<"Tablica jest pusta"<<endl;
    }
}

//Wiek Pracownikow

void Stocznia::WiekPracownikow()
{
    time_t current_time;
    current_time = time(NULL);
    int rok = 1970 + current_time / 31537970;
    for(int i=0;i<pracownicy_size;i++){
    cout << pracownicy[i]->get_imie() << "\t" << pracownicy[i]->get_nazwisko()<< "\t" << rok-pracownicy[i]->get_rocznik()<< "\t" <<   pracownicy[i]->get_zawod() << endl;
    }
}

void WiekStoczni(Stocznia** stocznia, size_t size)
{
    time_t current_time;
    current_time = time(NULL);
    int rok = 1970 + current_time / 31537970;
    for(int i=0;i<size;i++){
        cout<<stocznia[i]->get_nazwaStoczni()<<"\t"<<stocznia[i]->get_adres()<<"\t"<<rok - stocznia[i]->get_rokZalozenia()<<endl;
    }
}

Stocznia& Stocznia::operator=(Stocznia& stocznia){
    this->nazwaStoczni = stocznia.nazwaStoczni;
    this->kraj = stocznia.kraj;
    this->adres = stocznia.adres;
    this->numerAdres = stocznia.numerAdres;
    this->rokZalozenia = stocznia.rokZalozenia;
    this->pracownicy_size = stocznia.pracownicy_size;
    usun(pracownicy,stocznia.pracownicy_size);
    stworz(pracownicy,pracownicy_size);
    for(size_t i =0;i<pracownicy_size;i++){
        pracownicy[i]->set_imie(stocznia.pracownicy[i]->get_imie());
        pracownicy[i]->set_nazwisko(stocznia.pracownicy[i]->get_nazwisko());
        pracownicy[i]->set_rocznik(stocznia.pracownicy[i]->get_rocznik());
        pracownicy[i]->set_zawod(stocznia.pracownicy[i]->get_zawod());
    }
    return *this;
}

ostream& operator<<(ostream& out, const Stocznia& stocznia){
    out<< stocznia.nazwaStoczni <<endl<<stocznia.kraj<<endl<<stocznia.adres<<endl<<stocznia.numerAdres<<endl<<stocznia.rokZalozenia<<endl;
    return out;
}

Stocznia::Pracownik& Stocznia::operator[](int index){
    assert(0<=index && index <pracownicy_size);
    return *(pracownicy[index]);
}
