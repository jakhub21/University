#include <iostream>
#include <stdlib.h>
#include "Stocznia.h"
using namespace std;

void menu() {
    size_t size = 10;
    Stocznia** stocznia = nullptr;
    int opcja=1;
    int index;
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
                    cout<<"Podaj index stoczni"<<endl;
                    cin>>index;
                    if(stocznia!=nullptr){
                        stocznia[index]->wprowadz();
                    }
                    else{
                        cout<<"Nie ma takiej stoczni"<<endl;
                    }
                    break;
                case 2:
                    cout<<"Podaj index stoczni"<<endl;
                    cin>>index;
                    stocznia[index]->print();
                    break;
                case 3:
                    cout<<"Podaj index stoczni"<<endl;
                    cin>>index;
                    stocznia[index]->wpisz();
                    break;
                case 4:
                    cout<<"Podaj index stoczni"<<endl;
                    cin>>index;
                    stocznia[index]->usun(6);
                    break;
                case 5:
                    cout<<"Podaj index stoczni"<<endl;
                    cin>>index;
                    stocznia[index]->WiekPracownikow();
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
                    cout<<"Podaj index stoczni"<<endl;
                    cin>>index;
                    usun(stocznia,size);
                    exit(1);
                    break;
                default:
                    break;
            }
            system( "read -n 1 -s -p \"Press any key to continue...\"" );
           
            
        }while(true);
}


