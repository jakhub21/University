#include <iostream>
#include <stdlib.h>
#import <locale>
#include <ctime>
#include "Klasa_h.h"
using namespace std;

//Opcje tworzenia
void stworz(Pracownik*& pracownik)
{
    pracownik = new Pracownik;
    
}

void stworz(Stocznia**& stocznia)
{
    stocznia = new Stocznia*;
    
}

void stworz(Pracownik*& pracownik, const size_t size)
{
    pracownik = new Pracownik[size];
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
void usun(Pracownik*& pracownik,const size_t size)
{
    if(pracownik!=0)
    {
        delete [] pracownik;
        pracownik = NULL;
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

void usun(Pracownik*& pracownik, size_t& size, int index) {
    if (index < size) {
        Pracownik* temp = new Pracownik[size - 1];
        short int j{ -1 };
        for (int i = 0; i < size; ++i)
            if (i != index) {
                ++j;
                temp[j].set_imie(pracownik[i].get_imie());
                temp[j].set_nazwisko(pracownik[i].get_nazwisko());
                temp[j].set_rocznik(pracownik[i].get_rocznik());
                temp[j].set_zawod(pracownik[i].get_zawod());
            }
        delete[] pracownik;
        pracownik = temp;
        --size;
    }
    else
        cout <<"Index nieprawidłowy" << endl;
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
void wpisz(Pracownik* pracownik)
{
    int tempi;
    string temps;
    cout<<"Imie:"<<endl;
    cin>>temps;
    pracownik->set_imie(temps);
    cout<<"Nazwisko:"<<endl;
    cin>>temps;
    pracownik->set_nazwisko(temps);
    cout<<"Rocznik:"<<endl;
    cin>>tempi;
    pracownik->set_rocznik(tempi);
    cout<<"Zawód:"<<endl;
    cin>>temps;
    pracownik->set_zawod(temps);
}

void wpisz(Pracownik*& pracownik,size_t &size)
{
    int tempi;
    string temps;
    Pracownik* temp = new Pracownik[size + 1];
        if (size == 0) {
            temp = new Pracownik;
        }
        else {
            for (int i = 0; i < size; ++i){
                temp[i].set_imie(pracownik[i].get_imie());
                temp[i].set_nazwisko(pracownik[i].get_nazwisko());
                temp[i].set_rocznik(pracownik[i].get_rocznik());
                temp[i].set_zawod(pracownik[i].get_zawod());
            }
            delete[] pracownik;
        }
    pracownik = temp;
    cout<<"Imie:"<<endl;
    cin>>temps;
    pracownik[size].set_imie(temps);
    cout<<"Nazwisko:"<<endl;
    cin>>temps;
    pracownik[size].set_nazwisko(temps);
    cout<<"Rocznik:"<<endl;
    cin>>tempi;
    pracownik[size].set_rocznik(tempi);
    cout<<"Zawód:"<<endl;
    cin>>temps;
    pracownik[size].set_zawod(temps);
    size++;
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
void wprowadz(Pracownik* pracownik, size_t size)
{
    for (int i = 0; i < size; i++)
    {
        pracownik[i].set_imie("Hubert");
        pracownik[i].set_nazwisko("Jakubiak");
        pracownik[i].set_rocznik(rand() % 120 + 1900);
        pracownik[i].set_zawod("Pyper");
        
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

void print(Pracownik* pracownicy) {
    if(pracownicy!=0){
        cout << "Pracownicy:" << endl;
        cout << pracownicy->get_imie() << "\t" << pracownicy->get_nazwisko()<< "\t" << pracownicy->get_rocznik()<< "\t" << pracownicy->get_zawod()<<"\t"<<pracownicy->get_pesel()<< endl;
    }else
    {
        cout<<"Tablica jest pusta"<<endl;
    }
    }

void print(Pracownik* pracownicy,const size_t rozmiar) {
    if(pracownicy!=0){
        cout << "Pracownicy:" << endl;
        for (int i = 0; i < rozmiar; i++) {
            cout << pracownicy[i].get_imie() << "\t" << pracownicy[i].get_nazwisko()<< "\t" << pracownicy[i].get_rocznik()<< "\t" << pracownicy[i].get_zawod()<<"\t"<<pracownicy[i].get_pesel()<< endl;
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
            cout<<stocznia[i]->get_nazwaStoczni()<<"\t"<<stocznia[i]->get_kraj()<<"\t"<<stocznia[i]->get_adres()<<"\t"<<stocznia[i]->get_numerAdres()<<"\t"<<stocznia[i]->get_rokZalozenia()<<"\t"<<stocznia[i]->get_Nip()<<endl;
        }
    }else
    {
        cout<<"Tablica jest pusta"<<endl;
    }
}

//Wiek Pracownikow

void WiekPracownikow(Pracownik* pracownik, size_t size)
{
    time_t current_time;
    current_time = time(NULL);
    int rok = 1970 + current_time / 31537970;
    for(int i=0;i<size;i++){
    cout << pracownik[i].get_imie() << "\t" << pracownik[i].get_nazwisko()<< "\t" << rok-pracownik[i].get_rocznik()<< "\t" <<   pracownik[i].get_zawod() << endl;
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
