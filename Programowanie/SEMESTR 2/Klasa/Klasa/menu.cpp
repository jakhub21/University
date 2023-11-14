#include <iostream>
#include "Klasa_h.h"
using namespace std;

void menu() {
    size_t size = 10;
    Pracownik* pracownik = nullptr;
    Stocznia** stocznia = nullptr;
    int opcja=1;
        do
        {
            cout<<"MENU"<<endl;
            cout<<"1.Utworz baze pracownikow"<<endl;
            cout<<"2.Wypisz pracownikow"<<endl;
            cout<<"3.Dodaj pracownika"<<endl;
            cout<<"4.Usun pracownika"<<endl;
            cout<<"5.Podaj wiek pracowników"<<endl;
            cout<<"6.Utworz baze stoczni"<<endl;
            cout<<"7.Wypisz stocznie"<<endl;
            cout<<"8.Dodaj stocznie"<<endl;
            cout<<"9.Usun stocznie"<<endl;
            cout<<"10.Podaj wiek stoczni"<<endl;
            cout<<"11.Wyjscie z programu."<<endl;
            cout<<"Wybierz opcje: ";
            cin>>opcja;
            switch (opcja)
            {
                case 1:
                    stworz(pracownik,size);
                    wprowadz(pracownik,size);
                    break;
                case 2:
                    print(pracownik,size);
                    break;
                case 3:
                    wpisz(pracownik,size);
                    break;
                case 4:
                    usun(pracownik,size,6);
                    break;
                case 5:
                    WiekPracownikow(pracownik,size);
                    break;
                case 6:
                    stworz(stocznia,size);
                    wprowadz(stocznia,size);
                    break;
                case 7:
                    print(stocznia,size);
                    break;
                case 8:
                    wpisz(stocznia,size);
                    break;
                case 9:
                    usun(stocznia,size,6);
                    break;
                case 10:
                    WiekStoczni(stocznia, size);
                    break;
                case 11:
                    usun(pracownik,size);
                    exit(1);
                    break;
                default:
                    break;
            }
            //system("pause");
            //system("cls");
            
        }while(true);
}

