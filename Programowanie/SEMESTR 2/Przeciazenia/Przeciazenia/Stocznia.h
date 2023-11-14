#pragma once
#include <string>
#include <iostream>

using namespace std;

class Stocznia{
    
    class Pracownik{
        friend class Stocznia;
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
    const string Nip;
    string nazwaStoczni;
    string kraj;
    string adres;
    int numerAdres;
    int rokZalozenia;
    Pracownik **pracownicy;
    size_t pracownicy_size = 10;
    Stocznia& operator=(Stocznia& stocznia);
    friend ostream& operator<<(ostream&, const Stocznia&);
    
public:
    //Stocznia
    Stocznia():Nip{to_string(rand()%100000+178923)}{
        stworz(pracownicy,pracownicy_size);
    }
    ~Stocznia(){
        usun(pracownicy,pracownicy_size);
    }
    Stocznia(const Stocznia& stocznia):Nip{to_string(rand()%100000+178923)}{
        this -> nazwaStoczni = stocznia.nazwaStoczni;
        this -> kraj = stocznia.kraj;
        this -> adres = stocznia.adres;
        this -> numerAdres = stocznia.numerAdres;
        this -> rokZalozenia = stocznia.rokZalozenia;
        stworz(pracownicy,pracownicy_size);
        for(size_t i =0;i < stocznia.pracownicy_size;i++){
            pracownicy[i]->set_imie(stocznia.pracownicy[i]->get_imie());
            pracownicy[i]->set_nazwisko(stocznia.pracownicy[i]->get_nazwisko());
            pracownicy[i]->set_rocznik(stocznia.pracownicy[i]->get_rocznik());
            pracownicy[i]->set_zawod(stocznia.pracownicy[i]->get_zawod());
            
        }
    }
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
    Pracownik& operator[](int);
    //Pracownik
    //tworzenie
    void stworz(Pracownik**& pracownicy,size_t size);
    //usuwanie
    void usun(Pracownik**& pracownicy,size_t size);
    void usun(int index);
    //wpisywanie
    void wpisz();
    //wprowadzanie
    void wprowadz();
    //wypisywanie
    void print();
    //wiek
    void WiekPracownikow();
};
void stworz(Stocznia**& stocznia);
void stworz(Stocznia**& stocznia, const size_t size);
void usun(Stocznia**& stocznia);
void usun(Stocznia**& stocznia, size_t& size);
void usun(Stocznia**& stocznia, size_t& size, int index);
void wpisz(Stocznia**& stocznia, size_t& size);
void wprowadz(Stocznia** stocznia, size_t size);
void print(Stocznia** stocznia, const size_t size);
void WiekStoczni(Stocznia** stocznia, size_t size);
void menu();

