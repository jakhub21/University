#include <iostream>
#include <random>
#include <iostream>
#include <locale>
#include <string>
using namespace std;
//isnieje klasa pracownika ktora posiada poczatkowy wiek od 20 do 50 lat za pomoca konstruktora wygenerowac wiek i pesel pracownika
//wygenerowac tablice pracowników na podwojnym wskazniku o losowym rozmiarze
//losowy wiek i pesel
//stworzyc tablice obikt wskaznik do zus, zadanie okreslic status pracownika
//ilosc pracownikow moze byc mniej niz 200
//do zusu trzeba przekazywac kazdego pracownika
//index na pracowniku
//pracownika orzecza ZUS
//losowo podnosi sie wiek kazdemu pracownikowi
//na konic orzeczamy pracownika kazdego
//jesli wiek pracownika wiekszy niz 67 zmien status na Emeryt
//zworici zmienna i jego status
class Pracownik{
    int wiek;
    const int pesel;
public:
    int get_wiek(){return wiek;}
    const int get_pesel(){return pesel;}
    void set_wiek(int _wiek){wiek=_wiek;}
};

class ZUS{
    string status;
public:
    void Orzeczenie(const Pracownik);
    string get_status(){return status;}
    void set_status(string _status){status = _status;}
};
void wprowadz(Pracownik** pracownik, size_t size)
{
    for (int i = 0; i < size; i++)
    {
        pracownik[i]->set_wiek(rand() % 30 + 20);
        
    }
}
void wyswietl(Pracownik** pracownik, const size_t size) {
    if(pracownik!=0){
        cout << "Pracownicy:" << endl;
        for (int i = 0; i < size; i++) {
            cout << pracownik[i]->get_wiek() << endl;
        }
    }else
    {
        cout<<"Tablica jest pusta"<<endl;
    }
}
void wyswietlStatus(ZUS* status, const size_t size) {
    if(status!=0){
        cout << "Status:" << endl;
        for (int i = 0; i < size; i++) {
            cout << status[i].get_status() << endl;
        }
    }else
    {
        cout<<"Tablica jest pusta"<<endl;
    }
}
int main(){
    size_t iloscOrzeczen = rand() % 199 + 1;
    int dodanieLat = (rand() %  100+ 0);
    Pracownik** pracownik = nullptr;
    ZUS*status = nullptr;
    wprowadz(pracownik, iloscOrzeczen);
    for (int i; i< iloscOrzeczen; i++){
        pracownik[i]->get_wiek()+dodanieLat;
        if(pracownik[i]->get_wiek()<67){
            status[i].get_status() = "emeryt";
        }
        else{
            status[i].get_status() = "pracownik";
        }
    
    }
    wyswietlStatus(status, iloscOrzeczen);
    wyswietl(pracownik, iloscOrzeczen);

    
    
    

}
