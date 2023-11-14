#include <iostream>
#include <locale>
#include <cstdlib>
#include <ctime>
using namespace std;

struct Pracownik
{
    string imie;
    string nazwisko;
    int rocznik;
    string zawod;
};

struct Stocznia
{
    string nazwaStoczni;
    string kraj;
    string adres;
    int numerAdres;
    int rokZalozenia;
};

//Opcje tworzenia
void stworz(Pracownik*& pracownik)
{
    pracownik = new Pracownik;
    
}

void stworz(Stocznia**& stocznia)
{
    stocznia = new Stocznia*;
    
}

void stworz(Pracownik*& pracownik, const int rozmiar)
{
    pracownik = new Pracownik[rozmiar];
}

void stworz(Stocznia**& stocznia, const int rozmiar)
{
    stocznia = new Stocznia*[rozmiar];
    for (int i = 0; i < rozmiar; i++)
    {
        stocznia[i] = new Stocznia;
    }
}

//Opcje usuwania
void usun(Pracownik*& pracownik)
{
    if(pracownik!=0)
    {
        free(pracownik);
        pracownik = NULL;
    }else
    {
        cout<<"Tablica jest pusta"<<endl;
    }
}

void usun(Stocznia**& stocznia)
{
    if(stocznia!=0){
        free(*stocznia);
        *stocznia = NULL;
    }else
    {
        cout<<"Tablica jest pusta"<<endl;
    }
}

void usun(Pracownik*& pracownik, const int rozmiar)
{
    if(pracownik!=0){
        delete [] pracownik;
        pracownik = nullptr;
    }else
    {
        cout<<"Tablica jest pusta"<<endl;
    }
}

void usun(Stocznia**& stocznia,int& rozmiar)
{
    if(stocznia!=0){
        for (int i = 0; i < rozmiar; i++)
            delete stocznia[i];
        delete[] stocznia;
        stocznia = nullptr;
        rozmiar = 0;
    }else
    {
        cout<<"Tablica jest pusta"<<endl;
    }
}

void usun(Pracownik*& pracownik, int& size, int index) {
    if (index < size) {
        Pracownik* temp = new Pracownik[size - 1];
        short int j{ -1 };
        for (int i = 0; i < size; ++i)
            if (i != index) {
                ++j;
                temp[j] = pracownik[i];
            }
        delete[] pracownik;
        pracownik = temp;
        --size;
    }
    else
        cout <<"Index nieprawidłowy" << endl;
}

void usun(Stocznia**& stocznia, int& size, int index) {
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


//Opcje wypisywania

void print(Pracownik* pracownicy) {
    if(pracownicy!=0){
        cout << "Pracownicy:" << endl;
        cout << pracownicy->imie << "\t" << pracownicy->nazwisko<< "\t" << pracownicy->rocznik<< "\t" << pracownicy->zawod << endl;
    }else
    {
        cout<<"Tablica jest pusta"<<endl;
    }
    }

void print(Pracownik* pracownicy, const int rozmiar) {
    if(pracownicy!=0){
        cout << "Pracownicy:" << endl;
        for (int i = 0; i < rozmiar; i++) {
            cout << pracownicy[i].imie << "\t" << pracownicy[i].nazwisko<< "\t" << pracownicy[i].rocznik<< "\t" << pracownicy[i].zawod << endl;
        }
    }else
    {
        cout<<"Tablica jest pusta"<<endl;
    }
}


void print(Stocznia** stocznia, const int rozmiar) {
    if(stocznia!=0){
        cout << "Stocznie:" << endl;
        for (int i = 0; i < rozmiar; i++) {
            cout<<stocznia[i]->nazwaStoczni<<"\t"<<stocznia[i]->kraj<<"\t"<<stocznia[i]->adres<<"\t"<<stocznia[i]->numerAdres<<"\t"<<stocznia[i]->rokZalozenia<<endl;
        }
    }else
    {
        cout<<"Tablica jest pusta"<<endl;
    }
}

//Opcja wpisywania
void wpisz(Pracownik* pracownik)
{
    cout<<"Imie:"<<endl;
    cin>>pracownik->imie;
    cout<<"Nazwisko:"<<endl;
    cin>>pracownik->nazwisko;
    cout<<"Rocznik:"<<endl;
    cin>>pracownik->rocznik;
    cout<<"Zawód:"<<endl;
    cin>>pracownik->zawod;
}

void wpisz(Pracownik*& pracownik,int &size)
{
    Pracownik* temp = new Pracownik[size + 1];
        if (size == 0) {
            temp = new Pracownik;
        }
        else {
            for (int i = 0; i < size; ++i)
                temp[i] = pracownik[i];
            delete[] pracownik;
        }
    pracownik = temp;
    cout<<"Imie:"<<endl;
    cin>>pracownik[size].imie;
    cout<<"Nazwisko:"<<endl;
    cin>>pracownik[size].nazwisko;
    cout<<"Rocznik:"<<endl;
    cin>>pracownik[size].rocznik;
    cout<<"Zawód:"<<endl;
    cin>>pracownik[size].zawod;
    size++;
}

void wpisz(Stocznia**& stocznia, int& size) {
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
    cin>>stocznia[size]->nazwaStoczni;
    cout<<"Kraj stoczni:"<<endl;
    cin>>stocznia[size]->kraj;
    cout<<"Adres:"<<endl;
    cin>>stocznia[size]->adres;
    cout<<"Numer stoczni:"<<endl;
    cin>>stocznia[size]->numerAdres;
    cout<<"Rok zalozenia stoczni:"<<endl;
    cin>>stocznia[size]->rokZalozenia;
    size++;
}



//Zmiana roku

void WiekPracownikow(Pracownik* pracownik,int size)
{
    time_t current_time;
    current_time = time(NULL);
    int rok = 1970 + current_time / 31537970;
    for(int i=0;i<size;i++){
    cout << pracownik[i].imie << "\t" << pracownik[i].nazwisko<< "\t" << rok-pracownik[i].rocznik<< "\t" <<   pracownik[i].zawod << endl;
    }
}

void WiekStoczni(Stocznia** stocznia,int size)
{
    time_t current_time;
    current_time = time(NULL);
    int rok = 1970 + current_time / 31537970;
    for(int i=0;i<size;i++){
        cout<<stocznia[i]->nazwaStoczni<<"\t"<<stocznia[i]->kraj<<"\t"<<stocznia[i]->adres<<"\t"<<stocznia[i]->numerAdres<<"\t"<<rok - stocznia[i]->rokZalozenia<<endl;
    }
}

//Inicjalizacja
void wprowadz(Pracownik* pracownik, int size)
{
    for (int i = 0; i < size; i++)
    {
        pracownik[i].imie = "adam";
        pracownik[i].nazwisko = "nowak";
        pracownik[i].rocznik = rand() % 120 + 1900;
        pracownik[i].zawod = "Pyper";
    }
}
void wprowadz(Stocznia** stocznia, int size)
{
    for (int i = 0; i < size; i++)
    {
        stocznia[i]->nazwaStoczni = "Kleven";
        stocznia[i]->kraj = "Norwegia";
        stocznia[i]->adres = "Topolowa";
        stocznia[i]->numerAdres =rand() % 100 + 0;
        stocznia[i]->rokZalozenia =rand() % 100 + 1900;
    }
}

int main() {
    int size =10;
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
                    usun(stocznia,size);
                    exit(1);
                    break;
                default:
                    break;
            }
            //system("pause");
            //system("cls");
            
        }while(true);
    return 0;
}
