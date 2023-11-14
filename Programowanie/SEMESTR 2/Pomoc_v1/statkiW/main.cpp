#include <iostream>
using namespace std;

struct Gosc{
    string godnosc{"Karyna"};
};

/*void foo(int i){
    i = 55;
    cout<<i<<endl;

}*/
//funkcja przeladowana
void foo(int* i){
    *i = 775;
    cout<<*i<<"\t"<<i<<endl;

}
void foo(Gosc& g){
    g.godnosc = {"Grazyna"};
    cout<<g.godnosc<<endl;

}
void foo(Gosc* g){
    g->godnosc = {"Duren"};
    cout<<g->godnosc<<endl;

}
void print(Gosc tab[],int size){
    for(int i=0;i<size;i++){
        cout<<tab[i].godnosc<<endl;
    }
}

void stworz(int*&ptr_i){
    ptr_i = new int;
}
void usun(int *&ptr_i){
    delete ptr_i;
    ptr_i = nullptr;
}
void stworz(Gosc *&ptr_i){
    ptr_i = new Gosc;
}
void usun(Gosc *&ptr_i){
    delete ptr_i;
    ptr_i = nullptr;
}
void stworz(Gosc *&ptr_i,int size){
    ptr_i = new Gosc[size];
}
void usun(Gosc *&ptr_i,int size){
    delete [] ptr_i;
}
void stworz(Gosc **&ptr_i,int size){
    ptr_i = new Gosc*[size];
    for(int i=0;i<size;i++){
        ptr_i[i] = new Gosc;
    }
}
void usun(Gosc **&ptr_i,int size){
    for(int i=0;i<size;i++){
        delete ptr_i[i];
    }
    delete [] ptr_i;
}
int main(int argc, const char * argv[]) {
    int i {10};//i =10 na stosie
    int* ptr_i;//zmienna wskaznikowa, bedzie komorka ktora bedzie zajeta
    ptr_i =&i;//przypisanie i na miejsce ptr_i
    cout<<i<<"\t"<<ptr_i<<"\t"<<*ptr_i<<endl;
    i =20;//przypisywanie innego i
    cout<<i<<"\t"<<ptr_i<<"\t"<<*ptr_i<<endl;
    *ptr_i= 100000;//zmiana wskaznikowa i
    cout<<i<<"\t"<<ptr_i<<"\t"<<*ptr_i<<endl;
    int j{2};
    int* ptr_j;
    ptr_j = &j;
    *ptr_j = 700;
    cout<<*ptr_j<<endl;
    //foo(i);//wywolanie funkcji
    cout<<i<<endl;
    foo(&i);//wywolanie funkcji przeladowanej
    cout<<i<<"\t"<<ptr_i<<"\t"<<*ptr_i<<endl;
    Gosc s;
    foo(&s);
    cout<<s.godnosc<<endl;
    foo(s);
    cout<<s.godnosc<<endl;
    
    Gosc tab[7];
    print(tab,7);
    //Gosc *ptr;
    stworz(ptr_i);
    *ptr_i=10;
    cout<<i<<"\t"<<ptr_i<<"\t"<<*ptr_i<<endl;
    usun(ptr_i);
    Gosc *ptr;
    stworz(ptr);
    ptr->godnosc= "Szczescie";
    cout<<ptr->godnosc<<endl;
    usun(ptr);
    
    return 0;
}
