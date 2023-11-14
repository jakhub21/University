#pragma once
#include <string>
#include <iostream>
using namespace std;

class Pracownik{
    string imie;
    string nazwisko;
    const string pesel;
    int rocznik;
    string zawod;
public:
    Pracownik():pesel{to_string(rand()%693246493+178923)}{}
    string get_imie() {return imie;}
    string get_nazwisko() {return nazwisko;}
    int get_rocznik() {return rocznik;}
    string get_zawod() {return zawod;}
    string get_pesel() {return pesel;}
    
    void set_imie(string _imie){imie = _imie;}
    void set_nazwisko(string _nazwisko){nazwisko = _nazwisko;}
    void set_rocznik(int _rocznik){rocznik = _rocznik;}
    void set_zawod(string _zawod){zawod = _zawod;}
};

class Stocznia{
    const string Nip;
    string nazwaStoczni;
    string kraj;
    string adres;
    int numerAdres;
    int rokZalozenia;
public:
    Stocznia():Nip{to_string(rand()%100000+178923)}{}
    string get_nazwaStoczni() {return nazwaStoczni;}
    string get_kraj() {return kraj;}
    string get_adres() {return adres;}
    int get_numerAdres() {return numerAdres;}
    int get_rokZalozenia() {return rokZalozenia;}
    string get_Nip() {return Nip;}
    
    void set_nazwaStoczni(string _nazwaStoczni){nazwaStoczni = _nazwaStoczni;}
    void set_kraj(string _kraj){kraj = _kraj;}
    void set_adres(string _adres){adres = _adres;}
    void set_numerAdres(int _numerAdres){numerAdres = _numerAdres;}
    void set_rokZalozenia(int _rokZalozenia){rokZalozenia = _rokZalozenia;}
};
//tworzenie
void stworz(Pracownik*& pracownik);
void stworz(Stocznia**& stocznia);
void stworz(Pracownik*& pracownik, const size_t size);
void stworz(Stocznia**& stocznia, const size_t size);

//usuwanie
void usun(Pracownik*& pracownik);
void usun(Stocznia**& stocznia);
void usun(Pracownik*& pracownik, const size_t size);
void usun(Stocznia**& stocznia, size_t& size);
void usun(Pracownik*& pracownik, size_t& size, int index);
void usun(Stocznia**& stocznia, size_t& size, int index);

//wpisywanie
void wpisz(Pracownik* pracownik);
void wpisz(Pracownik*& pracownik, size_t& size);
void wpisz(Stocznia**& stocznia, size_t& size);

//wprowadzanie
void wprowadz(Pracownik* pracownik, size_t size);
void wprowadz(Stocznia** stocznia, size_t size);

//wypisywanie
void print(Pracownik* pracownik);
void print(Pracownik* pracownik, const size_t size);
void print(Stocznia** stocznia, const size_t size);

//wiek
void WiekPracownikow(Pracownik* pracownik, size_t size);
void WiekStoczni(Stocznia** stocznia, size_t size);

void menu();

