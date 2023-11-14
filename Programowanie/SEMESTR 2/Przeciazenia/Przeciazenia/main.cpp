
#include "Stocznia.h"


int main () {
    Stocznia** stocznia = nullptr;
    stworz(stocznia,10);
    wprowadz(stocznia, 10);
    auto s=stocznia[1];
    s[1].wpisz();
    menu();
}


