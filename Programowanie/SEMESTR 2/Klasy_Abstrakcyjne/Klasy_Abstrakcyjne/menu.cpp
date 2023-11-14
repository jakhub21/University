#include <iostream>
#include "Statek.h"
#include "Stocznia.h"
using namespace std;

void menu() {
    size_t size = 10;
    size_t sizeStatek = 10;
    Stocznia** stocznia = nullptr;
    Statek** statek = nullptr;
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
            cout<<"11.Dodaj statek."<<endl;
            cout<<"12.Wypisz statek."<<endl;
            cout<<"13.Dodaj statek."<<endl;
            cout<<"14.Usun statek."<<endl;
            cout<<"15.Oblicz ile km lub ile kg moze statek przejechac/przewiezc."<<endl;
            cout<<"16.Wyjscie z programu."<<endl;
            cout<<"Wybierz opcje: ";
            cin>>opcja;
            switch (opcja)
            {
                case 1:
                    cout<<"Podaj index stoczni"<<endl;
                    cin>>index;
                    if(stocznia!=nullptr){
                        stocznia[index]->stworz();
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
                    stworz(statek,sizeStatek);
                    wprowadz(statek,sizeStatek);
                    break;
                case 12:
                    print(statek,sizeStatek);
                    break;
                case 13:
                    wpisz(statek,sizeStatek);
                    break;
                case 14:
                    usun(statek,sizeStatek,6);
                    break;
                case 15:
                    for(int i=0; i<sizeStatek;i++){
                        statek[i]->droga();
                    }
                    break;
                case 16:
                    cout<<"Podaj index stoczni"<<endl;
                    cin>>index;
                    stocznia[index]->usun();
                    usun(statek,sizeStatek);
                    usun(stocznia,size);
                    exit(1);
                    break;
                default:
                    break;
            }
            //system("pause");
            //system("cls");
            
        }while(true);
}


