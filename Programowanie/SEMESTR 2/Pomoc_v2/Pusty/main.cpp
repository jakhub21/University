#include <iostream>
//paradygmat spelnia 3 elementy zeby byc obiektowy
//agregacje bycie czescia innego bitu
//dziedziczenie cos jest rodzajem czegos
//nie ma senstu robienia w poliformizmie metody pokaz
using namespace std;
class Choroba{
    
};
class Osoba{
    size_t wiek{10};
public:
    Osoba(){cout<<"Konstruktor.O"<<endl;}
    virtual~Osoba(){cout<<"Destruktor.O"<<endl;}
    virtual size_t get(){return wiek;}
    virtual void rejestruj()=0;//metoda abstrakcyjna
};
class Student:public Osoba{
    
    
public:
    Student(){cout<<"Konstruktor.S"<<endl;}
    ~Student(){cout<<"Destruktor.S"<<endl;}
    virtual size_t get(){return 2*Osoba::get();}//rozbudowa dla podanej klasy
    virtual void rejestruj(){ //dziedziczenie
        cout<<"Student"<<endl;
    }
};
class Nauczyciel:public Osoba{
    Choroba*nerwica;
    
public:
    Nauczyciel(){cout<<"Konstruktor.N"<<endl;}
    ~Nauczyciel(){cout<<"Destruktor.N"<<endl;}
    virtual size_t get(){return 3*Osoba::get();}
    virtual void rejestruj(){ //dziedziczenie
        cout<<"Nauczyciel"<<endl;
    }
};
void foo(Osoba*os){
    cout<< os->get()<<endl;
    os->rejestruj();
}
void foo(Osoba&os){
    cout<< os.get()<<endl;
    os.rejestruj();
}

int main() {
    
    
    //DZIEDZICZENIE//
    //Osoba os;
    //cout<<os.get()<<endl;
    Student stud;
    cout<<stud.get()<<endl;
    stud.rejestruj();
    Nauczyciel nau;
    cout<<nau.get()<<endl;
    nau.rejestruj();
    
    
    //POLIMORFIZM//
    Osoba * stud1 = new Student;
    cout<< stud1->get()<<endl;
    stud1->rejestruj();
    Osoba * nau1 = new Nauczyciel;
    cout<< nau1->get()<<endl;
    nau1->rejestruj();
    
    //ZUTOWANIE NA TYP WSKAZNIKOWY I REFERENCYJNY//
    foo(stud1);
    foo(nau1);
    foo(*nau1);
    
    //KONTENER ZAWIERAJACY ROZEN TYPY//
    Osoba* tab[2];
    tab[0]= stud1;
    tab[1]= nau1;
    for(size_t i=0;i<2;i++){
        foo(tab[i]);
    }
    for(size_t i=0;i<2;i++){
        delete tab[i];
    }
    
    return 0;
}
